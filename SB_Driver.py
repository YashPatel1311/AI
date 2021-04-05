import os
from SB_Agent import Agent
from SB_environment import Sokoban

#             char == ' ' or # floor
#             char == '#' or # wall
#             char == '@' or # worker on floor
#             char == '.' or # goal
#             char == '*' or # box on goal
#             char == '$' or # box
#             char == '+' ): # worker on goal

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

    # board=[
	# ['#','#','#','#',' ',' ',' '],           
    # ['#',' ',' ','#','#','#',' '],  
    # ['#',' ',' ',' ',' ','#',' '],    
    # ['#',' ',' ',' ',' ','#',' '],  
    # ['#','#','#',' ','#','#','#'],  
    # ['#',' ',' ',' ',' ',' ','#'],  
    # ['#',' ',' ','$','$',' ','#'],  
    # ['#',' ','$','$','$',' ','#'],  
    # ['#','#','#',' ',' ','#','#'],  
    # [' ',' ','#','#','#','#',' ']]
    
    # board=[
	# ['#','#','#','#','#','#'],           
    # ['#',' ',' ',' ',' ','#'],   
    # ['#',' ',' ',' ',' ','#'],
    # ['#',' ',' ',' ',' ','#'],
    # ['#',' ',' ',' ',' ','#'],
	# ['#','#','#','#','#','#']]           

    # boxPos=[(2,3),(3,4),(4,4),(6,4),(6,3),(6,5),(6,1)]  # write box position here
    # goalPos=[(2,1),(4,1),(3,5),(5,4),(6,6),(7,4),(6,3)]  # write goal position here    
    # workerPos=(2,2)

    # boxPos = [(2,2),(3,2)]
    # goalPos = [(1,3),(3,3)]
    # workerPos = (2,1)

    SBobj=Sokoban(board,boxPos,goalPos,workerPos)        

    agnt=Agent(SBobj)

    result,counter=agnt.BFS()

    try:
        os.remove("path.txt")
    except:
        pass
    agnt.printPath(result,"path.txt")
    print(counter)


