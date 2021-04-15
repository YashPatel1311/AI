
import sys
from tabulate import tabulate
import copy
from os import system


class Sokoban:

    # workerPos -> (Tuple) initial position of Worker
    # boxPos -> (List of tuples) initial position of all boxes
    # goal -> (List of tuples) position of all goals

    def __init__(self,board,boxPos,goal,workerPos):

        self.board=board
        self.goal=goal
        self.root=Node(None,boxPos,workerPos[0],workerPos[1])

    def moves(self,node):
        u=(-1,0)
        d=(1,0)
        l=(0,-1)
        r=(0,1)
        # moves=[(-1,0),(0,-1),(1,0),(0,1)]
        moves=[
            r,u,d,l
]
        result=[]

        for mv in moves:
            newWPX=node.workerPosX +mv[0]
            newWPY=node.workerPosY +mv[1]

            if self.board[newWPX][newWPY]=="#":
                continue

            elif self.board[newWPX][newWPY]==" ":
                
                boxIdx=-1

                #Finding which box will move
                for i in range(len(node.boxPos)):
                    if node.boxPos[i]==(newWPX,newWPY):
                        boxIdx=i

                if boxIdx==-1:
                    result.append(Node(node,node.boxPos,newWPX,newWPY))
                    continue


                newBPX=newWPX+mv[0]
                newBPY=newWPY+mv[1]  

                if self.board[newBPX][newBPY]==" " and (newBPX,newBPY) not in node.boxPos:
                    newBoxPos=copy.deepcopy(node.boxPos)
                    newBoxPos[boxIdx]=(newBPX,newBPY)
                    result.append(Node(node,newBoxPos,newWPX,newWPY))

                else:
                    continue

        return result

# def is_valid_value(self,char):
#         if (
#             char == ' ' or # floor
#             char == '#' or # wall
#             char == '@' or # worker on floor
#             char == '.' or # goal
#             char == '*' or # box on goal
#             char == '$' or # box
#             char == '+' ): # worker on goal
#             return True
#         else:
#             return False

# Level 1
                # # # # 
                #     # # # 
                #         # 
                #   $     # 
                # # #   # # #
                #   $   $   #
                # . . @ . . #
                #     $     #
                # # #     # #
                    # # # # 


class Node:

    def __init__(self,parent,boxPos,workerPosX,workerPosY):
        self.parent=parent
        self.boxPos=boxPos
        self.workerPosX=workerPosX
        self.workerPosY=workerPosY
        try:
            self.level=parent.level+1
        except:
            self.level=0
        self.cost=0

    # def __eq__(self,other):
    #     if (self.workerPosX,self.workerPosY)==(other.workerPosX,other.workerPosY) and set(self.boxPos)==set(self.boxPos):
    #         return True
    #     else:
    #         return False

    def __lt__(self,other):
        return self.cost<other.cost

    # workerPos -> (Tuple) initial position of Worker
    # boxPos -> (List of tuples) initial position of all boxes
    # goal -> (List of tuples) position of all goals
    def Print(self,SBobj,filename):
        cls = lambda: system('cls')
        board=copy.deepcopy(SBobj.board)
        row=len(SBobj.board)
        col=len(SBobj.board[0])

        for i in range(row):
            for j in range(col):
                if (i,j) in self.boxPos :
                    board[i][j]="$"
                    
                if (i,j) in SBobj.goal :
                    board[i][j]="."
                    if (i,j) in self.boxPos :
                        board[i][j]="*"

        board[self.workerPosX][self.workerPosY]="@"
        if (self.workerPosX,self.workerPosY) in SBobj.goal:
            board[self.workerPosX][self.workerPosY]="+"

        config = board
        table = tabulate(config, tablefmt="fancy_grid")
        fp=open(filename,'a+',encoding="utf-8")
        fp.write(table)
        fp.write("\n")
        fp.close()
  

if __name__=="__main__":

    board=[
	['#','#','#','#',' ',' ',' '],           
    ['#',' ',' ','#','#','#',' '],  
    ['#',' ',' ',' ',' ','#',' '],    
    ['#',' ',' ',' ',' ','#',' '],  
    ['#','#','#',' ','#','#','#'],  
    ['#',' ',' ',' ',' ',' ','#'],  
    ['#',' ',' ',' ',' ',' ','#'],  
    ['#',' ',' ',' ',' ',' ','#'],  
    ['#','#','#',' ',' ','#','#'],  
    [' ',' ','#','#','#','#',' ']]


    boxPos=[(3,2) , (5,2) , (5,4) , (7,3),(8,3)]  # write box position here
    goalPos=[(6,1) , (6,2) , (6,4) , (6,5)]  # write goal position here
    
    workerPos=(6,3)

    SBobj=Sokoban(board,boxPos,goalPos,workerPos)        
    
    children=SBobj.moves(SBobj.root)

    for c in children:
        c.Print(SBobj)


# mat=[
# 	   ['0','1','2','3','4','5','6']           
# 	 0 ['#','#','#','#',' ',' ',' '],           
#    1 ['#',' ',' ','#','#','#',' '],  
#    2 ['#',' ',' ',' ',' ','#',' '],    
#    3 ['#',' ','$',' ',' ','#',' '],  
#    4 ['#','#','#',' ','#','#','#'],  
#    5 ['#',' ','$',' ','$',' ','#'],  
#    6 ['#','.','.','@','.','.','#'],  
#    7 ['#',' ',' ','$',' ',' ','#'],  
#    8 ['#','#','#',' ',' ','#','#'],  
#    9 [' ',' ','#','#','#','#',' '],
# ]
    

# temp=[
#     ['0','1','2','3','4','5','6']
# 	0 ['#','#','#','#',' ',' ',' '],           
#   1 ['#',' ','$',' ',' ',' ',' '], 
#   2 ['#',' ',' ',' ',' ',' ',' '],   
#   3 ['#',' ',' ','$','$',' ',' '],  
#   4 ['#',' ',' ','$','$',' ','#'],  
#   5 ['#',' ',' ',' ',' ',' ','#'],  
#   6 ['#',' ',' ','$','$',' ','#'],  
#   7 ['#',' ','$','$',' ',' ','#'],  
#   8 ['#','#','#',' ',' ','#','#'],  
#   9 [' ',' ','#','#','#','#',' ']]




'''
i-1 & j-1 , i+1 & j-1 , i+1 & j+1 , i-1 & j+1

'''