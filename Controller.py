from Game import Game
from View import View
import pygame
from utils import *
import time

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
                        correct_Row =self.throwChip(col)
                        i = time.time()
                        self.view.upgradeBoard(row=correct_Row,col=col)
                        if(self.game.checkWin(correct_Row,col)):
                            print(f"Ha ganado {self.turn}")
                            self.running = False
                        print(f"Tiempo en hacer el algoritmo de resolver para saber si hay ganador{time.time() - i} s")
                        self.changeTurn()

    def throwChip(self, col):

        for row in  reversed(range(self.game.rows)):
            if self.game.board[row, col] == 0:
                self.game.board[row, col] = self.turn
                return row
                
    
    def changeTurn(self) : self.turn = YELLOW_TURN if self.turn == RED_TURN else RED_TURN





                    
        




        
