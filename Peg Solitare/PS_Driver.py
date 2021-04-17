from PS_agent import agent
import numpy as np

def driver():
    
    agnt=agent()
    # gnode=Node(None,agnt.goal,0)
    # print(gnode)

    node,iterations=agnt.BFS()

    if not node:
        print("\n no sol")

    print("Total iterations: ",iterations)
    agnt.printPath(node)

if __name__=="__main__":
    driver()