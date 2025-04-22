print("Type a year to check if it is a leap year.")
year = int(input())

if(year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0)):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year")