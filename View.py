from Game import Game
import pygame
from utils import *

#View
class View:
    
    BLOCKSIZE = 90
    
    def __init__(self, game:Game):
        self.game = game
        
        
    def on_init(self):
        
        self._display_surf = None
        self._running = True
        self.pygame = pygame
        self.pygame.init()
        self.SCREEN = pygame.display.set_mode((self.game.col * self.BLOCKSIZE,self.game.rows * self.BLOCKSIZE))
        self.clock = pygame.time.Clock()
        self.draw_board()

        

    def on_cleanup(self):
        pygame.quit()

    def draw_board(self):
        

        for row in range(self.game.rows):
            for col in range(self.game.col):
                x = col * self.BLOCKSIZE
                y = row * self.BLOCKSIZE
                rect = pygame.Rect(x, y, self.BLOCKSIZE, self.BLOCKSIZE)
                color = (200,200,200)
                pygame.draw.rect(self.SCREEN,color,rect)
                pygame.draw.rect(self.SCREEN,(0,0,0),rect,1)

        pygame.display.flip()
        self.clock.tick(60)

    def upgradeBoard(self,row,col):

        x = col * self.BLOCKSIZE
        y = row * self.BLOCKSIZE
        rect = pygame.Rect(x, y, self.BLOCKSIZE, self.BLOCKSIZE)
        color = RED_COLOR_RGB if self.game.board[row, col] == RED_TURN else YELLOW_COLOR_RGB
        pygame.draw.rect(self.SCREEN,color,rect)
        pygame.display.flip()






    def get_cell(self, pos):
        # Obtener las coordenadas de la celda según la posición del clic
        x, y = pos
        # // for a return int, not a double Ej. 18 // 5=  3

        fila = y // self.BLOCKSIZE
        columna = x // self.BLOCKSIZE

        if 0 <= fila < self.game.rows and 0 <= columna < self.game.col:
            return fila, columna
        return None
    

    def get_events(self) -> list : return pygame.event.get()

    def possibleThrowPaint(self,row,col,turn) -> None:

        x = col * self.BLOCKSIZE
        y = row * self.BLOCKSIZE
        rect = pygame.Rect(x, y, self.BLOCKSIZE, self.BLOCKSIZE)

        color = RED_LIGHT_COLOR_RGB if turn == RED_TURN else YELLOW_LIGHT_COLOR_RGB
        pygame.draw.rect(self.SCREEN,color,rect)
        pygame.display.flip()



        
        
    



    