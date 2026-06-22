def ft_plant_age():
    x = int(input("Enter plant age in days: "))
    y = 60
    if x > y:
        print("Plant is ready to harvest!")
    elif x < y:
        print("Plant needs more time to grow.")


ft_plant_age()
