# Name- Alexander Koschnitzki
# Date- 11-18-21
# CSS- 225

# Number 4

# In ths problem, it is able to see if the number is a leap
# year or if it is not. You can be able to input any number
# to see if it is a leap year.

def is_leap(year):
    if (year % 4 == 0) and (year % 100 != 0):
        print("True")
    elif (year % 100 == 0) and (year % 400 != 0):
        print("False")
    elif (year % 400 == 0):
        print("True")
    else:
        print("False")

is_leap(800)