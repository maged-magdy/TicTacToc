from TicTacToc import *


if __name__ == '__main__':
    while 1:
        player1 = Player("X", 1)
        player2 = Player("O", 2)
        board = Board()
        game = Game()
        while 1:
            board.display_board()
            print(f"player 1 (X) turn.")
            player1.play(board)
            board.display_board()
            winner = game.check_win(board)
            if winner:
                print(f"player {winner} wins ")
                break
            elif board.is_full():
                print("Withdraw")
                break
            print(f"player 2 (O) turn.")
            player2.play(board)
            board.display_board()
            winner = game.check_win(board)
            if winner:
                print(f"player {winner} wins ")
                break
            elif board.is_full():
                print("Withdraw")
                break
        if game.replay():
            board.clear()
            continue
        else:
            break
