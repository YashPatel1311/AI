import sys
from agent_ttt import Agent

def driver():

    agnt=Agent()
    result=agnt.miniMax(agnt.board.root)
    if result==1:
        print("Player 1 won!")
    if result==-1:
        print("Player 2 won!")
    else:
        print("Draw")

    print("# of nodes evaluated: ",agnt.counter)

    agnt.counter=0

    result=agnt.abPruning(agnt.board.root,-sys.maxsize,sys.maxsize)
    if result==1:
        print("Player 1 won!")
    if result==-1:
        print("Player 2 won!")
    else:
        print("Draw")

    print("# of nodes evaluated: ",agnt.counter)


if __name__=="__main__":
    driver()