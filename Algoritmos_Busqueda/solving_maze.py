import numpy as np
import pygame as pg
from heapq import *
import random
from solving_maze2 import *



def get_circle(x, y):
    return (x * TILE + TILE // 2, y * TILE + TILE // 2), TILE // 4


def get_rect(x, y):
    return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2


#impresion de laberinto
def _main_():
 
  m = 41
  n = 41
  
  laberinto = []
  visitados = []
  stack = []
  vecinos = []

  # Generar una cuadricula
  laberinto = generar_cuadricula(n, m, laberinto)
  imprimir_laberinto(laberinto)

  actual = [1, 1]

  # Con DFS generar un laberinto
  while True:

    visitados.append(actual)

    # Obtener vecinos
    vecinos = obtener_vecinos(laberinto, actual[0], actual[1], visitados)

    if vecinos:
      # Escoger un vecino al azar
      vecino = random.choice(vecinos)

      # Marcar el vecino como visitado
      visitados.append(vecino)

      # Insertar el vecino en la pila
      stack.append(actual)

      # Eliminar la pared entre el vecino y el actual
      laberinto[int((actual[0]+vecino[0])/2)][int((actual[1]+vecino[1])/2)] = '1'

      # Actualizar el actual
      actual = vecino

    else:
      if stack:
        actual = stack.pop()
      else:
        break
  
  # Imprimir el laberint

  # Modificar el laberinto para que tenga mas caminos posibles
  # Agregar caminos aleatorios para conectar nodos
  for i in range(35):
    x = random.randint(1, n-2)
    y = random.randint(1, m-2)
    laberinto[x][y] = '1'

  laberinto_para_dijkstra = laberinto.copy()
  start_time_dijkstra = time.time()
  return laberinto

#creamos la funcion para solucionar el laberinto con dijkstra
laberinto_para_dijkstra = _main_()
m = 41
n = 41
solucionar_laberinto_dijsktra(laberinto_para_dijkstra, [1, 1], [m-2, n-2])

#tomamos el camino que nos da dijkstra y lo metemos en el laberinto como 2
for i in range(len(solucionar_laberinto_dijsktra(laberinto_para_dijkstra, [1, 1], [m-2, n-2]))):
    #si esa casilla esta en el camino que nos dio dijkstra lo insertamos como 2
    if solucionar_laberinto_dijsktra(laberinto_para_dijkstra, [1, 1], [m-2, n-2])[i] in solucionar_laberinto_dijsktra(laberinto_para_dijkstra, [1, 1], [m-2, n-2]):
        laberinto_para_dijkstra[solucionar_laberinto_dijsktra(laberinto_para_dijkstra, [1, 1], [m-2, n-2])[i][0]][solucionar_laberinto_dijsktra(laberinto_para_dijkstra, [1, 1], [m-2, n-2])[i][1]] = '2'

#imprimimos el laberinto con el camino que nos dio dijkstra
imprimir_laberinto(laberinto_para_dijkstra)

