from data_model import Graph
from data_model import Drone
from visualization import colorize


class Simulation:
    def __init__(
            self, graph: Graph, path: list[str]
            ) -> None:
        self.graph = graph
        self.path = path
        self.drones = []

        for i in range(1, graph.nb_drones + 1):
            self.drones.append(Drone(i, self.path))

    def run(self) -> None:
        turns = 0
        while not all(
            drone.index == len(self.path) - 1 for drone in self.drones
        ):
            turns += 1
            moves = []
            for conn in self.graph.connections.values():
                conn.current_load = 0
            for drone in self.drones:
                if drone.index == len(self.path) - 1:
                    continue
                elif drone.in_flight:
                    drone.index += 1
                    drone.in_flight = False
                    moves.append(f"D{drone.id}-{self.path[drone.index]}")
                else:
                    next_zone = self.path[drone.index + 1]
                    current_zone = self.path[drone.index]
                    conn = self.graph.connections[(current_zone, next_zone)]
                    next_type = self.graph.zones[next_zone].zone_type
                    zone_room = (
                        next_zone == self.graph.end.name
                        or self.count_in_zone(next_zone)
                        < self.graph.zones[next_zone].max_drones
                    )
                    link_room = conn.current_load < conn.max_link_capacity
                    if zone_room and link_room:
                        if next_type == "restricted":
                            drone.in_flight = True
                            conn.current_load += 1
                            moves.append(
                                f"D{drone.id}-{current_zone}-{next_zone}"
                            )
                        else:
                            drone.index += 1
                            conn.current_load += 1
                            moves.append(
                                f"D{drone.id}-{self.path[drone.index]}"
                            )
            print(" ".join(moves))
            self.display()
        print(f"Total turns: {turns}")

    def count_in_zone(self, zone_name: str) -> int:
        count = 0
        for drone in self.drones:
            if self.path[drone.index] == zone_name:
                count += 1
        return count

    def display(self) -> None:
        cells = []
        for zone_name in self.path:
            ids = []
            for drone in self.drones:
                if self.path[drone.index] == zone_name:
                    ids.append(f"D{drone.id}")
            color = self.graph.zones[zone_name].color
            cell = colorize(zone_name, color) + f"[{','.join(ids)}]"
            cells.append(cell)
        print(" | ".join(cells))
