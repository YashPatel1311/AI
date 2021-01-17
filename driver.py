from environment import puzzle,Node
from agent import agent
import numpy as np

def driver():
    initial= np.array([[1,2,3],[4,-1,5],[6,7,8]])
    final= np.array([[1,2,3],[-1,4,6],[7,5,8]])
    puzz=puzzle(initial)
    agnt=agent(puzz,final)

    node=agnt.BFS()

    if not node:
        print("\n no sol")

    
    agnt.printPath(node)
    
if __name__ == "__main__":
    driver()