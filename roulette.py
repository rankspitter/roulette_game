class player:
    def __init__(self, money):
        self.money = money




class roulette:
    def __init__(self, ball) :
        self.ball = ball






class betting_table:
    def __init__(self):
        pass

    def roulette_board(self):
        number = []
        for i in range (1,37):
            number.append(i)
        return print(number)








class game:
    board = betting_table()
    board.roulette_board()







if __name__ == "__main__":
    start = game()




