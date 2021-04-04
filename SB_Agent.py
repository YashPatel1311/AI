from SB_environment import Sokoban,Node

from queue import PriorityQueue


class Agent:

    def __init__(self, sokoban):
        self.sokoban = sokoban
        self.frontier = PriorityQueue()
        self.explored = {}

    # def solve(self):

    def PBCheck(self, boxR,boxC, boxPos, parent,depth):
        board = self.sokoban.board
        goalPos = self.sokoban.goal

        if depth>len(boxPos):
            return True

        hBlocked=None
        vBlocked=None

        # Pakke Wale Status       
        # Horizontal check
        if (board[boxR][boxC-1]==" " and (boxR,boxC-1) not in boxPos) and (board[boxR][boxC+1]==" " and (boxR,boxC+1) not in boxPos):
            return False
        # vertical check
        elif (board[boxR-1][boxC]==" " and (boxR-1,boxC) not in boxPos) and (board[boxR+1][boxC]==" " and (boxR+1,boxC) not in boxPos):
            return False
        
        # checking for wall
        # wall in horizontal dir
        if board[boxR][boxC-1]=="#" or board[boxR][boxC+1]=="#":
            hBlocked=True
        # wall in vertical dir
        if board[boxR-1][boxC]=="#" or board[boxR+1][boxC]=="#":
            vBlocked=True


        # checking for boxes
        # Left or Right position containing box
        if not hBlocked and ((boxR,boxC-1) in boxPos or (boxR,boxC+1) in boxPos):
            
            # Checking if Left box if free or not.
            lbox=rbox=None
            if (boxR,boxC-1) in boxPos:
                if (boxR,boxC-1)==parent:
                    lbox=True
                else:
                    lbox= self.PBCheck(boxR,boxC-1,boxPos,(boxR,boxC),depth+1)
                
            # Checking if Right box if free or not
            if (boxR,boxC+1) in boxPos:
                if (boxR,boxC+1) == parent:
                    rbox=True
                else:
                    rbox = self.PBCheck(boxR,boxC+1,boxPos,(boxR,boxC),depth+1)

            # If both left and right boxes are movable(false) then return false
            # else return true
            # if lbox==False and rbox==False:
            if not (lbox or rbox):
                hBlocked=False
            else:
                hBlocked=True
        
        # box at up or down position
        if not vBlocked and ((boxR-1,boxC) in boxPos or (boxR+1,boxC) in boxPos):
            
            # Checking if upper box if free or not
            ubox=dbox=None
            if (boxR-1,boxC) in boxPos:
                if (boxR-1,boxC)==parent:
                    ubox=True
                else:
                    ubox=self.PBCheck(boxR-1,boxC,boxPos,(boxR,boxC),depth+1)
                
            # Checking if lower(down) box if free or not
            if (boxR+1,boxC) in boxPos:
                if (boxR+1,boxC) == parent:
                    dbox=True
                else:
                    dbox = self.PBCheck(boxR+1,boxC,boxPos,(boxR,boxC),depth+1)

            # If both up and down boxes are movable(false) then return false
            # else return true
            # if lbox==False and rbox==False:
            if not (ubox or dbox):
                vBlocked=False
            else:
                vBlocked=True
            
        # deadlock
        if hBlocked and vBlocked:
            return True
        else:
            return False
        


    def PBCheckPurana(self, boxPosX, boxPosY, boxPos, checkedBoxes):
        board = self.sokoban.board
        goal = self.sokoban.goal

        checkedBoxes.append((boxPosX, boxPosY))

        check =[((1, 0), (0, 1)), 
                ((1, 0), (0, -1)), 
                ((-1, 0), (0, 1)), 
                ((-1, 0), (0, -1))]

        for a, b in check:
            adj1 = (boxPosX+a[0], boxPosY+a[1])
            adj2 = (boxPosX+b[0], boxPosY+b[1])

            # adj1 box and adj2 wall
            # adj1 wall and adj2 box
            # adj1 and 2 wall
            # adj1 and 2 box

            # Poor block waited for her neighbour's reply but he may be blocked! Sed lyf    

            if adj1  in checkedBoxes and adj2 in checkedBoxes:
                # return true only after checking that any of 4 boxes are not on goal position
                if (adj1, adj2, (boxPosX, boxPosY), (adj1[0]+adj2[0], adj1[1]+adj2[1])) not in goal:
                    return True

            if (adj1 in boxPos or board[adj1[0]][adj1[1]] == "#") and (adj2 in boxPos or board[adj2[0]][adj2[1]] == "#"):

                if board[adj1[0]][adj1[1]] == "#" and board[adj2[0]][adj2[1]] == "#":
                    if (boxPosX, boxPosY) not in goal:
                        return True

                if adj1 in boxPos and adj1 not in checkedBoxes:
                    blocked1 = self.PBCheckPurana(adj1[0], adj1[1],boxPos,checkedBoxes)
                    if blocked1 and board[adj2[0]][adj2[1]] == "#":
                        return True

                    elif adj2 in boxPos and adj2 not in checkedBoxes:
                        blocked2 = self.PBCheckPurana(adj2[0], adj2[1],boxPos,checkedBoxes)
                        
                        if blocked1 and blocked2:
                            if (boxPosX, boxPosY) not in goal:
                                return True

                if adj2 in boxPos and adj2 not in checkedBoxes:
                    blocked2 = self.PBCheckPurana(adj2[0], adj2[1],boxPos,checkedBoxes)
                    if blocked2 and board[adj1[0]][adj1[1]] == "#":
                        return True

                    elif adj1 in boxPos and adj1 not in checkedBoxes:
                        blocked2 = self.PBCheckPurana(adj1[0], adj1[1],boxPos,checkedBoxes)

                        if blocked1 and blocked2:
                            if (boxPosX, boxPosY) not in goal:
                                return True 

        return False


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

    boxPos=[(7,2),(7,3),(7,4),(6,3),(6,4)]  # write box position here
    goalPos=[]  # write goal position here
    
    workerPos=(1,1)

    SBobj=Sokoban(board,boxPos,goalPos,workerPos)        

    agnt=Agent(SBobj)
    isBlocked=agnt.PBCheck(7,2,SBobj.root.boxPos,(-1,-1),1)

    print(isBlocked)