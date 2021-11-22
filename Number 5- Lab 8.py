# Name- Alexander Koschnitzki
# Date- 11-18-21
# CSS- 225

# Problem 5

# In this problem, I was able to create a function to be
# able to check certain tasks and checks against any status effect.
# It is able to print the statement when you choose the number.


class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self. weaknesses

    def profile(self):
        return self.nickname, self.weapons, self. weaknesses
    def check_equipment(self, taskL, state):
        missing_item = []
        for item in range(len(taskL)):
            if taskL[item] not in self.weapons:
                missing_item.append(taskL[item])
                print("{} is not ready".format(taskL[item]))
            if len(missing_item) == 0:
                print("Confirmed all items are prepared")

        if state == self.weaknesses[0]:
            print("Player's status is {}, which is not allowed condition".format(state))
        else:
            print("Player is in good condition")


player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)
print("There are three task that you can choose from.")
print("1. Task 1 - Climb a mountain.")
print("2. Task 2 - Cook a meal.")
print("3. Task 3 - Write a book.")
option = input("Please enter one of the following options(1-3):")

if option == "1":
    task = ["rope", "coat", "first aid kit"]
    not_allowed_state = "slow"
if option == "2":
    task = ['pan', 'groceries']
    not_allowed_state = 'small'
if option == "3":
    task = ['pen', 'paper']
    not_allowed_state = 'confusion'


player1.check_equipment(task, not_allowed_state)
