import os
from SB_Agent import Agent
from SB_environment import Sokoban
import copy

def get_level(level):

    start = "Level "+str(level)
    end = "Level "+str(level + 1)
    file = open("levels.txt","r")
    flag_start = False
    flag_end = False
    start_pos = end_pos = itr = 0

    allLevels = file.readlines()

    for line in allLevels:
        itr += 1
        if not flag_start and start in line:
            start_pos = itr
            flag_start = True
            continue
        
        if flag_start and end in line:
            end_pos = itr
            flag_end = True
            break
    
    if start_pos < end_pos:
        mat = [""]*(end_pos-start_pos)
        mat = allLevels[start_pos:end_pos-2]
        maxSize = 0
        ll = [""]*len(mat)

        for i in range(len(mat)):
            tmp = mat[i]
            for j in range(len(tmp)-1):
                ll[i] += tmp[j]
            for j in range(len(ll)):
                if maxSize < len(ll[j]):
                    maxSize = len(ll[j])
        # print("maxSize: ",maxSize)
        for i in range(len(ll)):
            if len(ll[i]) < maxSize:
                temp = " "*(maxSize-len(ll[i]))
                ll[i] += temp
        
        lll = []

        for i in range(len(ll)):
            lll.append([""]*maxSize)
            for j in range(len(ll[i])):
                lll[i][j] = copy.deepcopy(ll[i][j])
        
        # print(lll)

        return lll
    
    else:
        print("Level requested doesn't exists!!!")



    

if __name__=="__main__":
    # board=[
	# [' ',' ','#','#','#','#','#',' '],           
    # ['#','#','#',' ',' ',' ','#',' '],  
    # ['#','.','@','$',' ',' ','#',' '],    
    # ['#','#','#',' ','$','.','#',' '],  
    # ['#','.','#','#','$',' ','#',' '],  
    # ['#',' ','#',' ','.',' ','#','#'],  
    # ['#','$',' ','*','$','$','.','#'],
    # ['#',' ',' ',' ','.',' ',' ','#'],  
    # ['#','#','#','#','#','#','#','#']]

    board=get_level(3)

    # print(board)

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

    print("Nodes explored: ",counter)
    print("Path length: ",result.level)

    agnt.Interactive(path)


    



            