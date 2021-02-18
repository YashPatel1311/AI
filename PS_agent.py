from queue import PriorityQueue
from PS_environment  import PegSolitare
import numpy as np

class agent:

    def __init__(self):
        
        self.puzzle=PegSolitare()
        self.goal=[False]*34
        self.goal[0]=True
        self.goal[17]=True
       
        self.frontier=PriorityQueue()
        # self.explored={}
    
    def printPath(self,node):
        if(node != None):
            self.printPath(node.parent)
            print(node,"\n")

    def isGoal(self,node):
        
        return node.config[1:] == self.goal[1:]
        


    def BFS(self):
        frontier = self.frontier
        # explored = self.explored

        frontier.put(self.puzzle.root)
        counter=0
        while not frontier.empty():
            node = frontier.get()
            
            if counter%10000==0:
                print(counter)
                print(node)
            counter+=1
            
            
            # print(node)
            # print(node.cost)
            conf = node.config
            
            # confStr = str(list(map(int,conf))).replace(",","").replace("[","").replace("]","").replace(" ","")
            # explored[confStr]=node
            
            if self.isGoal(node):
                return node

            neighbours=self.puzzle.moves(node)

            for neighbour in neighbours:
                # print(neighbour)
                # configuration = neighbour.config
                # configurationStr = str(list(map(int,configuration))).replace(",","").replace("[","").replace("]","").replace(" ","")
                # if configurationStr not in explored:
                #     frontier.put(neighbour)
                # else:
                #     del(neighbour)
                frontier.put(neighbour)

        return None