from kSAT_Gen import Generator

import numpy as np
import sys
from tabulate import tabulate
import copy

#class puzzle would initialize the environment
class Tree:

    def __init__(self,generator):
        initial={}
        self.problem=generator.problem

        for i in range(generator.n):
            initial[chr(65+i)]=None


        self.root=Node(None,initial,generator.problem,0)

    def moves(self,node):
        result=[]

        if 65+node.level>91:
            return None

        currVar=chr(65+node.level)

        values=[True,False]

        for val in values:
            newConfig=copy.deepcopy(node.config)

            newConfig[currVar]=val
            
            newProblem=node.assign(currVar,val)
            newNode=Node(node,newConfig,newProblem,node.level+1)
            # newNode.problem=node.assign(currVar,val)

            result.append(newNode)


        return result


        
class Node:
    # config is a dict  which stores the bool values of variables 
    def __init__(self,parent,config,problem,level):
        self.parent=parent
        self.problem=problem
        self.config=config
        self.level=level
        self.cost=self.heuristic()

    def __lt__(self, other):
        return self.cost<other.cost


    def assign(self,currVar,val):
        problem=copy.deepcopy(self.problem)
        marked=[]
        for i in range(len(problem)):
            for j in range(len(problem[i])):

                x=problem[i][j]
                flag=True
                if x.upper()==currVar and val==True:

                    if x.isupper():         # val -> True and variable in exp is positive
                        #  clause would be positive -> remove clause
                        marked.append(i)
                        # flag=False
                    else:        
                        pass

                elif x.upper()==currVar and val==False:

                    if x.isupper():     # val -> False and variable in exp is positive
                        
                        pass
                    else:
                        #  clause would be positive -> remove clause
                        marked.append(i)

        for x in reversed(marked):
            del problem[x]
        
        return problem


    def heuristic(self):
        try:
            return len(self.problem)
        except:
            return 0