print("Type your grade.")
grade = float(input())

if(grade > 89.5 and grade <= 100):
    print("A")
elif(grade > 79.5 and grade <= 89.5):
    print("B")
elif(grade > 69.5 and grade <= 79.5):
    print("C")
elif(grade > 59.5 and grade <= 69.5):
    print("D")
elif(grade <= 59.5 and grade >= 0):
    print("F")
else:
    print("Error not valid.")