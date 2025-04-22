def Area(shape, radius, side1, side2):
    if(radius == 0):
        area = side1 * side2
    elif(radius > 0):
        area = 3.14 * (radius * radius)
    print(area)

Area("rectangle", 0, 2, 2)
Area("Circle", 2, 0, 0)
Area("rectangle", 0, 3, 6)
Area("Circle", 4, 0, 0)