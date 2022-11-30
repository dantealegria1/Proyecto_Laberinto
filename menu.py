import pygame 
import pygame_menu
from solving_maze2 import *
from solving_maze2 import _main_Dick
from nuevoLaberinto_DFS_funcionandp import *
from nuevoLaberinto_DFS_funcionandp import _main_
from solving_maze_3 import *
from solving_maze_3 import _main_BetoGay
from solving_maze_4 import *
from solving_maze_4 import _main_AlgoritmoParaSolucionarAEstrellaHechaPorYyeyoMoreno
#iniciar automaticamente 
pygame.init()
pygame.mixer.init()
surface = pygame.display.set_mode((600, 400))

def DFS():
    _main_()

def Dijkstra():
    _main_Dick()

def BFS():
    _main_BetoGay()

def AStar():
    _main_AlgoritmoParaSolucionarAEstrellaHechaPorYyeyoMoreno()

menu = pygame_menu.Menu('Laberinto', 600, 400,
                theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Nombre :', default='')
menu.add.button('DFS',DFS)
menu.add.button('Dijkstra',Dijkstra)
menu.add.button('BFS',BFS)
menu.add.button('A*',AStar)
menu.add.button('Salir', pygame_menu.events.EXIT)

menu.mainloop(surface)