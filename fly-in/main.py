import sys
from router import Router
from simulation import Simulation
from parser import Parser


def main() -> None:
    if len(sys.argv) < 2:
        print("Filename not found.")
    else:
        try:
            graph = Parser().parse(sys.argv[1])
            path = Router(graph).find_path()
            if path is None:
                print("No path.")
            else:
                Simulation(graph, path).run()
        except (ValueError, FileNotFoundError) as e:
            print(f"Error: {e}")
            return



if __name__ == "__main__":
    main()
