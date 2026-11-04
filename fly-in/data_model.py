class Drone():
    def __init__(
            self, id: str, current_pos: str,
            path: list[str], index: int = 0
    ) -> None:
        self.id = id
        self.current_pos = current_pos
        self.path = path
        self.index = index


class Zone():
    def __init__(
            self, name: str, x: int, y: int, zone_type: str,
            max_drones: int, drones: list[Drone], color: str = "none"
    ) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.zone_type = zone_type
        self.max_drones = max_drones
        self.drones = drones
        self.color = color


class Connection():
    def __init__(
            self, name1: str, name2: str,
            max_link_capacity: int
    ) -> None:
        self.name1 = name1
        self.name2 = name2
        self.max_link_capacity = max_link_capacity
        self.current_load: int = 0


class Graph():
    def __init__(
            self, zones: dict[str, Zone],
            start: Zone, end: Zone, nb_drones: int,
            adjacency: dict[str, list[str]],
            connections: dict[tuple[str, str], Connection],
    ) -> None:
        self.zones = zones
        self.start = start
        self.end = end
        self.nb_drones = nb_drones
        self.adjacency = adjacency
        self.connections = connections
