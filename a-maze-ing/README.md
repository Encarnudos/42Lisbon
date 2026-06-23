# mazegen — engine documentation

> This is the Person A (engine) portion. Merge the relevant parts into
> the main `README.md` your colleague maintains.

## What the engine is

A single-file, pip-installable module (`mazegen.py`) exposing one class,
`MazeGenerator`. It builds a rectangular maze and can solve it. The shell
treats it as a black box: it only needs the constructor, `generate()`,
`grid`, `entry`, `exit`, and `solve()`.

## Wall encoding (same as the output file)

Each cell is an integer bitmask; a **set bit means the wall is closed**:

| Direction | Bit | Value |
|-----------|-----|-------|
| North     | 0   | 1     |
| East      | 1   | 2     |
| South     | 2   | 4     |
| West      | 3   | 8     |

A cell of `15` (`0b1111`) is fully closed; `0` is fully open. Because the
module uses the exact output-file scheme, the writer is just
`format(cell, "x")` per cell — no translation layer.

## Basic example

```python
from mazegen import MazeGenerator

gen = MazeGenerator(width=20, height=15, entry=(0, 0),
                    exit=(19, 14), perfect=True, seed=42)
gen.generate()

grid = gen.grid     # grid[y][x] -> bitmask of closed walls
start = gen.entry   # (x, y)
goal = gen.exit     # (x, y)
path = gen.solve()  # shortest path, e.g. "EESENEE..."
```

## Custom parameters

- `width` / `height`: maze size in cells.
- `entry` / `exit`: `(x, y)` coordinates; must differ and be in bounds.
- `perfect`: `True` for a perfect maze (exactly one path between entry
  and exit); `False` guarantees a second route reaches the exit, plus a
  few extra loops elsewhere.
- `seed`: same seed → same maze.

## Accessing the result

- `gen.grid` — the 2D list of cell bitmasks.
- `gen.entry` / `gen.exit` — the coordinates back.
- `gen.seed` — the integer seed that produced this maze.
- `gen.solve()` — shortest path as a string of `N`, `E`, `S`, `W`.

## Seed handling (SEED is a mandatory config key)

`SEED` is read from the config like every other key. Two cases:

- `SEED=12345` → the shell passes `seed=12345`; same value, same maze.
- `SEED=random` (or blank) → the shell passes `seed=None`; the engine
  picks a random seed, uses it, and exposes it as `gen.seed`. The shell
  can then print or store that number to reproduce the maze later.

The engine therefore always ends up with one concrete, retrievable seed,
whether the user fixed it or asked for a random one.

## How the shell (Person B) uses the engine

The shell treats `mazegen` as a black box. A minimal glue looks like:

```python
from mazegen import MazeGenerator

# ... config has already been parsed into these values ...
gen = MazeGenerator(
    width=cfg["WIDTH"], height=cfg["HEIGHT"],
    entry=cfg["ENTRY"], exit=cfg["EXIT"],
    perfect=cfg["PERFECT"], seed=cfg["SEED"],   # int, or None for random
)
gen.generate()

# 1) write the output file (hex grid, blank line, entry, exit, path)
with open(cfg["OUTPUT_FILE"], "w") as f:
    for row in gen.grid:
        f.write("".join(format(cell, "x") for cell in row) + "\n")
    f.write("\n")
    f.write(f"{gen.entry[0]},{gen.entry[1]}\n")
    f.write(f"{gen.exit[0]},{gen.exit[1]}\n")
    f.write(gen.solve() + "\n")

print(f"maze generated with seed {gen.seed}")

# 2) draw it: for each cell, gen.grid[y][x] tells which walls are closed
#    (bit 1 = N, 2 = E, 4 = S, 8 = W). "Re-generate" = call generate()
#    again; "show path" = gen.solve().
```

So the shell never needs to know *how* the maze is built — only the five
methods/properties above.

## Algorithm choice

- **Generation: depth-first search (recursive backtracker).** Easiest to
  implement, naturally produces a perfect maze (a spanning tree), and is
  well documented. An explicit stack is used instead of recursion so big
  mazes never hit Python's recursion limit.
- **Solving: breadth-first search.** BFS over the carved graph returns a
  shortest path, which the project requires.

The "42" glyph is stamped first as fully closed (isolated) cells and
excluded from carving; DFS then connects every remaining cell around it.
Each digit is 3×6 with one-cell-thick strokes and a 1-cell gap, centered,
needing a one-cell margin (minimum maze 9×8). Before stamping, the
engine checks that the free cells stay connected on all sides, and skips
the glyph with a message if they would not. For imperfect mazes, the
engine first opens a small parallel detour around one edge of the
entry-exit path (forcing a second route to the exit), then opens a few
more interior walls — always refusing any opening that would create a
fully open 3×3 block (so corridors stay ≤ 2 wide).

## Build the package

```bash
python3 -m build --wheel      # produces dist/mazegen-1.0.0-py3-none-any.whl
pip install dist/mazegen-1.0.0-py3-none-any.whl
```

## Tests (development only, not graded)

```bash
python3 -m pytest -q
```

Covered: seed reproducibility, connectivity, perfect-maze-is-a-tree,
imperfect loops with no open 3×3, border walls, isolated "42" cells,
neighbour wall coherence, solver correctness, and small-maze glyph skip.
