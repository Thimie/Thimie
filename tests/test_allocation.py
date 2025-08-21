 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a//dev/null b/tests/test_allocation.py
index 0000000000000000000000000000000000000000..d3fe0ba0066f96a3e5685ce7e0ebeb802ed45903 100644
--- a//dev/null
+++ b/tests/test_allocation.py
@@ -0,0 +1,17 @@
+from allocation_engine import Position, allocate_margin
+
+def test_allocation_proportional():
+    positions = [
+        Position("A", "", 100, 0.3, 30, 50),
+        Position("B", "", 200, 0.3, 60, 150),
+    ]
+    allocations, leftover = allocate_margin(positions, 100)
+    assert leftover == 0
+    assert round(allocations["A"], 2) == 25.00
+    assert round(allocations["B"], 2) == 75.00
+
+def test_allocation_caps_and_leftover():
+    positions = [Position("A", "", 100, 0.3, 30, 50)]
+    allocations, leftover = allocate_margin(positions, 80)
+    assert round(allocations["A"], 2) == 50.00
+    assert round(leftover, 2) == 30.00
 
EOF
)
