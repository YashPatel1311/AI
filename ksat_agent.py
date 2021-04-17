from kSAT_environment import Tree
from queue import PriorityQueue,Queue


class Agent:

    finalSolutions = []
    variables = set()
    def __init__(self,k,n,m):
        '''
        k=no of var in each clause \n
        n=no of var \n
        m=no of clauses \n\n

        Output: List containing randomly generated clauses 
        '''
        self.tree=Tree(k,n,m)
        for i in range(n):
            self.variables.add(chr(65+i))
        # self.k=k
        # self.n=n
        # self.m=m

    

    def evaluate(self,val):
        '''
        Integer input representing truth values of variables in binary \n
        Problem instance \n
        Goal : to find the whether truth value of problem is True or not. \n
        '''
        # truthVal = bin(truthVal)
        # truthVal=truthVal[2:]
        problem = self.tree.problem
        truthVal = format(val,"026b")
        n = len(truthVal)-1
        # exp = ""
        tmp1 = True
        # assuming problem is list of list containing variables as dtype=str
        for i in problem:
            # exp += "("
            tmp2 = False
            for j in i:

                if j.isupper():
                    # exp += str(truthVal[ord(j)-ord("A")])
                    tmp2 |= bool(int(truthVal[n-(ord(j)-ord("A"))]))
                elif j.islower():
                    # exp += str(truthVal[ord(j)-ord("a")])
                    tmp2 |= (not bool(int(truthVal[n-(ord(j)-ord("a"))])))
                # exp += "∨"
                if tmp2:
                    break
            tmp1 &= tmp2
        #     exp = exp[:-1]
        #     exp += ") ∧"
        # exp = exp[:-2]
        if tmp1:
            return truthVal
        return None


    def VariableNeighbourhood(self,problem,initial):
        if len(initial) == self.tree.n:
            if self.verify(initial):
                return initial
            else:
                return None

        currSol = initial.copy()
        solutions = Queue()

        for key in currSol:
            newPossibleSol = currSol.copy()
            newPossibleSol[key] = not currSol[key]
            isCorrect = self.evaluate(problem,newPossibleSol)
            if isCorrect:
                solutions.put(newPossibleSol)

        while not solutions.empty():
            sol = solutions.get()
            currVar = set(sol.keys())
            if len(sol) != self.tree.n:
                rem = list(self.variables-currVar)
                while not self.empty(rem):
                    sol_0 = sol.copy()
                    sol_1 = sol.copy()
                    toInsert = rem.pop(0)
                    sol_0[toInsert] = False
                    sol_1[toInsert] = True
                    newSol_0 = self.VariableNeighbourhood(problem,sol_0)
                    newSol_1 = self.VariableNeighbourhood(problem,sol_1)
                    if newSol_0 != None:
                        solutions.put(newSol_0)
                    if newSol_1 != None:
                        solutions.put(newSol_1)
            else:
                return self.finalSolutions.append(sol)
        # return finalSolutions

    # empty() method for list
    def empty(self,lst):
        if len(lst) == 0:
            return True
        else:
            return False

    # to generate initial solution by assigning least variables
    def initSol(self):
        problem = self.tree.problem
        res = {}
        for i in problem:
            if i[0].upper() not in res:           
                if i[0].isupper():
                    res[i[0]] = True
                elif i[0].islower():
                    res[i[0].upper()] = False
        return res


    # to verify whether sol is correct or not
    def verify(self,sol):
        problem = self.tree.problem
        tmp1 = True
        for clause in problem:
            tmp2 = False
            for variable in clause:
                if variable.isupper():
                    tmp2 |= sol[variable]
                elif variable.islower():
                    tmp2 |= not sol[variable.upper()]
                # tmp2 |= sol[variable.upper()]
            tmp1 &= tmp2
        if tmp1:
            return True
        else:
            return False

    # to evaluate problem on a possible solution
    def evaluate(self,problem,possibleSol):
        tmp1 = True
        for i in problem:
            tmp2 = False
            for j in i:
                if j.upper() in possibleSol:
                    if j.isupper():
                        tmp2 |= possibleSol[j]
                    elif j.islower():
                        tmp2 |= not possibleSol[j.upper()]
                    # tmp2 |= possibleSol[j.upper()]
                else:
                    tmp2 |= False
                if tmp2:
                    break
            tmp1 &= tmp2

        if not tmp1:
            return True
        else:
            return None


    def BruteForce(self):
        problem=self.tree.problem
        n=self.tree.n
        for i in range(2**n-1):
            result=self.evaluate(i)
            if result != None:
                return result

        return None


    def HillClimb(self):

        currNode=self.tree.root
        currNode.cost=currNode.heuristic()
        childs=self.tree.moves(currNode)
        counter=0

        while True:

            counter+=1

            if len(childs)!=0:
                childs[0].cost=childs[0].heuristic()
                childs[1].cost=childs[1].heuristic()

                if currNode.cost>childs[0].cost or currNode.cost>childs[1].cost:

                    if childs[0].cost<=childs[1].cost:
                        currNode=childs[0]

                    elif childs[1].cost<childs[0].cost:
                        currNode=childs[1]

                    childs=self.tree.moves(currNode)

                else:
                    break

            else:
                break

        return currNode,counter

    def BeamSearch(self,width):
        frontier = PriorityQueue()
        
        self.tree.root.cost = self.tree.root.heuristic()
        # explored = self.explored
        # self.Tree.root.cost = self.cal_cost(self.Tree.root,optimizer)
        frontier.put(self.tree.root)


        counter=0

        while not frontier.empty():
            counter+=1
            node = frontier.get()
            # conf = node.config
            # confStr = str(list(map(int,conf))).replace(",","").replace("[","").replace("]","").replace(" ","")
            # explored[confStr]=node
            
            if node.cost==0:
                return node,counter

                
            temp = PriorityQueue()
            neighbours = self.tree.moves(node)
            
            for neighbour in neighbours:
                neighbour.cost=neighbour.heuristic()
                temp.put(neighbour)

            for i in range(frontier.qsize()):
                
                temp.put(frontier.get())

            for i in range(min(width,temp.qsize())):

                frontier.put(temp.get())

            # neighbours=self.Trees.moves(node)

            # for neighbour in neighbours:
            #     neighbour.cost = self.width
            # #   configuration = neighbour.config
            # #   configurationStr = str(list(map(int,configuration))).replace(",","").replace("[","").replace("]","").replace(" ","")
            # if configurationStr not in explored:
            #     frontier.put(neighbour)
            # else:
            #     del(neighbour)

        return node , counter
