"""Unit tests for the mazegen engine.

Run with:  python3 -m pytest -q
These tests are for development only; they are not graded.
"""

from __future__ import annotations

from collections import deque

from mazegen import MazeGenerator, N, E, S, W

Coord = tuple[int, int]


def free_cells(gen: MazeGenerator) -> set[Coord]:
    """All cells that are not part of the '42' glyph."""
    out: set[Coord] = set()
    for y in range(gen.height):
        for x in range(gen.width):
            if gen._is_free(x, y):
                out.add((x, y))
    return out


def reachable(gen: MazeGenerator, start: Coord) -> set[Coord]:
    """Flood fill from ``start`` through open walls only."""
    grid = gen.grid
    moves = ((0, -1, N), (1, 0, E), (0, 1, S), (-1, 0, W))
    seen = {start}
    queue: deque[Coord] = deque([start])
    while queue:
        x, y = queue.popleft()
        for dx, dy, bit in moves:
            if grid[y][x] & bit:
                continue
            nb = (x + dx, y + dy)
            if gen._is_free(*nb) and nb not in seen:
                seen.add(nb)
                queue.append(nb)
    return seen


def count_open_edges(gen: MazeGenerator) -> int:
    """Number of open walls between two free cells (counted once)."""
    grid = gen.grid
    edges = 0
    for y in range(gen.height):
        for x in range(gen.width):
            if not gen._is_free(x, y):
                continue
            if gen._is_free(x + 1, y) and not grid[y][x] & E:
                edges += 1
            if gen._is_free(x, y + 1) and not grid[y][x] & S:
                edges += 1
    return edges


def count_paths(gen: MazeGenerator, start: Coord, goal: Coord) -> int:
    """Count distinct simple paths from start to goal via open walls."""
    grid = gen.grid
    moves = ((0, -1, N), (1, 0, E), (0, 1, S), (-1, 0, W))
    seen: set[Coord] = set()
    total = 0

    def walk(cell: Coord) -> None:
        nonlocal total
        if cell == goal:
            total += 1
            return
        x, y = cell
        seen.add(cell)
        for dx, dy, bit in moves:
            if grid[y][x] & bit:
                continue
            nb = (x + dx, y + dy)
            if gen._is_free(*nb) and nb not in seen:
                walk(nb)
        seen.remove(cell)

    walk(start)
    return total


def test_seed_reproducibility() -> None:
    a = MazeGenerator(25, 20, (0, 0), (24, 19), seed=7)
    b = MazeGenerator(25, 20, (0, 0), (24, 19), seed=7)
    a.generate()
    b.generate()
    assert a.grid == b.grid
    assert a.solve() == b.solve()


def test_random_seed_is_concrete_and_reproducible() -> None:
    a = MazeGenerator(20, 15, (0, 0), (19, 14))  # no seed -> random
    a.generate()
    assert isinstance(a.seed, int)               # a real number, not None
    b = MazeGenerator(20, 15, (0, 0), (19, 14), seed=a.seed)
    b.generate()
    assert a.grid == b.grid                       # same seed -> same maze
    assert a.solve() == b.solve()


def test_connectivity() -> None:
    gen = MazeGenerator(25, 20, (0, 0), (24, 19), seed=1)
    gen.generate()
    cells = free_cells(gen)
    assert reachable(gen, gen.entry) == cells


def test_perfect_is_a_tree() -> None:
    gen = MazeGenerator(25, 20, (0, 0), (24, 19), perfect=True, seed=2)
    gen.generate()
    cells = free_cells(gen)
    # A connected graph with exactly V-1 edges is a tree, i.e. exactly
    # one path between any two cells.
    assert count_open_edges(gen) == len(cells) - 1


def test_perfect_has_exactly_one_entry_exit_path() -> None:
    gen = MazeGenerator(20, 15, (0, 0), (19, 14), perfect=True, seed=12)
    gen.generate()
    assert count_paths(gen, gen.entry, gen.exit) == 1


def test_detour_adds_a_second_route() -> None:
    # Build a perfect maze (one route), then add only the detour and
    # confirm a second route to the exit appears. Many seeds, no extra
    # loops, so the path count stays small and fast to enumerate.
    for seed in range(30):
        gen = MazeGenerator(12, 10, (0, 0), (11, 9),
                            perfect=True, seed=seed)
        gen.generate()
        assert count_paths(gen, gen.entry, gen.exit) == 1
        assert gen._add_alternative_path() is True
        assert count_paths(gen, gen.entry, gen.exit) >= 2


def test_imperfect_has_more_than_one_route_to_exit() -> None:
    # Full imperfect pipeline on a small maze: more than one path must
    # reach the exit.
    for seed in range(10):
        gen = MazeGenerator(8, 7, (0, 0), (7, 6),
                            perfect=False, seed=seed)
        gen.generate()
        assert count_paths(gen, gen.entry, gen.exit) >= 2


def test_imperfect_has_loops_and_no_open_3x3() -> None:
    gen = MazeGenerator(25, 20, (0, 0), (24, 19), perfect=False, seed=3)
    gen.generate()
    cells = free_cells(gen)
    assert count_open_edges(gen) > len(cells) - 1  # has loops
    for cy in range(gen.height - 2):
        for cx in range(gen.width - 2):
            assert not gen._is_open_block(cx, cy)


def test_border_walls_present() -> None:
    gen = MazeGenerator(25, 20, (0, 0), (24, 19), seed=4)
    gen.generate()
    grid = gen.grid
    for x in range(gen.width):
        assert grid[0][x] & N
        assert grid[gen.height - 1][x] & S
    for y in range(gen.height):
        assert grid[y][0] & W
        assert grid[y][gen.width - 1] & E


def test_glyph_cells_isolated() -> None:
    gen = MazeGenerator(25, 20, (0, 0), (24, 19), seed=5)
    gen.generate()
    assert gen._glyph  # the glyph fits in a 25x20 maze
    for x, y in gen._glyph:
        assert gen.grid[y][x] == (N | E | S | W)


def test_coherence_like_validator() -> None:
    gen = MazeGenerator(25, 20, (0, 0), (24, 19), seed=6)
    gen.generate()
    g = gen.grid
    h, w = gen.height, gen.width
    for r in range(h):
        for c in range(w):
            v = g[r][c]
            if r > 0:
                assert (v & 1) == ((g[r - 1][c] >> 2) & 1)
            if c < w - 1:
                assert ((v >> 1) & 1) == ((g[r][c + 1] >> 3) & 1)
            if r < h - 1:
                assert ((v >> 2) & 1) == (g[r + 1][c] & 1)
            if c > 0:
                assert ((v >> 3) & 1) == ((g[r][c - 1] >> 1) & 1)


def test_solve_follows_open_walls() -> None:
    gen = MazeGenerator(25, 20, (0, 0), (24, 19), seed=8)
    gen.generate()
    path = gen.solve()
    step = {"N": (0, -1, N), "E": (1, 0, E),
            "S": (0, 1, S), "W": (-1, 0, W)}
    x, y = gen.entry
    for letter in path:
        dx, dy, bit = step[letter]
        assert not gen.grid[y][x] & bit  # wall must be open
        x, y = x + dx, y + dy
    assert (x, y) == gen.exit


def test_glyph_at_minimum_size_stays_connected() -> None:
    # Glyph is 7x6 and needs a 1-cell margin -> minimum 9x8.
    gen = MazeGenerator(9, 8, (0, 0), (8, 7), seed=11)
    gen.generate()
    assert gen._glyph                       # the glyph fits exactly
    assert reachable(gen, gen.entry) == free_cells(gen)


def test_too_small_skips_glyph_but_stays_valid() -> None:
    gen = MazeGenerator(8, 8, (0, 0), (7, 7), seed=9)
    gen.generate()
    assert gen._glyph == set()           # skipped, too small
    assert reachable(gen, gen.entry) == free_cells(gen)
