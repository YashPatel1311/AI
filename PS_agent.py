

from queue import PriorityQueue
from PS_environment  import PegSolitare
import numpy as np

class agent:

    def __init__(self):
        
        self.puzzle=PegSolitare()
        # self.goal = [False,False,False,True,False,False,False,True,True,True,True,True,False,False,True,True,True,True,True,False,False,True,True,True,False,False,False,False,True,False,False,False,False,False]
        self.goal=[False]*34
        self.goal[17]=True
       

        self.frontier=PriorityQueue()
        self.explored={}
    
    def cal_cost(self,config):
      # config = node.config
      dist = np.array([1,2,4,8])
      coeff = np.zeros((4))
      d = {0:[17],1:[9,10,11,16,18,23,24,25],2:[4,5,6,8,12,15,19,22,26,28,29,30],3:[1,2,3,7,13,14,20,21,27,31,32,33]}
      base = 2
      for i in d:
          toCheck = d[i]
          count = 0
          for j in toCheck:
              if config[j]:
                  count += 1
          coeff[i] = count
      dist = dist.reshape((1,4))
      coeff = coeff.reshape((4,1))
    
      return np.dot(dist,coeff).squeeze()

    def printPath(self,node):
        if(node != None):
            self.printPath(node.parent)
            print(node,"\n")

    def isGoal(self,node):
        
        return node.config[1:] == self.goal[1:]
        


    def BFS(self):
        frontier = self.frontier
        explored = self.explored
        # self.puzzle.root.cost = self.cal_cost(self.puzzle.root.config)
        frontier.put(self.puzzle.root)
        counter=0
        while not frontier.empty():
            if counter%10000==0:
                print(counter)
            counter+=1
            
            node = frontier.get()
            conf = node.config
            if counter%10000==0:
              print(node)
            confStr = str(list(map(int,conf))).replace(",","").replace("[","").replace("]","").replace(" ","")
            explored[confStr]=node
            
            if self.isGoal(node):
                return node,counter

            neighbours=self.puzzle.moves(node)

            for neighbour in neighbours:
            #   neighbour.cost = self.cal_cost(neighbour.config)
              # print(neighbour)
              configuration = neighbour.config
              configurationStr = str(list(map(int,configuration))).replace(",","").replace("[","").replace("]","").replace(" ","")
              if configurationStr not in explored:
                  frontier.put(neighbour)
              else:
                  del(neighbour)

        return None

    def DFS(self):
      # self.puzzle.root.cost = self.cal_cost(self.puzzle.root.config)
      frontier = [self.puzzle.root]
      # frontier = self.frontier
      # frontier.put(self.puzzle.root)
      counter=0
      while len(frontier) != 0:
      # while not frontier.empty():
          node = frontier.pop(-1)
          # node = frontier.get()
          # if counter%10000==0:
          #     print(counter)
          #     print(node)
          counter+=1
          if self.isGoal(node):
              return node,counter
          neighbours=self.puzzle.moves(node)
          for neighbour in neighbours:
            # neighbour.cost = self.cal_cost(neighbour.config)
            # frontier.put(neighbour)
            frontier.append(neighbour)
          # frontier.extend(neighbours)
      return None

