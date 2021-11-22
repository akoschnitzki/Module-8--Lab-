# Name- Alexander Koschnitzki
# Date- 11-18-21
# CSS- 225

# Number 2

# In this problem, you can input two numbers and it would
# let you know if the two number add up to 10, less then 10, or
# greater then 10.

def test_number():
    x = int(input("Enter first number :"))
    y = int(input("Enter second number :"))
    if x + y == 10:
       print("Equal to 10")
    elif x + y > 10:
       print("Greater then 10")
    elif x + y < 10:
       print("Less then 10")

test_number()