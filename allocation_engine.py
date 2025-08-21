"""Simple allocation engine based on margin requirements and safe capacity."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple
import csv


@dataclass
class Position:
    ticker: str
    name: str
    value: float
    m: float  # maintenance requirement
    req_amt: float
    safe_loan: float  # safe capacity under 50% stress


def allocate_margin(positions: List[Position], margin_amount: float) -> Tuple[Dict[str, float], float]:
    """Allocate ``margin_amount`` across ``positions`` based on safe capacity.

    Returns a tuple of (allocations, leftover) where ``allocations`` is a
    mapping from ticker to allocated amount (capped at ``safe_loan``) and
    ``leftover`` is any margin that could not be deployed because all
    positions hit their safe capacity.
    """

    total_safe = sum(p.safe_loan for p in positions)
    if total_safe <= 0:
        return {p.ticker: 0.0 for p in positions}, margin_amount

    allocations: Dict[str, float] = {}
    for p in positions:
        weight = p.safe_loan / total_safe
        allocation = margin_amount * weight
        allocations[p.ticker] = min(allocation, p.safe_loan)

    leftover = margin_amount - sum(allocations.values())
    if leftover < 0:  # avoid tiny negative due to float rounding
        leftover = 0.0
    return allocations, leftover


def load_positions(path: str) -> List[Position]:
    positions: List[Position] = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            positions.append(
                Position(
                    ticker=row["Ticker"],
                    name=row["Name"],
                    value=float(row["Value"]),
                    m=float(row["M"]),
                    req_amt=float(row["ReqAmt"]),
                    safe_loan=float(row["SafeLoan_per_position"]),
                )
            )
    return positions


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Allocate margin across positions.")
    parser.add_argument("margin", type=float, help="Total margin to deploy")
    parser.add_argument(
        "--positions",
        default="data/positions.csv",
        help="CSV file containing position data",
    )
    args = parser.parse_args()

    positions = load_positions(args.positions)
    allocations, leftover = allocate_margin(positions, args.margin)
    print(f"Total allocated: {sum(allocations.values()):.2f}")
    if leftover:
        print(f"Leftover margin: {leftover:.2f}")
    for p in positions:
        print(f"{p.ticker}: {allocations[p.ticker]:.2f} (cap {p.safe_loan:.2f})")

