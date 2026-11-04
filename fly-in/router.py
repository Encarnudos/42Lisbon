from data_model import Graph, Zone
import heapq


class Router:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph

    def cost(self, zone: Zone) -> int:
        if zone.zone_type == "restricted":
            return 2
        return 1

    def find_path(self) -> list[str] | None:
        start_name = self.graph.start.name
        end_name = self.graph.end.name
        distance = {start_name: (0, 0)}
        came_from = {}
        queue: list[tuple[int, int, str]] = []
        if start_name == end_name:
            return [start_name]
        heapq.heappush(queue, (0, 0, start_name))
        while queue:
            cost, negate_prio, name = heapq.heappop(queue)
            priority_count = -negate_prio
            for neighbor in self.graph.adjacency[name]:
                if self.graph.zones[neighbor].zone_type == "blocked":
                    continue
                new_cost = cost + self.cost(self.graph.zones[neighbor])
                new_prio = priority_count + (1 if self.graph.zones[neighbor].zone_type == "priority" else 0)
                key = (new_cost, -new_prio)
                if key < distance.get(neighbor, (float("inf"), 0)):
                    distance[neighbor] = key
                    came_from[neighbor] = name
                    heapq.heappush(queue, (new_cost, -new_prio, neighbor))
        lista = [end_name]
        if end_name not in came_from: 
            return None
        current = end_name
        while current != start_name:
            current = came_from[current]
            lista.append(current)
        lista.reverse()
        return lista
