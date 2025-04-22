print("Player 1 select:\n1. Rock\n2. Paper\n3. Scissors")
inputOne = int(input())
print("Player 2 select:\n1. Rock\n2. Paper\n3. Scissors")
inputTwo = int(input())

if(inputOne == 1 and inputTwo == 1):
    print("Draw")
elif(inputOne == 2 and inputTwo == 2):
    print("Draw")
elif(inputOne == 3 and inputTwo == 3):
    print("Draw")
if(inputOne == 1 and inputTwo == 2):
    print("Player Two Wins")
elif(inputOne == 1 and inputTwo == 3):
    print("Player One Wins")
elif(inputOne == 2 and inputTwo == 1):
    print("Player One Wins")
elif(inputOne == 2 and inputTwo == 3):
    print("Player Two Wins")
elif(inputOne == 3 and inputTwo == 1):
    print("Player Two Wins")
elif(inputOne == 3 and inputTwo == 2):
    print("Player One Wins")
else:
    print("Error")