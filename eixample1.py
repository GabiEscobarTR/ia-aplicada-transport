import random
from math import *
import numpy as np
import matplotlib.pyplot as plt
import time



TIME_STEP = 1


class Car():
  
  def __init__(self, x, y, speedX, speedY):
      self.x = x
      self.y = y
      self.speedX = speedX
      self.speedY = speedY

  def move(self, map):
      newX = self.x + self.speedX*TIME_STEP
      newY = self.y + self.speedY*TIME_STEP
      if map.get(newX, newY) == 0:
        self.x = newX
        self.y = newY
        
      else:
          print("Explosion")
    

class Map():
    
    def __init__(self, sizeX, sizeY):
        self.grid = np.ones((sizeX, sizeY))
        for i in range(0, sizeX, 10):
            self.grid[i,:] = 0
            #self.grid[i+1,:] = 0
            if all(self.grid[i,:]) == 0:
                availableX = self.grid[i,:]
        for j in range(0, sizeY, 10):
            self.grid[:,j] = 0
            #self.grid[:,j+1] = 0
            if all(self.grid[:,j]) == 0:
                availableY = self.grid[:,j]
    def show(self):
      plt.imshow(self.grid)
      
    def get(self, x, y):
      return self.grid[x,y]
     


class Game():
  
  def __init__(self, map, cars):
    self.map = map
    self.cars = cars
    
  def step(self):
    for car in self.cars:
      car.move(self.map)
      self.collisions() 

  def show(self):
    self.map.show()
    for car in self.cars:
      plt.scatter(car.x, car.y, c='green')
      self.map.grid[car.x, car.y] = 1
      self.map.grid[car.x, car.y] = 0
    plt.show()
     
  def collisions(self):  # necessita replantejament
    for car in self.cars:
      if self.map.grid[car.x,car.y] == 1:
          print("Explosion")
          raise 
          


def generate_route(map, oriX, oriY, destX, destY):
  """
  """
  if not map.get(oriX, oriY) == 0:
    print("Origin direction is not valid.")
    raise
    
  if not map.get(destX, destY) == 0:
    print("Destiny direction is not valid.")
    raise
  
  if len(route) == 0:
    route = [(oriX, oriY)]
    
  if map.get(oriX or oriY or destX or destY) == 0:
      distX = destX - oriX
      return distX
      distY = destY - oriY
      return distY
  #...
  




      
      
     

c1 = Car(0,0,2,2)
c2 = Car(0,0,0,1)
m = Map(200,200)

g = Game(map=m, cars=[c1,c2])

generate_route(m,0,0,150,150)
iterations = distX + distY
for _ in range(iterations):
  g.step()
  g.show()
  #time.sleep(0.5)
  

  











