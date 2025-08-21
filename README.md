## Margin allocation tool

`allocation_engine.py` distributes available margin based on each holding's safe capacity. The default data lives in `data/positions.csv`.

Run the allocator with the amount of margin you want to deploy:

```bash
python allocation_engine.py 1163.74
```

Use `--positions` to point to a different CSV file.
