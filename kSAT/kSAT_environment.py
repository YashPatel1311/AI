import random as rd
import numpy as np
import sys
from tabulate import tabulate
import copy

#class puzzle would initialize the environment

def generator(k,n,m):
    '''
    k=no of var in each clause \n
    n=no of var \n
    m=no of clauses \n\n
    Output: List containing randomly generated clauses 
    '''
    # self.k=k
    # self.n=n
    # self.m=m
    sym=[]
    for j in range(n):
        sym.append(chr(65+j))
        
    c=True
    while c:
        output=[]
        # output=[['a', 'f', 'C'], ['e', 'A', 'c'], ['F', 'C', 'E'], ['a', 'D', 'c'], ['f', 'D', 'c']]
        for i in range(m):
            clause=rd.sample(sym,k)
            loop=[]
            for j in range(k):
            
                negation = rd.sample([True,False],1)
                if negation[0]:
                    loop.append(clause[j].lower())
                else:
                    loop.append(clause[j])
            output.append(loop)
        nl= sum(output, [])
        for i in range(len(nl)):
            nl[i]=nl[i].upper()
        nl=list(set(nl))
        flag=False
        for i in sym:
            if(i in nl):
                pass
            else:
                flag=True
                break
        if flag==False:
            c=False
        # Output should contain all variables atleast one time
    return output

class Tree:

    def __init__(self,k,n,m):
        initial={}
        self.k=k
        self.n=n
        self.m=m

        self.problem=generator(k,n,m)

        print(self.problem)

        for i in range(n):
            initial[chr(65+i)]=None


        self.root=Node(None,initial,self.problem,0)

    def moves(self,node):
        result=[]

        if node.level>self.n-1:
            return []

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
        self.cost=None

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