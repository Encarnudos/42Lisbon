"""Mock maze generator for shell (Person B) development.

Conforms to the agreed MazeGenerator contract so the config parser,
output writer, and display can be built and tested before the real
engine exists. Swap the import for the real module once it lands;
nothing else in the shell should need to change.

The mock returns a fixed, hand-verified 4x4 perfect maze. It ignores
the constructor's size/entry/exit on purpose and exposes its own, so
that grid + entry + exit + path stay mutually consistent and the
validation script passes. The real generator WILL honor those args.

While developing against this mock, use a config of:
    WIDTH=4 / HEIGHT=4 / ENTRY=0,0 / EXIT=3,3 / PERFECT=True
"""
from __future__ import annotations


class MazeGenerator:
    """Hardcoded 4x4 perfect maze matching the contract interface."""

    # grid[y][x] = bitmask of CLOSED walls.  N=bit0(1) E=bit1(2)
    # S=bit2(4) W=bit3(8).  Bit set => wall closed.  Borders are walled,
    # adjacent cells agree on every shared wall, single path between any
    # two cells (a boustrophedon spanning tree).
    _GRID: list[list[int]] = [
        [0xD, 0x5, 0x5, 0x3],
        [0x9, 0x5, 0x5, 0x6],
        [0xC, 0x5, 0x5, 0x3],
        [0xD, 0x5, 0x5, 0x6],
    ]
    # Shortest (here, only) path (0,0) -> (3,3), snaking through the rows.
    _PATH: str = "EEESWWWSEEES"

    def __init__(
        self,
        width: int,
        height: int,
        entry: tuple[int, int],
        exit: tuple[int, int],
        perfect: bool = True,
        seed: int | None = None,
    ) -> None:
        """Store params. The mock ignores them but keeps the signature."""
        self._width = width
        self._height = height
        self._entry = entry
        self._exit = exit
        self._perfect = perfect
        self._seed = seed
        self._generated = False

    def generate(self) -> None:
        """Build the maze. The mock just marks itself ready."""
        self._generated = True

    @property
    def grid(self) -> list[list[int]]:
        """Return grid[y][x] = bitmask of closed walls (a copy)."""
        if not self._generated:
            raise RuntimeError("call generate() before accessing grid")
        return [row[:] for row in self._GRID]

    @property
    def entry(self) -> tuple[int, int]:
        """Return entry coordinates as (x, y). Mock fixes it at (0, 0)."""
        return (0, 0)

    @property
    def exit(self) -> tuple[int, int]:
        """Return exit coordinates as (x, y). Mock fixes it at (3, 3)."""
        return (3, 3)

    def solve(self) -> str:
        """Return the shortest entry->exit path as N/E/S/W letters."""
        if not self._generated:
            raise RuntimeError("call generate() before solve()")
        return self._PATH


if __name__ == "__main__":
    m = MazeGenerator(4, 4, (0, 0), (3, 3))
    m.generate()
    for row in m.grid:
        print("".join(f"{cell:X}" for cell in row))
    print()
    print(f"{m.entry[0]},{m.entry[1]}")
    print(f"{m.exit[0]},{m.exit[1]}")
    print(m.solve())
