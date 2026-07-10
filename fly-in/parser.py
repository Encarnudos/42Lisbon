from data_model import Graph, Zone, Connection


VALID_TYPES = {"normal", "blocked", "restricted", "priority"}


class Parser():
    def __init__(self) -> None:
        self.zones: dict[str, Zone] = {}
        self.start: Zone | None = None
        self.end: Zone | None = None
        self.connections: dict[tuple[str, str], Connection] = {}
        self.adjacency: dict[str, list[str]] = {}

    def parse(self, filename: str) -> Graph:
        with open(filename, "r") as f:
            lines = f.readlines()
            clean = [
                line.strip()
                for line in lines
                if line.strip() and not line.strip().startswith("#")
            ]
            if not clean:
                raise ValueError("File is empty or contains no valid lines")
            first = clean[0]
            if not first.startswith("nb_drones:"):
                raise ValueError(
                    "First line must be"
                    "'nb_drones: <positive_integer>'"
                )
            value = first.split(":", 1)[1].strip()
            try:
                nb_drones = int(value)
            except ValueError:
                raise ValueError(
                    f"nb_drones must be an integer,"
                    f"got: {value!r}"
                )
            if nb_drones < 1:
                raise ValueError(
                    f"nb_drones must be positive,"
                    f"got: {nb_drones}"
                )
            for line in clean[1:]:
                if line.startswith("start_hub:")\
                        or line.startswith("end_hub:")\
                        or line.startswith("hub:"):
                    self.parse_zone(line)
                elif line.startswith("connection:"):
                    self.parse_connection(line)
                else:
                    raise ValueError(f"Unknown line type: {line!r}")
        if self.start is None:
            raise ValueError("Map must have exactly one start_hub")
        if self.end is None:
            raise ValueError("Map must have exactly one end_hub")
        return Graph(self.zones, self.start, self.end, nb_drones)

    def parse_metadata(self, text: str) -> dict[str, str]:
        result: dict[str, str] = {}
        for pair in text.split():
            if "=" not in pair:
                raise ValueError(
                    f"Format of metadata should be key=value,"
                    f" got {pair!r}"
                )
            key, value = pair.split("=", 1)
            result[key] = value
        return result

    def parse_zone(self, text: str) -> None:
        if text.startswith("start_hub:"):
            kind = "start"
            rest = text.split(":", 1)[1].strip()
        elif text.startswith("end_hub:"):
            kind = "end"
            rest = text.split(":", 1)[1].strip()
        else:
            kind = "normal"
            rest = text.split(":", 1)[1].strip()
        if "[" in rest:
            core = rest.split("[", 1)[0].strip()
            metadata = rest.split("[", 1)[1]
            metadata = metadata.rstrip("]").strip()
        else:
            core = rest.strip()
            metadata = ""
        parts = core.split()
        if len(parts) != 3:
            raise ValueError(f"Zone must be 'name x y', got : {core!r}")
        name = parts[0]
        try:
            x = int(parts[1])
            y = int(parts[2])
        except ValueError:
            raise ValueError(
                f"Zone coordinates must be integers,"
                f"got {core!r}"
            )
        if "-" in name:
            raise ValueError(f"Zone name cannot contain '-': {name!r}")
        if name in self.zones:
            raise ValueError(f"Duplicate zone name: {name!r}")
        meta = self.parse_metadata(metadata)
        zone_type = meta.get("zone", "normal")
        if zone_type not in VALID_TYPES:
            raise ValueError(f"Invalid zone type; {zone_type!r}")
        raw = meta.get("max_drones", "1")
        try:
            max_drones = int(raw)
        except ValueError:
            raise ValueError(f"max_drones must be an integer, got {raw!r}")
        if max_drones < 1:
            raise ValueError(f"max_drones must be positive, got: {max_drones}")
        zone = Zone(name, x, y, zone_type, max_drones, [])
        self.zones[name] = zone
        if kind == "start":
            if self.start is not None:
                raise ValueError("Map must be exaclty one start_hub")
            self.start = zone
        elif kind == "end":
            if self.end is not None:
                raise ValueError("Map must have exactly one end_hub")
            self.end = zone

    def parse_connection(self, text: str) -> None:
        rest = text.split(":", 1)[1].strip()
        if "[" in rest:
            core = rest.split("[", 1)[0].strip()
            metadata = rest.split("[", 1)[1].strip()
            metadata = metadata.rstrip("]").strip()
        else:
            core = rest.strip()
            metadata = ""
        names = core.split("-")
        if len(names) != 2:
            raise ValueError(
                f"Connection must be 'name1-name2',"
                f"got: {core!r}"
            )
        name1, name2 = names
        meta = self.parse_metadata(metadata)
        if name1 not in self.zones:
            raise ValueError(f"Connection references unknown zone: {name1!r}")
        if name2 not in self.zones:
            raise ValueError(f"Connection references unknown zone: {name2!r}")
        raw = meta.get("max_link_capacity", "1")
        try:
            capacity = int(raw)
        except ValueError:
            raise ValueError(
                f"max_link_capacity must be an integer, got: {raw!r}"
            )
        if capacity < 1:
            raise ValueError(
                f"max_link_capacity must be a positive integer, got {capacity}"
            )
        if (name1, name2) in self.connections:
            raise ValueError(f"Duplicate connection: {name1}-{name2}")
        conn = Connection(name1, name2, capacity)
        self.connections[(name1, name2)] = conn
        self.connections[(name2, name1)] = conn



if __name__ == "__main__":
    p = Parser()
    for line in [
        "hub: bad 3 3 [zone=foo]",
        "hub: bad-name 1 1",
        "hub: short 3",
        "hub: nope 3 3 [max_drones=0]",
    ]:
        try:
            p.parse_zone(line)
            print(f"NO ERROR (unexpected): {line!r}")
        except ValueError as e:
            print(f"OK, raised: {e}")
