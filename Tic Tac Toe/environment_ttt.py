import numpy as np
import sys
from tabulate import tabulate
import copy

#class puzzle would initialize the environment
class Board:

    def __init__(self):
        initial=[]
        initial.append([])
        initial.append([])
        initial.append([])
    
        for i in range(3):
            for j in range(3):
                initial[i].append('')
        self.root=Node(None,initial,0,True)      


class Node:
    def __init__(self,parent,config,level,isMax):
        self.parent=parent
        self.config=config
        self.level=level
        self.isMax=isMax             # True -> X , False -> O

    def moves(self,isMax):
        result=[]
        node=self
        if isMax:
            marker='O'
        else:
            marker='X'

        for i in range(3):
            for j in range(3):
                if node.config[i][j]=='':
                    newConfig=copy.deepcopy(node.config)
                    newConfig[i][j]=marker

                    result.append(Node(node,newConfig,node.level+1,isMax))

        return result        


    def evaluate(self):
        config=self.config
        for i in range(3):
            result=""
            for j in range(3):
                result+=config[i][j]
            if result=="XXX":
                return 1

            elif result=="OOO":
                return -1

        for x in range(3):
            result=""
            for y in range(3):
                result+=config[y][x]
            if result=="XXX":
                return 1
            elif result=="OOO":
                return -1

        result=""
        for z in range(3):
            result+=config[z][z]
            if result=="XXX":
                return 1
            elif result=="OOO":
                return -1

        result=""
        result=config[0][2]+config[1][1]+config[2][0]
        if result=="XXX":
            return 1
        elif result=="OOO":
            return -1


        if self.level==9:
            return 0
        else: 
            return None



    def __str__(self):

        for i in range(3):
            for j in range(3):
                if j<2:
                    print(self.config[i][j],end='|')
                else:
                    print(self.config[i][j])

        return ""

