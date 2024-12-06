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

    #TODO REFACTORIZAR
    def checkWin(self,row,col) -> bool:
        board = self.board

        win = False
        
        #DOWN
        try:
            if (board[row+1,col] == board[row+2,col] ==board[row+3,col] == board[row,col]):
                return True
        except:
            pass
        
        #UP
        try:
            if (board[row-1,col] == board[row+2,col] ==board[row+3,col] == board[row,col]):
                return True     
        except:
            pass

        #LEFT
        try:
            if (board[row,col-1] == board[row,col-2] ==board[row,col-3] == board[row,col]):
                return True     
        except:
            pass
    
        #RIGHT
        try:
            if (board[row,col+1] == board[row,col+2] ==board[row,col+3] == board[row,col]):
                return True     
        except:
            pass

        #RIGHT-UP
        try:
            if (board[row-1,col+1] == board[row-2,col+2] ==board[row-3,col+3] == board[row,col]):
                return True     
        except:
            pass
            

        
        #RIGHT-DOWN
        try:
            if (board[row+1,col+1] == board[row+2,col+2] ==board[row+3,col+3] == board[row,col]):
                return True     
        except:
            pass

        #LEFT-UP
        try:
            if (board[row-1,col-1] == board[row-2,col-2] ==board[row-3,col-3] == board[row,col]):
                return True     
        except:
            pass

        #LEFT-DOWN
        try:
            if (board[row+1,col-1] == board[row+2,col-2] ==board[row+3,col-3] == board[row,col]):
                return True     
        except:
            pass
        



        return False
    






if __name__ == "__main__":
    test = Game()
    print(test.board)
