from Game import Game
from View import View
import pygame
from utils import *
import time
import math

#Controller
class Controller:

    
    
    def __init__(self, game:Game, view: View):

        self.game : Game = game
        self.view : View = view
        self.running = True
        self.turn = RED_TURN

    
    def mainLoop(self):
        
        self.view.on_init()
        
        while(self.running):
            events = self.view.get_events()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    row,col = self.view.get_cell(pygame.mouse.get_pos())
                    print(f"Fila {row} y columna {col}")
                    if not self.game.isFull(col):
                        
                        correct_Row =self.getGoodRow(col)
                        
                        self.throwChip(row=correct_Row,col=col)

                        self.view.upgradeBoard(row=correct_Row,col=col)

                        if(checkWin(correct_Row,col,self.game.board)):
                            print(f"Ha ganado {self.turn}")
                            self.running = False

                        self.changeTurn()
                        #self.negamax()

                # if event.type == pygame.MOUSEMOTION:
                #     row,col = self.view.get_cell(pygame.mouse.get_pos())
                #     if not self.game.isFull(col):
                #         correct_Row =self.getGoodRow(col)    
                #         self.view.possibleThrowPaint(correct_Row,col,self.turn)
                #     print("SI")


    def getGoodRow(self,col):
        for row in  reversed(range(self.game.rows)):
            if self.game.board[row, col] == 0:
                return row
            
    def throwChip(self, row,col): self.game.board[row, col] = self.turn
                
                
    def existMorePlayes(self,board) -> bool :
        for x in range(self.game.col):
            if( board[0][x] == 0):
                return True
        return False
    
    def changeTurn(self) : self.turn = YELLOW_TURN if self.turn == RED_TURN else RED_TURN


     #TODO make the alghoritm that works to the CPU IA throw the chips
    #max to cpu, min to human

    

    #TODO REFACTORIZAR
def checkWin(row,col,board) -> bool:
    

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
    