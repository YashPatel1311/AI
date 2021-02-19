import numpy as np
import random as rd

class Problem:

    def __init__(self,k,n,m,samples):
        '''
        k=no of var in each clause \n
        n=no of var \n
        m=no of clauses \n\n

        Output: List of list containing randomly generated clauses 
        '''
        self.k=k
        self.n=n
        self.m=m
        self.probSet=[None]*samples
        print(self.probSet)


        sym=[]
        for j in range(n):
            sym.append(chr(65+j))

        for x in range(samples):

# k=int(input("no of var in each clause")) # no of var in each clause
# n=int(input("no of var")) # no of var
# m=int(input("no of clauses")) # no of clauses

            l=[]
            output=[]

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

            self.probSet[x]=output

        print(self.probSet)


    # def __str__(self,i):


    #     return 
                

if __name__=="__main__":
    newProb=Problem(3,6,5,10)

