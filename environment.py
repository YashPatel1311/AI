import numpy as np
import sys
from tabulate import tabulate
import copy

#class puzzle would initialize the environment
class puzzle:

    def __init__(self,initial):
        # if (np.size(initial,0) == np.size(final,0)) and (np.size(initial,1) == np.size(final,1)):
        if (np.size(initial,0) == np.size(initial,1)):
            self.initial=initial
            # self.final=final

            x,y=-1,-1
            for i in range(np.size(initial,0)):
                for j in range(np.size(initial,1)):
                    if initial[i,j]==-1:
                        x,y=i,j
                        break

            self.root=Node(None,self.initial,0,x,y)
            self.size=(len(initial),len(initial[0]))

    def moves(self,node):
        result=[]
        row,col=(self.size)

        # maximum possible moves are 4: Up, Down, Left, Right
        move=[(-1,0),(1,0),(0,-1),(0,1)]

        for r,c in move:
            x,y=node.x,node.y
            newR,newC=x+r,y+c

            if 0<=newR<row and 0<=newC<col:
            
                newConf=copy.deepcopy(node.config)
            
                temp= newConf[newR,newC]
                newConf[x,y]=temp
                newConf[newR,newC]=-1
            
                newNode=Node(node,newConf,node.level+1,newR,newC)
                result.append(newNode)

            else:
                continue
                
        return result


def addTup(tup1,tup2):
    res = tuple(map(sum, zip(tup1, tup2)))
    return res


        
class Node:
    # config is a numpy matrix which stores the state of game 
    def __init__(self,parent,config,level,x,y):
        self.parent=parent
        self.config=config
        self.level=level
        self.x=x
        self.y=y
        self.cost=sys.maxsize

    def __str__(self):
        config=self.config
        table = tabulate(self.config, tablefmt="fancy_grid")
        return f"{table}"

    def __lt__(self, other):
        return self.level<other.level

        


# if __name__ == "__main__":

#     initial= np.array([[1,2,3],[4,-1,5],[6,7,8]])
#     final= np.array([[1,2,3],[-1,4,6],[7,5,8]])

#     newPuzzle=puzzle(initial)
#     print(newPuzzle.root)
#     child=newPuzzle.moves(newPuzzle.root)


#     for x in child:
#         print(x)
