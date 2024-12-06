'''The execution of the game start in this file'''
from Game import Game
from View import View
from Controller import Controller

model = Game()

view = View(model)

controller : Controller = Controller(model, view)


controller.mainLoop()