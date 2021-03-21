class Player:
    # class for modeling players

    def __init__(self, symbol, turn):
        self.symbol = symbol  # contains symbol x or o
        self.turn = turn  # contains the turn of the player instance

    def choose_symbol(self):
        # method for letting the player choose his symbol

        while self.symbol != "X" and self.symbol != "x" and self.symbol != "O" and self.symbol != "o":
            self.symbol = input("first player Choose X or O : ")
            if self.symbol == "X" or self.symbol == "x":
                self.symbol = self.symbol.upper()
            elif self.symbol == "o" or "O":
                self.symbol = self.symbol.upper()

    def play(self, board):
        # method for letting the player play
        # takes the board and location of the mark
        while True:
            try:
                location = int(input("Enter desired position : "))
                if board.is_location_empty(location):
                    board.board[location] = self.symbol
                    break
                else:
                    print("=========================")
                    print("choose an empty space")
            except IndexError:
                print("=========================")
                print("Enter a value from 1 -> 9")
                continue
            except ValueError:
                print("=========================")
                print("Enter a value from 1 -> 9")
                continue


# class for modeling the board as list
class Board:
    def __init__(self):
        self.board = ["0", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def is_location_empty(self, location):
        if self.board[location] == " ":
            return True
        else:
            return False

    # display_board
    def display_board(self):
        for _ in range(0, 100):
            print("\n")
        print('''==============TicTacToc game==============''')
        for i in range(9, 0, -3):
            print("                 ----- ")
            print(f"                |{self.board[i - 2]}|{self.board[i - 1]}|{self.board[i]}|")
        print("                 ----- ")
        print('''==========================================''')

    # is board full?
    def is_full(self):
        empty_places = 0
        full_places = 0
        for i in range(1, 10):
            if self.is_location_empty(i):
                return False
        return True

    def clear(self):
        self.board = ["0", " ", " ", " ", " ", " ", " ", " ", " ", " "]


class Game:

    def check_win(self, board):
        if board.board[9] == "X" and board.board[8] == "X" and board.board[7] == "X":
            return 1
        if board.board[9] == "O" and board.board[8] == "O" and board.board[7] == "O":
            return 2
        if board.board[9] == "X" and board.board[6] == "X" and board.board[3] == "X":
            return 1
        if board.board[9] == "O" and board.board[6] == "O" and board.board[3] == "O":
            return 2
        if board.board[7] == "X" and board.board[4] == "X" and board.board[1] == "X":
            return 1
        if board.board[7] == "O" and board.board[4] == "O" and board.board[1] == "O":
            return 2
        if board.board[1] == "X" and board.board[2] == "X" and board.board[3] == "X":
            return 1
        if board.board[1] == "O" and board.board[2] == "O" and board.board[3] == "O":
            return 2
        if board.board[7] == "X" and board.board[5] == "X" and board.board[3] == "X":
            return 1
        if board.board[7] == "O" and board.board[5] == "O" and board.board[3] == "O":
            return 2
        if board.board[4] == "X" and board.board[5] == "X" and board.board[6] == "X":
            return 1
        if board.board[4] == "O" and board.board[5] == "O" and board.board[6] == "O":
            return 2
        if board.board[8] == "X" and board.board[5] == "X" and board.board[2] == "X":
            return 1
        if board.board[8] == "O" and board.board[5] == "O" and board.board[2] == "O":
            return 2
        if board.board[9] == "X" and board.board[5] == "X" and board.board[1] == "X":
            return 1
        if board.board[9] == "O" and board.board[5] == "O" and board.board[1] == "O":
            return 2
        else:
            return 0

    def replay(self):
        while True:
            ans = input("want to play again? (y/n) : ")
            if ans == "Y" or ans == "y":
                return True
            elif ans == "n" or ans == "N":
                return False
            else:
                continue
