# Fly-in

## Description

Fly-in is a multi-drone pathfinding simulation (a variant of the classic
lem-in problem). Given a map describing a network of **zones** connected by
**links**, the program moves a fleet of drones from the `start_hub` to the
`end_hub`, turn by turn, while respecting zone types, zone capacities, and
connection capacities. The goal is to get every drone to the end in as few
turns as possible.

The project is fully object-oriented and type-safe (passes `mypy .`), and
builds its own graph without any external graph library.

## Instructions

Run the simulation on a map file:

```
python main.py <map_file>
```

(or, with the provided Makefile: `make run MAP=<map_file>`)

### Map file format

```
nb_drones: <positive integer>
start_hub: <name> <x> <y> [optional metadata]
end_hub:   <name> <x> <y> [optional metadata]
hub:       <name> <x> <y> [optional metadata]
connection: <zone1>-<zone2> [optional metadata]
# lines starting with '#' are comments
```

Optional metadata (defaults in parentheses):
- Zones: `zone=<normal|restricted|priority|blocked>` (normal),
  `max_drones=<n>` (1), `color=<value>` (none)
- Connections: `max_link_capacity=<n>` (1)

## Algorithm explanation

> NOTE: read this section carefully and rewrite anything that isn't already
> how *you* would explain it out loud — the defense asks you to explain the
> algorithm in your own words.

**Data model.** A custom `Graph` holds the zones (`dict[name -> Zone]`), the
start and end zones, an adjacency map (`dict[name -> list[neighbour names]]`)
for fast neighbour lookup, and a connections map
(`dict[(name1, name2) -> Connection]`). Each connection is stored under both
orderings `(a,b)` and `(b,a)`, so a link can be looked up in O(1) regardless
of direction.

**Parsing.** The parser validates the full map format — drone count, zone
definitions, connections, and optional metadata with defaults — and raises
clear errors for malformed input (bad drone count, invalid zone type,
non-positive capacities, duplicate names/connections, unknown zones, missing
start/end).

**Pathfinding (weighted Dijkstra).** Movement cost is a property of the
*destination* zone: entering a `restricted` zone costs 2 turns, everything
else costs 1, and `blocked` zones are never entered. A priority queue
(`heapq`) always expands the cheapest-reached zone next. To honour the
"priority zones are preferred" rule without distorting turn counts, the heap
key is a pair `(cost, -priority_count)`: cost is compared first, and ties are
broken toward routes passing through more priority zones. A `came_from` map
records how each zone was reached, and the path is rebuilt by walking it
backwards from end to start. If the end is unreachable, the search returns
`None` (handled gracefully).

**Simulation.** Each drone tracks its progress as an index along the path.
On every turn the program advances each unfinished drone by one step, subject
to two capacity checks: the destination zone must be below its `max_drones`
(start and end are unlimited), and the connection being crossed must be below
its `max_link_capacity` (reset to zero at the start of every turn). A move is
recorded as `D<id>-<zone>`; moves for a turn are printed on one line, and
drones that do not move are omitted. The simulation ends once every drone has
reached the end.

**Design decisions / trade-offs.**
- Connections stored in both directions (simpler, O(1) lookups) at a small
  memory cost.
- Priority handled as a tie-breaker rather than a cost change, so reported
  turn counts stay exact.
- Current version routes all drones along a single shortest path; distributing
  drones across multiple paths is a planned optimisation to reduce total turns.

## Visual representation

<!-- TODO: fill in once the visualization feature is built -->
Describe here the colored terminal output, how zone `color` metadata is used,
and how the display shows drone positions and movements each turn.

## Example

Input (`test.txt`):

```
nb_drones: 5
start_hub: hub 0 0 [color=green]
end_hub: goal 10 10 [color=yellow]
hub: roof1 3 4 [zone=restricted color=red]
hub: corridorA 4 3 [zone=priority max_drones=2]
connection: hub-roof1
connection: hub-corridorA
connection: roof1-goal
connection: corridorA-goal
```

Output:

```
D1-corridorA
D1-goal D2-corridorA
D2-goal D3-corridorA
D3-goal D4-corridorA
D4-goal D5-corridorA
D5-goal
```

Each line is one turn; each token `D<id>-<zone>` means drone `<id>` moved into
`<zone>`. The algorithm chooses the `corridorA` route (a priority zone) over
the equal-length `roof1` route (restricted, higher cost).
