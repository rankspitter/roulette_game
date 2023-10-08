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
            return self.money, True
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
        self.bet_options = ['dozen1', 'dozen2', 'dozen3', 'high', 'low', 'even', 'odd', 'red', 'black']
        self.betnumber = []
        self.special_bets = []
        self.groups = [
            [[3, 6, 9, 12], [2, 5, 8, 11], [1, 4, 7, 10]],[[15, 18, 21, 24], [14, 17, 20, 23], [13, 16, 19, 22]],[[27, 30, 33, 36], [26, 29, 32, 35], [25, 28, 31, 34]]
        ]
        self.special_bets_option = {
        'dozen1': list(range(1, 13)), 'dozen2': list(range(13, 25)), 'dozen3': list(range(25, 37)),
        'high': list(range(19, 37)), 'low': list(range(1, 19)), 'even': list(range(2, 37, 2)), 'odd': list(range(1, 36, 2)),
        }


    def bet_number(self):
        input_numbers = input("Enter numbers you want to bet : \n")
        self.betnumber = list(map(int, input_numbers.split()))
        if self.check_number():
            return True
    
    def bet_special(self):
        check_special = input("Do you want to bet on special bets? (y/n) : \n").lower()
        while check_special not in ['y', 'n', 'yes', 'no']:
            check_special = input("Do you want to bet on special bets? (y/n) : \n").lower() 
        if check_special == 'y' or check_special == 'yes':
            self.show_specialbet()
            input_special = input("Enter special bets you want to bet : \n")
            self.special_bets = list(input_special.split())
            print(self.special_bets)
            for bet in self.special_bets:
                if bet not in self.bet_options:
                    print(f'{bet} is not on the table')
                    return False    
            return True
        else:
            return True

    def special_process(self):
        for key, value in self.special_bets_option.items():
            if key in self.special_bets:
                for number in self.betnumber:
                    if number in value:
                        print(f'You win {key} {number} bet')
                        return True
        return False




    def check_number(self):
        for number in self.betnumber:
            if number not in range(0, 37):
                print(f'number {number} is not on the table')
                return False
        return True

    def show_table(self):
        groups = self.groups
        for i in range(len(groups[0])):
            for group in groups:
                row = ' '.join(map(str, group[i]))
                print(row, end='   ')
            print()
        print('  1st 12     2nd 12      3rd 12')
        print("1 to 18" + " " + "<" + "even>" + "|" + " " + "red" + "   " + "black" + " " + "|" + "<odd>" + "| " + "19 to 36")

    def show_specialbet(self):
        print("this is special bet")
        print(self.bet_options)


    def check_bet(self, result):
        return result in self.betnumber

class PlayRoulette:

    def __init__(self):
        self.roulette_number = list(range(0, 37))
        self.black_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
        self.roulette_colors = ['red' if i not in self.black_numbers else 'black' for i in self.roulette_number]
        self.roulette = Roulette(self.roulette_number, self.roulette_colors)
        self.table = BettingTable()

    def clear_screen(self):
        os.system('cls')
    
    def show_table(self):
        self.clear_screen()
        print("This is the betting table")
        print(self.table.show_table())
        while True:
            try:
                if self.table.bet_number():
                    try:
                        if self.table.bet_special() is True:
                            break
                        else:
                            self.table.bet_special()
                    except ValueError:
                        print("Please enter valid special bet\n")
            except ValueError:
                print("Please enter valid numbers\n")

    def start(self):
        while True:
            try:
                print("\nWelcome to the roulette game")
                money = int(input("Insert your money : "))
                if money <= 0:
                    print("Please enter a non-negative number.")
                else:
                    player = Player(money)
                    print(f"You have {player.money} dollars.")
                    break
            except ValueError:
                self.clear_screen()
                print("Please enter a valid amount")
        self.show_table()

        while True:
            try:
                result_number, result_color = self.roulette.spin_the_wheel()
                amount = input("How much do you want to bet : ")
                if player.bet(amount):
                    if self.table.check_bet(result_number):
                        if self.table.special_process() is True:
                            amount = int(amount)
                            player.money += amount * 2
                            print(f"You have {player.money} left")
                            break
                        print(f"The ball landed on: {result_number} ({result_color})")
                        print("You win")
                        amount = int(amount)
                        player.money += amount * 5
                        print(f"You have {player.money} left")
                        break
                    else:
                        print(f"The ball landed on: {result_number} ({result_color})")
                        print("You lose")
                        print(f"You have {player.money} dollars left")
                        if player.money == 0:
                            print("You have been kicked out of the casino")
                            break
                        play_again = input("Do you want to play again? (y/n): ").lower()
                        while play_again not in ['y', 'n', 'yes', 'no']:
                            play_again = input("Do you want to play again? (y/n): ").lower()
                        if play_again == 'y' or play_again == 'yes':
                            self.clear_screen()
                            self.show_table()
                        else:
                            break
                else:
                    self.clear_screen()
                    print("You don't have enough money to bet")
                    print(f"You have {player.money} dollars left")
                    print("Please enter a valid amount\n")
                    print(self.table.show_table())
            except ValueError:
                print("Please enter a valid number")

if __name__ == "__main__":
    play = PlayRoulette()
    play.start()