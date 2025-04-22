def calc(num1, num2, oper):
    print("\n" + str(num1) + str(oper) + str(num2) + "=")
    if(oper == "+"):
        num1 = num1 + num2
    elif(oper == "-"):
        num1 = num1 - num2
    elif(oper == "*"):
        num1 = num1 * num2
    elif(oper == "/"):
        num1 = num1 / num2
    print(str(num1))

calc(1,2,"+")
calc(2,3,"-")
calc(3,4,"*")
calc(4,5,"/")