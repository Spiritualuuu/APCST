print("Type your x value")
x = int(input())
print("Type your y value")
y = int(input())

if(x > 0 and y > 0):
    print("Quadrant 1")
elif(x < 0 and y > 0):
    print("Quadrant 2")
elif(x < 0 and y < 0):
    print("Quadrant 3")
elif(x > 0 and y < 0):
    print("Quadrant 4")
elif(x == 0 and not y == 0):
    print("X origin")
elif(not x == 0 and y == 0):
    print("Y origin")
else:
    print("Origin")