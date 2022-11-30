import random
import numpy as np
import pygame 
import time
def imprimir_laberinto(laberinto):

  #Cambiar 2 por 🟩
  #Cambiar 0 por 🟦
  #Cambiar 1 por 🟨

  # crear copia del laberinto
  laberinto_copia = laberinto.copy()
  for i in range(len(laberinto_copia)):
    for j in range(len(laberinto_copia[0])):
      if laberinto_copia[i][j] == '0':
        laberinto_copia[i][j] = '🟦'
      elif laberinto_copia[i][j] == '1':
        laberinto_copia[i][j] = '🟨'
      elif laberinto_copia[i][j] == '2':
        laberinto_copia[i][j] = '🟩'
# Printing the maze.
  

# Generar una cuadricula 
def generar_cuadricula(n, m, laberinto):

  laberinto = np.full((m, n), '0')
  
  for i in range(m):
    if i % 2 == 0:
      laberinto[i] = np.full(n, '0')
    else:
      for j in range(n):
        if j % 2 == 0:
          laberinto[i][j] = '0'
        else:
          laberinto[i][j] = '1'

  return laberinto

def obtener_vecinos(laberinto, i, j, visitados):

  vecinos = []

  if i > 1 and [i-2, j] not in visitados:
    vecinos.append([i-2, j])
  
  if i < len(laberinto)-2 and [i+2, j] not in visitados:
    vecinos.append([i+2, j])

  if j > 1 and [i, j-2] not in visitados:
    vecinos.append([i, j-2])

  if j < len(laberinto[0])-2 and [i, j+2] not in visitados:
    vecinos.append([i, j+2])

  return vecinos

def obtener_vecinos_solucion(laberinto, i, j, visitados):

  vecinos = []

  if i > 1 and [i-2, j] not in visitados:
    vecinos.append([i-2, j])
  
  if i < len(laberinto)-2 and [i+2, j] not in visitados:
    vecinos.append([i+2, j])

  if j > 1 and [i, j-2] not in visitados:
    vecinos.append([i, j-2])

  if j < len(laberinto[0])-2 and [i, j+2] not in visitados:
    vecinos.append([i, j+2])

  vecinos_solucion = []

  # Comprobar si entre el actual y el vecino hay un 1
  for vecino in vecinos:
    if vecino[0] == i and vecino[1] == j + 2 :
      if laberinto[i][j+1] == '1':
        vecinos_solucion.append(vecino)
    elif vecino[0] == i and vecino[1] == j - 2:
      if laberinto[i][j-1] == '1':
        vecinos_solucion.append(vecino)
    elif vecino[0] == i + 2 and vecino[1] == j:
      if laberinto[i+1][j] == '1':
        vecinos_solucion.append(vecino)
    elif vecino[0] == i - 2 and vecino[1] == j:
      if laberinto[i-1][j] == '1':
        vecinos_solucion.append(vecino)

  return vecinos_solucion


# Con DFS solucion de un laberinto
def solucionar_laberinto(laberinto, inicio, fin):
  
    visitados = []
    stack = []
    vecinos = []
  
    actual = inicio
  
    while True:
      visitados.append(actual)
  
      # Obtener vecinos
      vecinos = obtener_vecinos_solucion(laberinto, actual[0], actual[1], visitados)

      if vecinos:
        # Escoger un vecino al azar
        vecino = random.choice(vecinos)

        # Marcar el vecino como visitado
        visitados.append(vecino)
  
        # Insertar el vecino en la pila
        stack.append(actual)
  
        # Actualizar el actual
        actual = vecino
  
      else:
        if stack:
          actual = stack.pop()
        else:
          break
  
      if actual == fin:
        break

    # Marcar el camino
    for i in range(len(visitados)):
      if i < len(visitados)-1:
        actual = visitados[i]
        siguiente = visitados[i+1]
        # Obtener la coordenada entre visitados[i] y visitados[i+1]
        print(actual, siguiente)
        if actual[0] == siguiente[0]:
          if actual[1] < siguiente[1]:
            laberinto[actual[0]][actual[1]+1] = '2'
          elif actual[1] > siguiente[1]:
            laberinto[actual[0]][actual[1]-1] = '2'
        elif actual[1] == siguiente[1]:
          if actual[0] < siguiente[0]:
            laberinto[actual[0]+1][actual[1]] = '2'
          elif actual[0] > siguiente[0]:
            laberinto[actual[0]-1][actual[1]] = '2'

      laberinto[visitados[i][0]][visitados[i][1]] = '2'


def _main_():

  m = 41
  n = 41
  TILE = 10
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
  
  # Imprimir el laberinto\
  imprimir_laberinto(laberinto)

  # Solucionar el laberinto
  solucionar_laberinto(laberinto, [1, 1], [m-2, n-2])

  caminito = []
  for i in range(len(laberinto)):
      for j in range(len(laberinto[0])):
          if laberinto[i][j] == '2':
              caminito.append([i, j])

  caminito2 = caminito.copy()
  #que un circulo se mueva por el laberinto
  pygame.init()
  screen = pygame.display.set_mode((n*TILE, m*TILE))
  pygame.display.set_caption("Laberinto")
  clock = pygame.time.Clock()
  #posicion inicial
  running = True
  x = 1
  y = 1
  while running:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    screen.fill((0, 0, 0))
    for i in range(len(laberinto)):
      for j in range(len(laberinto[0])):
        if laberinto[i][j] == '1':
          pygame.draw.rect(screen, (255, 255, 255), (j*TILE, i*TILE, TILE, TILE))
        elif laberinto[i][j] == '2':
          pygame.draw.rect(screen, (200, 255, 255), (j*TILE, i*TILE, TILE, TILE))

    pygame.draw.circle(screen, (255, 0, 0), (x*TILE+5, y*TILE+5), 5)
    pygame.display.flip()
    movimientoAnterior = []
    if [y, x+1] in caminito:
      x += 1 
      #elimino la posicion de caminito
      movimientoAnterior.append("derecha")
      caminito.remove([y, x])
    elif [y+1, x] in caminito:
      y += 1
      movimientoAnterior.append("abajo")
      caminito.remove([y, x])
    elif [y, x-1] in caminito:
      x -= 1
      movimientoAnterior.append("izquierda")
      caminito.remove([y, x])
    elif [y-1, x] in caminito:
      y -= 1
      movimientoAnterior.append("arriba")
      caminito.remove([y, x])
    else:
      #si no hay camino, retrocedo
      #verificamos cuales casillas se pueden visitar
      clock.tick(100)
      if [y,x+1] in caminito2:
        caminito.append([y,x+1])
      if [y+1,x] in caminito2:
        caminito.append([y+1,x])
      if [y,x-1] in caminito2:
        caminito.append([y,x-1])
      if [y-1,x] in caminito2:
        caminito.append([y-1,x])
  
    clock.tick(40)
    if x == n-2 and y == m-2:
      pygame.mixer.init()
      sonido = pygame.mixer.Sound("videoplayback.wav")
      sonido.play()
      #mostramos una imagen de victoria
      imp = pygame.image.load("ye.png").convert()
      #ajustamos el tamaño de la imagen
      imp = pygame.transform.scale(imp, (n*TILE, m*TILE))
      screen.blit(imp, (0, 0))
      pygame.display.flip()
      time.sleep(7)
      break
  pygame.quit()


if __name__ == "__main__":
  _main_()