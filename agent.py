from queue import PriorityQueue
from environment import puzzle,Node
import numpy as np

class agent:

    def __init__(self,puzzle,goal):
        if (np.size(puzzle.initial,0) == np.size(goal,0)) and (np.size(puzzle.initial,1) == np.size(goal,1)):
            self.puzzle=puzzle
            self.goal=goal
            self.frontier=PriorityQueue()
            self.explored={}
    
    def printPath(self,node):
        if(node != None):
            self.printPath(node.parent)
            print(node,"\n")

    def isGoal(self,node):
        flag = False
        config=node.config
        goal=self.goal
        comp = config == goal
        if(comp.all() == True):
            flag = True
        return flag
        


    def BFS(self):
        frontier = self.frontier
        explored = self.explored

        frontier.put(self.puzzle.root)

        while not frontier.empty():
            node = frontier.get()
            conf = node.config
            explored[np.array2string(conf)]=node
            
            if self.isGoal(node):
                return node

            neighbours=self.puzzle.moves(node)

            for neighbour in neighbours:
                configuration = neighbour.config
                if np.array2string(configuration) not in explored:
                    frontier.put(neighbour)
                else:
                    del(neighbour)

        return None