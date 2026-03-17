print(" Check Leap Year ")

year = int(input("enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year,"year is leap year")
else:
    print(year,"not a leap year")