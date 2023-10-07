import random
import os

class Node:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.next = None

class Player:
    def __init__(self, money):
        self.money = money
    
    def bet(self, amount):
        amount_cleaned = amount.replace(' ', '').lower()

        if amount_cleaned == 'allin':
            if self.money == 0:
                print("You don't have any money left.")
                return False
            self.money -= self.money
            return self.money , True

        try:
            amount = int(amount)
            if amount > self.money:
                return False
            else:
                self.money -= amount
                print("You have " + str(self.money) + " dollars left")
                return True
        except ValueError:
            print("Please enter a valid number or 'all in'")
            return False



class Roulette:
    def __init__(self, value, color):
        self.head = Node(value[0], color[0])
        current = self.head
        self.value = value
        self.color = color
        for value, color in zip(value[1:], color[1:]):
            current.next = Node(value, color)
            current = current.next
        current.next = self.head

    def spin_the_wheel(self):
        random.shuffle(self.value)
        random_index = random.randint(0, 36)
        self.head = Node(self.value[random_index], self.color[self.value[random_index]])
        return self.head.value, self.head.color

class BettingTable:
    def __init__(self):
        self.betnumber = []
        self.groups = [
            [[3, 6, 9, 12], [2, 5, 8, 11], [1, 4, 7, 10]],
            [[15, 18, 21, 24], [14, 17, 20, 23], [13, 16, 19, 22]],
            [[27, 30, 33, 36], [26, 29, 32, 35], [25, 28, 31, 34]]
        ]

    def bet_number(self):
        input_numbers = input("Enter numbers you want to bet : \n")
        self.betnumber = list(map(int, input_numbers.split()))

    def show_table(self):
        groups = self.groups
        for i in range(len(groups[0])):
            for group in groups:
                row = ' '.join(map(str, group[i]))
                print(row, end='   ')
            print()
        print('  1st 12     2nd 12      3rd 12')
        print("1 to 18" + " " + "<" + "even>" + "|" + " " + "red" + "   " + "black" + " " + "|" + "<odd>" + "| " + "19 to 36")
        return " "

    def check_bet(self, result):
        return result in self.betnumber

if __name__ == "__main__":
    roulette_number = list(range(0, 37))
    black_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    roulette_colors = ['red' if i not in black_numbers else 'black' for i in roulette_number]
    roulette = Roulette(roulette_number, roulette_colors)

    while True:
        try:
            print(" ")
            print("Welcome to the roulette game")
            money = int(input("Insert your money : "))
            player = Player(money)
            print(player.money)
            break
        except ValueError:
            print("Please enter a valid amount")

    print()
    print("This is the betting table")
    print()
    table = BettingTable()
    print(table.show_table())
    print()

    while True:
        try:
            table.bet_number()
            break
        except ValueError:
            print("Please enter valid numbers")

    while True:
        try:
            result_number, result_color = roulette.spin_the_wheel()
            amount = input("How much do you want to bet : ")
            if player.bet(amount):
                if table.check_bet(result_number):
                    print(f"The ball landed on: {result_number} ({result_color})")
                    print("You win")
                    player.money += amount * 2
                    print(f"You have {player.money} left")
                else:
                    print(f"The ball landed on: {result_number} ({result_color})")
                    print("You lose")
                    print(f"You have {player.money} dollars left")
                    if player.money == 0:
                        print("you have been kicked out of the casino")
                        break
                    play_again = input("Do you want to play again? (y/n): ").lower()
                    if play_again == 'y':
                        table.bet_number()
                        continue
                    else:
                        break
            else:
                os.system('cls')
                print("You don't have enough money to bet")
                print("You have " + str(player.money) + " dollars left")
                print(" plase enter a valid amount ")
                print(table.show_table())
                print()
        except ValueError:
            print("Please enter a valid number")
