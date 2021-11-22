# Name- Alexander Koschnitzki
# Date- 11-18-21
# CSS- 225

# Number 3

# In this problem, you can input any number in a list and
# it is able to see if any number is a five. If it is a five,
# it would print that it is a five, if not it would print no.

def number():
    a = [2, 5, 8, 0, 10, 3, 1, 20]

    for item in a:
        if item == 5:
            print("5")
        else:
            print("Not 5")

number()
