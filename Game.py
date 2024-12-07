import numpy as np

#Model
class Game:

   

    def __init__(self):
        self.newGame()
       
    
    def newGame(self):
        self.board = np.zeros((6,7))
        self.throws = 0
        self.rows = 6
        self.col = 7

    def isFull(self, col) : return self.board[0 , col] != 0
    
    #TO MINIMAX FUNCTIONS UTILITIES
    def canPlay(col,board) : board[0][col] != 0

    def play(col,board,turn) -> None:

        for row in reversed(range(6)):
            if board[row][col] != 0:
                board[row][col] = turn



if __name__ == "__main__":
    test = Game()
    print(test.board)
