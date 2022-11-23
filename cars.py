import os
import random
import time
import threading

inicioponte = 10
largoponte = 35

cantcars = 5

class car(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.9)

  def avanzar(self):
    time.sleep(1-self.velocidad)
    self.posicion += 1

  def dist(self):
    print(' ' * self.posicion + '🚗') 

  def run(self):
    while(True):
      self.avanzar()

cars = []
for i in range(cantcars):
  v = car()
  cars.append(v)
  v.start() 

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def distponte():
  print(' ' * inicioponte + '=' * largoponte)

while(True):
    
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  print()
  distponte()
  for v in cars:
    v.dist()
  distponte()
  time.sleep(0.1)