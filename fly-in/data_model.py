from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Drone:
    id: int
    path: list[str]
    index: int = 0
    in_flight: bool = False


@dataclass
class Zone:
    name: str
    x: int
    y: int
    zone_type: str
    max_drones: int
    color: str = "none"


@dataclass
class Connection:
    name1: str
    name2: str
    max_link_capacity: int
    current_load: int = field(default=0, init=False)


@dataclass
class Graph:
    zones: dict[str, Zone]
    start: Zone
    end: Zone
    nb_drones: int
    adjacency: dict[str, list[str]]
    connections: dict[tuple[str, str], Connection]
