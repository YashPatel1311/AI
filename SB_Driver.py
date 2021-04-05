from SB_Agent import Agent
from SB_environment import Sokoban

if __name__=="__main__":
    board=[
	[' ',' ','#','#','#','#','#',' '],           
    ['#','#','#',' ',' ',' ','#',' '],  
    ['#',' ',' ',' ',' ',' ','#',' '],    
    ['#','#','#',' ',' ',' ','#',' '],  
    ['#',' ','#','#',' ',' ','#',' '],  
    ['#',' ','#',' ',' ',' ','#','#'],  
    ['#',' ',' ',' ',' ',' ',' ','#'],
    ['#',' ',' ',' ',' ',' ',' ','#'],  
    ['#','#','#','#','#','#','#','#']]

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

    boxPos=[(4,1),(6,3),(7,4),(6,6),(2,1),(3,5),(5,4)]  # write box position here
    # boxPos=[(2,1),(4,1),(3,5),(5,4),(6,6),(7,4),(6,3)]  # write goal position here    
    goalPos=[(2,1),(4,1),(3,5),(5,4),(6,6),(7,4),(6,3)]  # write goal position here    
    workerPos=(0,0)

    # boxPos = [(2,2),(3,2)]
    # goalPos = [(1,3),(3,3)]
    # workerPos = (2,1)

    SBobj=Sokoban(board,boxPos,goalPos,workerPos)        

    agnt=Agent(SBobj)
    # flag=False
    # for boxR,boxC in boxPos:
    #     if (boxR,boxC) not in goalPos:
    #         if agnt.PBCheck(boxR,boxC,boxPos,(-1,-1),1):
    #             flag=True
    #             break

    # if flag:
    #     print("Error")

    # else:
    #     print("pass")

    result,counter=agnt.DFS()
    print(counter)
    agnt.printPath(result)


