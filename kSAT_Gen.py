import numpy as np
import random as rd

 

#+ve CAPITAL -ve small


class Generator:

    def __init__(self,k,n,m):
        '''
        k=no of var in each clause \n
        n=no of var \n
        m=no of clauses \n\n

        Output: List containing randomly generated clauses 
        '''
        self.k=k
        self.n=n
        self.m=m

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
        self.problem=output

           

            

    def evaluate(self,truthVal):
        '''
        Integer input representing truth values of variables in binary \n
        Problem instance \n

        Goal : to find the whether truth value of problem is True or not. \n
        '''
        # truthVal = bin(truthVal)
        # truthVal=truthVal[2:]
        truthVal = format(truthVal,"026b")
        n = len(truthVal)-1
        # exp = ""
        tmp1 = True
        problem=self.problem

        # assuming problem is list of list containing variables as dtype=str
        for i in problem:
            # exp += "("
            tmp2 = False
            for j in i:
                
                if j.isupper():
                    # exp += str(truthVal[ord(j)-ord("A")])
                    tmp2 |= bool(int(truthVal[n-(ord(j)-ord("A"))]))

                elif j.islower():
                    # exp += str(truthVal[ord(j)-ord("a")])
                    tmp2 |= (not bool(int(truthVal[n-(ord(j)-ord("a"))])))
                # exp += "∨"

                if tmp2:
                    break
            tmp1 &= tmp2
        #     exp = exp[:-1]
        #     exp += ") ∧"

        # exp = exp[:-2]
        if tmp1:
            return truthVal

        return None
                
if __name__=="__main__":
    newProb=Generator(3,6,5)
    

    print(newProb.problem)







































































    

