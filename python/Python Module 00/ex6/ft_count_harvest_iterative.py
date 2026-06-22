def ft_count_harvest_iterative():
    x = int(input("Days until harvest: "))
    y = 1
    while y <= x:
        print("Day " + str(y))
        y += 1
    print("Harvest time!")


ft_count_harvest_iterative()
