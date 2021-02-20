from kSAT_Gen import Generator
from kSAT_environment import Tree
import sys


class agent:

    def __init__(self,problem):
        '''
        k=no of var in each clause \n
        n=no of var \n
        m=no of clauses \n\n

        Output: List containing randomly generated clauses 
        '''
        self.tree=Tree(problem)
        # self.k=k
        # self.n=n
        # self.m=m

    def BruteForce(self):
        problem=self.tree.problem
        n=problem.n
        for i in range(2**n-1):
            result=problem.evaluate(i)
            if result != None:
                return result

        return None


    def HillClimb(self):

        currNode=self.tree.root
        childs=self.tree.moves(currNode)
        counter=0

        while True:

            counter+=1

            if childs!= None:

                if currNode.cost>childs[0].cost or currNode.cost>childs[1].cost:

                    if childs[0].cost<=childs[1].cost:
                        currNode=childs[0]

                    elif childs[1].cost<childs[0].cost:
                        currNode=childs[1]

                    childs=self.tree.moves(currNode)

                else:
                    break

            else:
                break

        return currNode,counter


    def BeamSearch(self,width):



        return Node,counter





if __name__=="__main__":
    newProb=Generator(3,10,40)
    print(newProb.problem)
    agt=agent(newProb)

    result,iterations=agt.HillClimb()
    # print(result[-6:])
    print("\nRemaining clauses:", result.cost)
    print("\nNodes explored:", iterations)
    print(result.config)


