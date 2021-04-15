import os
from SB_Agent import Agent
from SB_environment import Sokoban

    

if __name__=="__main__":
    board=[
	[' ',' ','#','#','#','#','#',' '],           
    ['#','#','#',' ',' ',' ','#',' '],  
    ['#','.','@','$',' ',' ','#',' '],    
    ['#','#','#',' ','$','.','#',' '],  
    ['#','.','#','#','$',' ','#',' '],  
    ['#',' ','#',' ','.',' ','#','#'],  
    ['#','$',' ','*','$','$','.','#'],
    ['#',' ',' ',' ','.',' ',' ','#'],  
    ['#','#','#','#','#','#','#','#']]

    workerPosX=None
    workerPosY=None
    boxPos =[]
    goalPos= []
    
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == '@':
                workerPosX=x
                workerPosY=y
                board[x][y]=' '
            if board[x][y] == '$':
                boxPos.append((x,y))
                board[x][y]=' '
            if board[x][y] =='.':
                goalPos.append((x,y))
                board[x][y]=' '
            if board[x][y] == '+':
                workerPosX=x
                workerPosY=y
                goalPos.append((x,y))
                board[x][y]=' '
            if board[x][y] == '*':
                boxPos.append((x,y))
                goalPos.append((x,y))
                board[x][y]=' '

    workerPos=(workerPosX,workerPosY)

    SBobj=Sokoban(board,boxPos,goalPos,workerPos)        

    agnt=Agent(SBobj)

    result,counter=agnt.BFS()

    try:
        os.remove("path.txt")
    except:
        pass
    path=agnt.printPath(result,"path.txt")

    agnt.main(path)

    print("Nodes explored: ",counter)
    print("Path length: ",result.level)
    



            