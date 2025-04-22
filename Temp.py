def temp(temp, sym):
    if(sym == "C"):
        temp2 = (temp * (9/5)) + 32
    else:
        temp2 = (5/9) * (temp - 32)
    print(temp2)

temp(32, "C")
temp(45, "F")
temp(7, "F")