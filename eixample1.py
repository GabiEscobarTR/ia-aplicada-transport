"""
Versió1
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

  def move(self, map):
      newX = self.x + self.speedX*TIME_STEP
      newY = self.y + self.speedY*TIME_STEP
      
      if map.get(newX, newY) == 0:
        self.x = newX
        self.y = newY
        
      else:
          print("BOOM")
          raise
          

class Map():
    
    def __init__(self, sizeX, sizeY):
        self.grid = np.ones((sizeX, sizeY))
        
        #Creació de les carreterres en l'eix X
        for i in range(0, sizeX, 10): 
            self.grid[i,:] = 0
            #self.grid[i+1,:] = 0
            if all(self.grid[i,:]) == 0: 
                availableX = self.grid[i,:]
        
        #Creació de les carreterres en l'eix Y
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
          print("BOOM")
          raise 
          

class Node():
    #Node for A* path finding algorithm
    
    def __init__(self, parent=None, position=None):
        
        self.parent = parent
        self.position = position
    
        self.g = 0
        self.h = 0
        self.f = 0
        


def generate_route(map, oriX, oriY, destX, destY):
    
    origin = (oriX, oriY)
    destiny = (destX, destY)
    
    origin_node = Node(None, origin)
    origin_node.g = origin_node.h = origin_node.f = 0
    destiny_node = Node(None, destiny)
    destiny_node.g = destiny_node.h = destiny_node.f = 0
    
    open_list = []
    closed_list = []
    
    
    open_list.append(origin_node)
    
    if not map.get(oriX, oriY) == 0:
        print("Origin direction is not valid.")
        raise
    
    if not map.get(destX, destY) == 0:
        print("Destiny direction is not valid.")
        raise
  
    if len(open_list) == 0:
        route = [(oriX, oriY)]
    
    
    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        
        for index, item in enumerate(open_list):
            if item.f > current_node.f:
                current_node = item
                current_index = index
                
                




"""
// A* (star) Pathfinding
// Initialize both open and closed list
let the openList equal empty list of nodes
let the closedList equal empty list of nodes
// Add the start node
put the startNode on the openList (leave it's f at zero)
// Loop until you find the end
while the openList is not empty
    // Get the current node
    let the currentNode equal the node with the least f value
    remove the currentNode from the openList
    add the currentNode to the closedList
    // Found the goal
    if currentNode is the goal
        Congratz! You've found the end! Backtrack to get path
    // Generate children
    let the children of the currentNode equal the adjacent nodes
    
    for each child in the children
        // Child is on the closedList
        if child is in the closedList
            continue to beginning of for loop
        // Create the f, g, and h values
        child.g = currentNode.g + distance between child and current
        child.h = distance from child to end
        child.f = child.g + child.h
        // Child is already in openList
        if child.position is in the openList's nodes positions
            if the child.g is higher than the openList node's g
                continue to beginning of for loop
        // Add the child to the openList
        add the child to the openList
"""
     
 

  
  

c1 = Car(0,0,2,2)
c2 = Car(0,0,0,1)
m = Map(200,200)

g = Game(map=m, cars=[c1,c2])

iterations = 100
for _ in range(iterations):
  g.step()
  g.show()
  #time.sleep(0.5)
  









