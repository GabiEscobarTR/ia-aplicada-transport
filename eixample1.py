"""
Versio1
Utilitzar # per afegir comentaris (no afecten al codi)
@author: GabiEscobar
"""

import random
from math import *
import numpy as np
import matplotlib.pyplot as plt
import time



#Variables globals
TIME_STEP = 1



class Car():
  def __init__(self, x, y, speedX, speedY): 
      self.x = x
      self.y = y
      self.speedX = speedX
      self.speedY = speedY
      self.route = []
      self.crash = False
      
  def generate_route(self, map, destX, destY):
      """
      Generates a route from destX to destY.
      """
      
      route = []
      oriX = self.x
      oriY = self.y
      
      if not map.grid[oriX, oriY] == 0:
          raise Exception("Origin direction is not valid.")
      if not map.grid[destX, destY] == 0:
          raise Exception("Destiny direction is not valid.")
    
      x = oriX
      y = oriY
      
      while x != destX:
          if x < destX and map.grid[x+1,y] == 0:
              x += 1
              route.append((x,y))
          elif x > destX and map.grid[x-1,y] == 0:
              x -= 1
              route.append((x,y))
          else:
              break
          
      while y != destY:
          if y < destY and map.grid[x,y+1] == 0:
              y += 1
              route.append((x,y))
          elif x > destY and map.grid[y-1] == 0:
              y -= 1
              route.append((x,y))
          else:
              break
         
      self.route = route
      print(route)
  
    

  def move(self, map):
      
      if len(self.route) > 0:
          
          newX, newY = self.route[0]
          if map.get(newX, newY) == 0:
            self.x = newX
            self.y = newY
            del self.route[0]
            return True
            
          else:
              print("Un resplandor y hace: BOOM")
              self.route = []
              self.crash = True
              return False
              
      else:
          print("Route is empty.")
          return False
    

class Map():
    def __init__(self, sizeX, sizeY):
        self.grid = np.ones((sizeX, sizeY))
        
        #Creació de les carreterres en l'eix X
        for i in range(0, sizeX, 10): 
            self.grid[i,:] = 0
        
        #Creació de les carreterres en l'eix Y
        for j in range(0, sizeY, 10): 
            self.grid[:,j] = 0
                
    def show(self):
      plt.imshow(self.grid)
      
    def get(self, x, y):
      return self.grid[x,y]




class Main():
    def __init__(self, map, cars, dests):
        self.map = map
        self.cars = cars
        for i, car in enumerate(cars):
            car.generate_route(map, dests[i][0], dests[i][1])
    
    def step(self):
        for car in self.cars:
            prevX, prevY = car.x, car.y
            #if car.move(self.map):
            #    self.map.grid[prevX, prevY] = 0
            #    self.map.grid[car.x, car.y] = 1
            car.move(self.map)
            
        self.collisions() 

    def show(self):
        self.map.show()
        for car in self.cars:
            if not car.crash:
                plt.scatter(car.x, car.y, c='green')
            else:
                plt.scatter(car.x, car.y, c='red', marker='x')
        plt.show()
     
    def collisions(self):
        for car in self.cars:
            if car.crash:
                raise Exception(f"Un resplandor y hace: BOOM. ({car.x}, {car.y})")
                 
         

 

  
  
m = Map(200,200)

c1 = Car(80,40,2,2)
c2 = Car(0,0,0,1)

d1 = (160,110)
d2 = (20,50)

g = Main(map=m, cars=[c1,c2], dests=[d1,d2])


iterations = 1000
for _ in range(iterations):
  g.step()
  g.show()
  #time.sleep(0.5)
  



  











