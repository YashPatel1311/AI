from PS_agent import agent
import numpy as np

def driver():
    
    agnt=agent()

    node=agnt.BFS()

    if not node:
        print("\n no sol")

    
    agnt.printPath(node)
    
if __name__ == "__main__":
    driver()