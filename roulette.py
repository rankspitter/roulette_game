import random



class Node():
    def __init__(self, data):
        self.data = data
        self.next = None



class player:
    def __init__(self, money):
        self.player = money
        self.deler = 0


class roulette:
    def __init__(self):
        self.ball = 1
        self.wheel = [random.randint(0, 36) for i in range(37)  ]
        self.last = None


    def spin_the_wheel(self):
        pass





class betting_table:
    def __init__(self):
        self.table = [x for x in range(37)]




if __name__ == "__main__":

    money = int(input("How much money do you have? : "))
    play = player(money)

    r = roulette()
    print('-'*100)
    print(r.wheel)
    print('-'*100)

    table = betting_table()
    print(table.table)