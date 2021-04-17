from ksat_agent import Agent

def driver():
    agt=Agent(3,20,70)

    print("Hill climb search results: ")
    result,iterations=agt.HillClimb()
    # print(result[-6:])
    print("Remaining clauses:", result.cost)
    print("Nodes explored:", iterations)
    pathLen=0
    for key,val in result.config.items():
        if val !=None:
            pathLen+=1
    print(result.config)
    print("Penetrance: ",pathLen/iterations)
    print()

    result,iterations=agt.BeamSearch(6)
    # print(result[-6:])
    print("Beam search results: ")
    print("Remaining clauses:", result.cost)
    print("Nodes explored:", iterations)
    pathLen=0
    for key,val in result.config.items():
        if val !=None:
            pathLen+=1
    print(result.config)
    print("Penetrance: ",pathLen/iterations)
    print()



    initial = agt.initSol()
    agt.VariableNeighbourhood(agt.tree.problem,initial)
    # for i in range(agt.tree.n):
    #     if chr(65+i) is not initial:
    #         initial[chr(65+i)] = False
    print("Initial Solution:",initial)
    if len(agt.finalSolutions) != 0:
        print("Neighbour Solution:",agt.finalSolutions[0])
    else:
        print("No optimized solution exist in neighbourhood!!!")

if __name__=="__main__":
    driver()