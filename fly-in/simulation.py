from data_model import Graph
from data_model import Zone
from data_model import Drone
from data_model import Connection
from visualization import colorize


class Simulation:
    def __init__(self, graph: Graph, path: list[str]) -> None:
        self.graph = graph
        self.path = path
        self.drones = []
        for i in range(1, graph.nb_drones + 1):
            self.drones.append(Drone(i, graph.start.name, self.path))


    def run(self) -> None:
        while not all(drone.index == len(self.path) - 1 for drone in self.drones):
            moves = []
            for connections in self.graph.connections.values():
                connections.current_load = 0
            for drone in self.drones:
                if drone.index != len(self.path) - 1:
                    next_zone = self.path[drone.index + 1]
                    current_zone = self.path[drone.index]
                    connections = self.graph.connections[(current_zone, next_zone)]
                    if next_zone == self.graph.end.name or self.count_in_zone(next_zone) < self.graph.zones[next_zone].max_drones:
                        if connections.current_load < connections.max_link_capacity:
                            drone.index += 1
                            connections.current_load += 1
                        moves.append(f"D{drone.id}-{self.path[drone.index]}")
            print(" ".join(moves))


    def count_in_zone(self, zone_name: str) -> int:
        count = 0
        for drone in self.drones:
            if self.path[drone.index] == zone_name:
                count += 1
        return count


    def display(self) -> None:
        for zone_name in self.path:
            
