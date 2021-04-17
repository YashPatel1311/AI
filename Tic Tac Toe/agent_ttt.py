from environment_ttt import Board,Node
import sys

class Agent:
    def __init__(self):
        self.board=Board()
        self.counter=0


    def miniMax(self,node):
        global counter
        self.counter+=1

        # if counter%10000==0:
        #     print(counter)

        value=node.evaluate()

        if value!=None:
            return value


        # if node.level==9:
        #     print(node)
        #     return node.evaluate()

        else:
            if node.isMax:
                maxval=-sys.maxsize
                childs=node.moves(not node.isMax)
                for x in childs:
                    # evaluate=node.evaluate()

                    val=self.miniMax(x)
                    maxval=max(val,maxval)

                return maxval


            else:
                minval=sys.maxsize
                childs=node.moves(not node.isMax)
                for x in childs:
                    val=self.miniMax(x)
                    minval=min(val,minval)

                return minval


    def abPruning(self,node,alpha,beta):

        self.counter+=1

        # if counter%10000==0:
        #     print(counter)

        value=node.evaluate()

        if value!=None:
            return value


        # if node.level==9:
        #     print(node)
        #     return node.evaluate()

        else:
            if node.isMax:
                maxval=-sys.maxsize
                childs=node.moves(not node.isMax)
                for x in childs:
                    val=self.abPruning(x,alpha,beta)
                    maxval=max(val,maxval)
                    alpha=max(alpha,maxval)
                    if beta<=alpha:
                        break


                return maxval


            else:
                minval=sys.maxsize
                childs=node.moves(not node.isMax)
                for x in childs:
                    val=self.abPruning(x,alpha,beta)
                    minval=min(val,minval)
                    beta=min(beta,minval)
                    if beta<=alpha:
                        break

                return minval 