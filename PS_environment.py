import numpy as np
import sys
from tabulate import tabulate
import copy



# 0 -> up
# 1 -> downe
                 
# 2 -> lefte
# 3 -> right
# blank -> False
# peg -> True

class Board:

    def __init__(self):
        self.pos=[None]*34
        pos=self.pos
        
        
        for i in range(1,34):
            pos[i] = Cell(i)

        pos[1].right=pos[2]
        pos[1].down=pos[4]

        pos[2].right=pos[3]
        pos[2].down=pos[5]
        pos[2].left=pos[1]
        
        pos[3].down=pos[6]
        pos[3].left=pos[2]

        pos[4].right=pos[5]
        pos[4].up=pos[1]
        pos[4].down=pos[9]

        pos[5].up=pos[2]
        pos[5].down=pos[10]
        pos[5].left=pos[4]
        pos[5].right=pos[6]

        pos[6].left=pos[5]
        pos[6].up=pos[3]
        pos[6].down=pos[11]

        pos[7].down=pos[14]
        pos[7].right=pos[8]

        pos[8].down=pos[15]
        pos[8].left=pos[7]
        pos[8].right=pos[9]

        pos[9].up=pos[4]
        pos[9].down=pos[16]
        pos[9].left=pos[8]
        pos[9].right=pos[10]
        
        pos[10].up=pos[5]
        pos[10].down=pos[17]
        pos[10].left=pos[9]
        pos[10].right=pos[11]

        pos[11].right = pos[12]
        pos[11].left = pos[10]
        pos[11].up = pos[6]
        pos[11].down = pos[18]
        
        pos[12].right = pos[13]
        pos[12].left = pos[11]
        pos[12].down = pos[19]

        pos[13].left = pos[12]
        pos[13].down = pos[20]
        
        pos[14].right = pos[15]
        pos[14].up = pos[7]
        pos[14].down = pos[21]

        pos[15].right = pos[16]
        pos[15].left = pos[14]
        pos[15].up = pos[8]
        pos[15].down = pos[22]
        
        pos[16].right = pos[17]
        pos[16].left = pos[15]
        pos[16].up = pos[9]
        pos[16].down = pos[23]

        pos[17].right = pos[18]
        pos[17].left = pos[16]
        pos[17].up = pos[10]
        pos[17].down = pos[24]

        pos[18].right = pos[19]
        pos[18].left = pos[17]
        pos[18].up = pos[11]
        pos[18].down = pos[25]

        pos[19].right = pos[20]
        pos[19].left = pos[18]
        pos[19].up = pos[12]
        pos[19].down = pos[26]

        pos[20].left = pos[19]
        pos[20].up = pos[13]
        pos[20].down = pos[27]

        pos[21].right = pos[22]
        pos[21].up = pos[14]

        pos[22].right = pos[23]
        pos[22].left = pos[21]
        pos[22].up = pos[15]

        pos[23].right = pos[24]
        pos[23].left = pos[22]
        pos[23].up = pos[16]
        pos[23].down = pos[28]

        pos[24].right = pos[25]
        pos[24].left = pos[23]
        pos[24].up = pos[17]
        pos[24].down = pos[29]

        pos[25].right = pos[26]
        pos[25].left = pos[24]
        pos[25].up = pos[18]
        pos[25].down = pos[30]

        pos[26].up = pos[19]
        pos[26].right=pos[27]
        pos[26].left=pos[25]
        
        pos[27].up = pos[20]
        pos[27].left=pos[26]

        pos[28].up = pos[23]
        pos[28].right=pos[29]
        pos[28].down=pos[31]

        pos[29].up = pos[24]
        pos[29].right=pos[30]
        pos[29].left=pos[28]
        pos[29].down=pos[32]
                
        pos[30].left = pos[29]
        pos[30].up = pos[25]
        pos[30].down = pos[33]

        pos[31].right = pos[32]
        pos[31].up = pos[28]

        pos[32].up = pos[29]
        pos[32].right = pos[33]
        pos[32].left = pos[31]

        pos[33].left = pos[32]
        pos[33].up = pos[30]
    
    def __getitem__(self,p):
        return self.pos[p]

class Cell:
    def __init__(self,idx):
        self.idx=idx
        self.up=None
        self.down=None
        self.left=None
        self.right=None

class Node:
    # config is a boolean list which stores the state of game 
    def __init__(self,parent,config,level):
        self.parent=parent
        self.config=config  
        self.level=level
        self.cost=self.calCost()

    def __str__(self):
        config=self.config[1:]
        for itm in range(len(config)):
  
          if config[itm] == True:
            config[itm]="●"
          elif config[itm] == False:
            config[itm]=" "

        two=["╳", "╳"]
        config=two+config[:3]+two + two+config[3:6]+two + config[6:13] + config[13:20] + config[20:27] + two+config[27:30]+two + two+config[30:]+two

        temp = np.array(config)
        newtemp = temp.reshape(7,7)
        config = newtemp
        table = tabulate(config, tablefmt="fancy_grid")
        return f"{table}"

    def calCost(self):
        hn=32-self.config[1:].count(False)

        return hn+self.level

    def __lt__(self, other):
        # return self.level<other.level
        return self.cost<other.cost



class PegSolitare:

    def __init__(self):
                    
        # initial = [False,False,False,True,False,False,False,True,True,True,True,True,False,False,True,True,True,True,True,False,False,True,True,True,False,False,False,False,True,False,False,False,False,False]
        initial = [True]*34
        initial[17]=False

        self.root=Node(None,initial,0)
        print(self.root)
        self.size=34

        self.board=Board()

    
    def moves(self,node):
        """ 
        curr -> position of peg to be moved
        direction -> possible moves
                0 -> up
                1 -> down
                2 -> left
                3 -> right
        config -> current configuration
        """
        result=[]

        board=self.board

        for curr in range(1,34):
            if node.config[curr]==False:
                continue

            for direction in range(0,4):
                NewConfig = copy.deepcopy(node.config)
                if direction == 0 :
                    try:
                        Next=board[curr].up.idx
                        Dest=board[curr].up.up.idx
                    except:
                        continue


                elif direction == 1 :
                    try:
                        Next=board[curr].down.idx
                        Dest=board[curr].down.down.idx
                    except:
                        continue


                elif direction == 2 :
                    try:

                        Next=board[curr].left.idx
                        Dest=board[curr].left.left.idx
                    except:
                        continue

                elif direction == 3:
                    try:
                        Next=board[curr].right.idx
                        Dest=board[curr].right.right.idx
                    except:
                        continue


                if NewConfig[Next] == True and NewConfig[Dest] == False:
                    NewConfig[curr]=False
                    NewConfig[Dest] = True
                    NewConfig[Next] = False

                    result.append(Node(node,NewConfig,node.level+1))

        return result