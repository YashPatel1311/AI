from SB_environment import Sokoban,Node
from queue import PriorityQueue
import copy
import time
import pygame
import sys



class Agent:

    def __init__(self, sokoban):
        self.sokoban = sokoban
        self.frontier = PriorityQueue()
        self.explored = {}
        self.stack=[]

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

    def isGoal(self,node):
        goal=self.sokoban.goal
        boxPos=node.boxPos

        if set(goal)==set(boxPos):
            return True
        else:
            return False

    def heuristic(self,node,goal):
        boxPos=copy.deepcopy(node.boxPos)
        boxPos.sort(key = lambda x: x[0] + x[1])

        cost=0

        for i in range(len(boxPos)):
            cost+=abs(boxPos[i][0]-goal[i][0])+abs(boxPos[i][1]-goal[i][1])

        return cost


    def conf2str(self,node):
        """
           Function to convert boxPos and workerPos to string 
           This function is used for hashing of configuration
        """
        result=""

        srted=set(node.boxPos)

        for r,c in srted:
            result=result+str(r)+str(c)

        result=result+str(node.workerPosX)+str(node.workerPosY)

        return result


    def printPath(self,node,filename):
        
        if(node != None):
            
            result=self.printPath(node.parent,filename)
            result.append(node)

            node.Print(self.sokoban,filename)
            return result

        else:
            return []


    def DFS(self):
        frontier = self.stack
        explored = self.explored
        goal=self.sokoban.goal
    
        frontier.append(self.sokoban.root)
        counter=0

        while len(frontier)>0:
            
            node = frontier.pop(-1)
            # node.Print(self.sokoban)
            if counter%10000==0:
                print(counter)
                
            counter+=1            
            
            # Add current node to explored
            explored[self.conf2str(node)]=None

            # Check if current node is goal node
            if self.isGoal(node):
                return node,counter

            # Find children of current node
            children=self.sokoban.moves(node)

            # Check for deadlock in all children's configuration which are not on goal pos
            # Calculate heuristic value for all valid child
            # Push them to frontier
            for child in children:

                configurationStr = self.conf2str(child)
                if configurationStr not in explored:

                # flag-> false means current configuration has no deadlock and is default behaviour    
                # If any box which is not on goal position and is permanent blocked then there is a deadlock
                    flag=False
                    for boxR,boxC in child.boxPos:
                        if (boxR,boxC) not in goal:
                            if self.PBCheck(boxR,boxC,child.boxPos,(-1,-1),1):
                                
                                flag=True
                                break
                    # deadlock -> prun the branch
                    if flag:
                        del(child)
                        continue

                    frontier.append(child)

                # already visited (infinite loop)
                else:
                    del(child)
                
        return None

    def BFS(self):
        frontier = self.frontier
        explored = self.explored
        goal=self.sokoban.goal
    
        frontier.put(self.sokoban.root)
        counter=0

        while not frontier.empty():
            
            node = frontier.get()
            # node.Print(self.sokoban,"path.txt")
            if counter%10000==0:
                print(counter)
                
            counter+=1            
            
            # Add current node to explored
            explored[self.conf2str(node)]=None

            # Check if current node is goal node
            if self.isGoal(node):
                return node,counter

            # Find children of current node
            children=self.sokoban.moves(node)

            # Check for deadlock in all children's configuration which are not on goal pos
            # Calculate heuristic value for all valid child
            # Push them to frontier
            for child in children:

                configurationStr = self.conf2str(child)
                if configurationStr not in explored:

                # flag-> false means current configuration has no deadlock and is default behaviour    
                # If any box which is not on goal position and is permanent blocked then there is a deadlock
                    flag=False
                    for boxR,boxC in child.boxPos:
                        if (boxR,boxC) not in goal:
                            if self.PBCheck(boxR,boxC,child.boxPos,(-1,-1),1):
                                
                                flag=True
                                break
                            
                    if flag:
                        del(child)
                        continue
                    
                    # h(x) is included while computing cost -> A*
                    child.cost=self.heuristic(child,goal)+child.level     # cost = h(x) + g(x)
                    
                    # only g(x) is considered -> breadth first search
                    # child.cost=child.level
                    frontier.put(child)

                else:
                    del(child)
                
        return None

    def is_valid_value(self,char):
        if ( char == ' ' or #floor
            char == '#' or #wall
            char == '@' or #worker on floor
            char == '.' or #goal
            char == '*' or #box on goal
            char == '$' or #box
            char == '+' ): #worker on goal
            return True
        else:
            return False
    
    def MakeLevel(self,filename,level):
        # self.queue = Queue.LifoQueue()
        self.matrix = []
        #        if level < 1 or level > 50:
        if level < 1:
            print ("ERROR: Level "+str(level)+" is out of range")
            sys.exit(1)
        else:
            file = open(filename,'r')
            level_found = False
            for line in file:
                row = []
                if not level_found:
                    if  "Level "+str(level) == line.strip():
                        level_found = True
                else:
                    if line.strip() != "":
                        row = []
                        for c in line:
                            if c != '\n' and self.is_valid_value(c):
                                row.append(c)
                            elif c == '\n': #jump to next row when newline
                                continue
                            else:
                                print ("ERROR: Level "+str(level)+" has invalid value "+c)
                                sys.exit(1)
                        self.matrix.append(row)
                    else:
                        break

    def Interactive(self,path):
        board=self.sokoban.board

        BLACK = (0, 0, 0)
        WINDOW_HEIGHT = len(board)*36
        WINDOW_WIDTH = len(board[0])*36

        pygame.display.set_caption('Sokoban')
        print("[+] Initailizing game...")

        pygame.init()
        SCREEN = pygame.display.set_mode((max(WINDOW_WIDTH,52), WINDOW_HEIGHT+50))
        # display_surface = pygame.display.set_mode((max(WINDOW_WIDTH,52), WINDOW_HEIGHT+50))
        CLOCK = pygame.time.Clock()
        SCREEN.fill(BLACK)

        print("[+] Rendering graphics...")
        i=0
        choice=1
        while i<len(path):
            # print(WINDOW_WIDTH)
            # print(f"    WINDOW_HEIGHT -> {WINDOW_HEIGHT} \n    WINDOW_WIDTH -> {WINDOW_WIDTH}")
            choice=self.drawGrid(path[i],choice)

            if choice==1:
                i=i+1
            elif choice==-1:
                i=i-1
            else: 
                i=i+1



    def drawGrid(self,node,choice):
        board=self.sokoban.board
        WINDOW_HEIGHT = len(board)*36
        WINDOW_WIDTH = len(board[0])*36

        display_surface = pygame.display.set_mode((max(WINDOW_WIDTH,52), WINDOW_HEIGHT+50))

        # Load level images
        wall = pygame.image.load('imgs\\wall.png').convert()
        box = pygame.image.load('imgs\\box.png').convert()
        box_on_target = pygame.image.load('imgs\\box_on_target.png').convert()
        player_on_target = pygame.image.load(
            'imgs\\player_on_targe.jpeg').convert()
        space = pygame.image.load('imgs\\space.png').convert()
        target = pygame.image.load('imgs\\target.png').convert()
        player = pygame.image.load('imgs\\player.png').convert()

        margin=(max(WINDOW_WIDTH,52)-(36*3))/4
        
        navLeft=button('black',margin,WINDOW_HEIGHT+4,36,36,'Left')
        navRight=button('black',2*margin+36,WINDOW_HEIGHT+4,36,36,'Right')
        navAuto=button('black',3*margin+2*36,WINDOW_HEIGHT+4,36,36,'Auto')

        blockSize = 36  # Set the size of the grid block
        for x in range(0, WINDOW_HEIGHT, blockSize):
            for y in range(0, WINDOW_WIDTH, blockSize):

                # print(f"({x//blockSize},{y//blockSize})    ====>    {mat[x//blockSize][y//blockSize]}")
                if board[x//blockSize][y//blockSize] == "#":
                    display_surface.blit(wall, (y, x))

                if board[x//blockSize][y//blockSize] == " ":
                    display_surface.blit(space, (y, x))

                if (x//blockSize,y//blockSize) in node.boxPos :
                    display_surface.blit(box, (y, x))

                if (x//blockSize,y//blockSize) in self.sokoban.goal:
                    display_surface.blit(target, (y, x))

                if (x//blockSize,y//blockSize) in self.sokoban.goal and (x//blockSize,y//blockSize) in node.boxPos:
                    display_surface.blit(box_on_target, (y, x))

                if (x//blockSize,y//blockSize) == (node.workerPosX,node.workerPosY):
                    display_surface.blit(player, (y, x))
                    if (x//blockSize,y//blockSize) in self.sokoban.goal:
                        display_surface.blit(player_on_target, (y, x))


        navLeft.draw(display_surface,outline='white')
        navRight.draw(display_surface,outline='white')
        navAuto.draw(display_surface,outline='white')

        pygame.display.update()

        if choice!=0:

            while True:
                for event in pygame.event.get():

                    if event.type==pygame.MOUSEBUTTONDOWN:
                        pos=pygame.mouse.get_pos()

                        if navLeft.isOver(pos):
                            return -1

                        elif navRight.isOver(pos):
                            return 1

                        elif navAuto.isOver(pos):
                            return 0

                    if event.type == pygame.QUIT:
                        print("[+] Quiting...")
                        pygame.quit()
                        sys.exit()       

        else:
            start_time = time.time()
            while True:
                current_time = time.time()
                elapsed_time = current_time - start_time

                if elapsed_time>1:
                    return 0

                for event in pygame.event.get():

                    if event.type==pygame.MOUSEBUTTONDOWN:
                        pos=pygame.mouse.get_pos()

                        if navLeft.isOver(pos):
                            return -1

                        elif navRight.isOver(pos):
                            return 1

                    if event.type == pygame.QUIT:
                        print("[+] Quiting...")
                        pygame.quit()
                        sys.exit()



            return choice     


class button:
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:

            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 15)
            text = font.render(self.text, 1, (255,255,255))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False