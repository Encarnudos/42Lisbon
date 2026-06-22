import math


def get_player_pos():
    while True:
        value = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = value.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(parts[0])
        except ValueError as e:
            print(f"Error on parameter'{parts[0]}': {e}")
            continue
        try:
            y = float(parts[1])
        except ValueError as e:
            print(f"Error on parameter'{parts[1]}': {e}")
            continue
        try:
            z = float(parts[2])
        except ValueError as e:
            print(f"Error on parameter'{parts[2]}': {e}")
            continue
        return (x, y, z)


def ft_coordinate_system():
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    distance = round(math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2), 4)
    print(f"Distance to center: {distance}")
    print()
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    distance2 = round(math.sqrt(
        (pos2[0]-pos1[0])**2 +
        (pos2[1]-pos1[1])**2 +
        (pos2[2]-pos1[2])**2
    ), 4)
    print(f"Distance between the 2 sets of coordinates: {distance2}")


if __name__ == "__main__":
    ft_coordinate_system()
