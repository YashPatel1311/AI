from kSAT_environment import Tree
import sys
from queue import PriorityQueue


class agent:

    def __init__(self,k,n,m):
        '''
        k=no of var in each clause \n
        n=no of var \n
        m=no of clauses \n\n

        Output: List containing randomly generated clauses 
        '''
        self.tree=Tree(k,n,m)
        # self.k=k
        # self.n=n
        # self.m=m

    def BruteForce(self):
        problem=self.tree.problem
        n=problem.n
        for i in range(2**n-1):
            result=problem.evaluate(problem,i)
            if result != None:
                return result

        return None


    def HillClimb(self):

        currNode=self.tree.root
        childs=self.tree.moves(currNode)
        counter=0

        while True:

            counter+=1

            if len(childs)!=0:

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
        frontier = PriorityQueue()
        

        # explored = self.explored
        # self.Tree.root.cost = self.cal_cost(self.Tree.root,optimizer)
        frontier.put(self.tree.root)


        counter=0

        while not frontier.empty():
            counter+=1
            node = frontier.get()
            # conf = node.config
            # confStr = str(list(map(int,conf))).replace(",","").replace("[","").replace("]","").replace(" ","")
            # explored[confStr]=node
            
            if node.cost==0:
                return node,counter

                
            temp = PriorityQueue()
            neighbours = self.tree.moves(node)
            
            for neighbour in neighbours:
                temp.put(neighbour)

            for i in range(frontier.qsize()):
                
                temp.put(frontier.get())

            for i in range(min(width,temp.qsize())):

                frontier.put(temp.get())

            # neighbours=self.Trees.moves(node)

            # for neighbour in neighbours:
            #     neighbour.cost = self.width
            # #   configuration = neighbour.config
            # #   configurationStr = str(list(map(int,configuration))).replace(",","").replace("[","").replace("]","").replace(" ","")
            # if configurationStr not in explored:
            #     frontier.put(neighbour)
            # else:
            #     del(neighbour)

        return node , counter


    # def variableNeighbourhood():

        



if __name__=="__main__":
    agt=agent(3,15,50)

    result,iterations=agt.BeamSearch(4)
    # print(result[-6:])
    print("\nRemaining clauses:", result.cost)
    print("\nNodes explored:", iterations)
    print(result.config)

    result,iterations=agt.HillClimb()
    # print(result[-6:])
    print("\nRemaining clauses:", result.cost)
    print("\nNodes explored:", iterations)
    print(result.config)





