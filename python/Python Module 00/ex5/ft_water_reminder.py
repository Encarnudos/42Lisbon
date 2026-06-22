def ft_water_reminder():
    x = int(input("Days since last watering: "))
    y = 2
    if x > y:
        print("Water the plants!")
    elif x < y:
        print("Plants are fine")


ft_water_reminder()
