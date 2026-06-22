import sys


def ft_inventory_system():
    print("=== Inventory System Analysis ===")

    inventory = {}

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter'{arg}'")
            continue

        parts = arg.split(":")

        if len(parts) != 2:
            print(f"Error - invalid paramter:'{arg}'")
            continue

        name = parts[0]

        try:
            quantity = int(parts[1])
        except ValueError as e:
            print(f"Quantity error for'{name}': {e}")
            continue

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        inventory[name] = quantity
    print(f"Got inventory: {inventory}")
    items = list(inventory.keys())
    print(f"Item list: {items}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")
    for name, qty in inventory.items():
        percent = (qty / total) * 100 if total > 0 else 0
        print(f"Item {name} represents {round(percent, 1)}%")
    if inventory:
        max_item = None
        min_item = None
        for name in inventory:
            if max_item is None or inventory[name] > inventory[max_item]:
                max_item = name
            if min_item is None or inventory[name] < inventory[min_item]:
                min_item = name
        print(
            f"Item most abundant: {max_item}"
            f" with quantity {inventory[max_item]}"
        )
        print(
            f"Item least abundant: {min_item}"
            f" with quantity {inventory[min_item]}"
        )
        new_item = "magic_item"
        new_quantity = 1
        inventory[new_item] = new_quantity
        print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    ft_inventory_system()
