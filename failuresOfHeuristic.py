# ALL LIST

%%time
import math
def huristic(currentState):
    patients = [k for k,v in currentState.items() if v == 'P']
    hospitals = [k for k,v in currentState.items() if v == 'H']
#     printState(currentState)
    location = currentState['A']
    minDis = 500000
    for k in patients:
        toPatent = math.sqrt(pow(location[0]-k[0],2)+pow(location[1]-k[1],2))
        for h in hospitals:
            toHospital = math.sqrt(pow(k[0]-h[0],2)+pow(k[1]-h[1],2))
            if(toHospital < minDis):
                minDis = toHospital
#     print(math.sqrt(minDis))
    return math.sqrt(minDis)

def findMinForA(gCost, hCost, length):
    minCost = 500000
    index = 0
    for i in range(length):
        temp = gCost[i] + hCost[i]
        if(temp<minCost):
            minCost = temp
            index = i
    return i
    
def AStar(start):
    initialState = initiateState(start)
    if(not('P' in initialState.values())):
        printState(initialState)
        return "done"
    
    frontier = []
    explored = set()
    hCost = []
    gCost = []
    frontierLen = 1
    gCost.append(0)
    hCost.append(huristic(initialState))
    frontier.append(initialState)
    
    while(frontier):
        minIndex = findMinForA(gCost, hCost, frontierLen)
        node = frontier.pop(minIndex)
        nodeGCost = gCost.pop(minIndex)
        nodeHCost = hCost.pop(minIndex)
#         print("Node in while loop!")
#         printState(node)
#         print("states:",states)
#         print("frontier:",frontier)
#         print("explored:",explored)
#         print("cost:",actualCost)
        for action in actions:
#             print(action)
            child = updateState(node.copy(),action)
            if child!= null:
#                 print("child")
#                 printState(child)
                if(not('P' in child.values())):
#                     printState(node)
                    return "done"
                hashChild = hash(frozenset(child.items()))
    
#                 if hashChild in actualCost:
#                     actualChildCost = actualCost[hashChild]
                    
#                 if(hashChild in frontier):
#                     if actualChildCost <= childCost:
#                         continue
#                 elif(hashChild in explored):
#                     if actualChildCost <= childCost:
#                         frontier[hashChild] = actualChildCost + huristic(child)
#                         explored.remove(hashChild)
#                 else:
                if(child not in frontier and  hashChild not in explored):
                    frontier.append(child)
                    gCost.append(nodeGCost + 1)
                    hCost.append(huristic(child))
        explored.add(hashChild)
    return null

print(AStar('test3.txt'))


# ///////////////////////////////////////////////////////////////////////////
# OROGONAL WITH DICTIONARY 

%%time
import math
def huristic(currentState):
    patients = [k for k,v in currentState.items() if v == 'P']
    hospitals = [k for k,v in currentState.items() if isinstance(v,int)]
#     printState(currentState)
    location = currentState['A']
    minDis = 500000
    for k in patients:
        toPatient = math.sqrt(pow(location[0]-k[0],2)+pow(location[1]-k[1],2))
#         print("P:",toPatient)
        for h in hospitals:
            toHospital = toPatient + math.sqrt(pow(k[0]-h[0],2)+pow(k[1]-h[1],2))
#             print("H:", toHospital)
            if(toHospital < minDis):
                minDis = toHospital
#     print(math.sqrt(minDis))
    return minDis

def AStar(start):
    seenStates = 0
    distinctSeenStates = 0
    initialState = initiateState(start)
    if(not('P' in initialState.values())):
        printState(initialState)
        return "done"
    
    frontier = {}
    states = {}
    explored = set()
    actualCost = {}
    
    hashNode = hash(frozenset(initialState.items()))
    actualCost[hashNode] = 0
    frontier[hashNode] = huristic(initialState)
    states[hashNode] = initialState
    
    while(frontier):
        distinctSeenStates+=1
        hashNode = min(frontier.keys(), key=(lambda k: frontier[k]))
        node = states[hashNode]
        nodeCost = actualCost[hashNode]
        explored.add(hashNode)
        del frontier[hashNode]
#         print("Node in while loop!")
#         printState(node)
#         print("states:",states)
#         print("frontier:",frontier)
#         print("explored:",explored)
#         print("cost:",actualCost)
        for action in actions:
#             print(action)
            child = updateState(node.copy(),action)
            if child!= null:
                seenStates += 1
#                 print("child")
#                 printState(child)
                if(not('P' in child.values())):
#                     printState(node)
                    return {'seen state': seenStates, 'distinct seen states': distinctSeenStates}
                childCost = nodeCost + 1
                hashChild = hash(frozenset(child.items()))
#                 if hashChild in actualCost:
#                     actualChildCost = actualCost[hashChild]
                    
#                 if(hashChild in frontier):
#                     if actualChildCost <= childCost:
#                         continue
#                 elif(hashChild in explored):
#                     if actualChildCost <= childCost:
#                         frontier[hashChild] = actualChildCost + huristic(child)
#                         explored.remove(hashChild)
#                 else:
                if(hashChild not in frontier and hashChild not in explored):
                    frontier[hashChild] = childCost + huristic(child)
                actualCost[hashChild] = childCost
                states[hashChild] = child
    return null
print(AStar('test2.txt'))

# ///////////////////////////////////////////////////////////////////////////////////////////
# FRONTIER WITH LIST


def AStar(start):
    initialState = initiateState(start)
    if(not('P' in initialState.values())):
        printState(initialState)
        return "done"
    
    frontier = []
    explored = set()
    actualCost = {}
#     print(1)
    hashNode = hash(frozenset(initialState.items()))
    actualCost[hashNode] = 0
    frontier.append((initialState,huristic(initialState)))
#     print(2)    
    while(frontier):
#         print(3)
        frontier.sort(key = lambda x: x[1]) 
#         print(frontier)
        node, huristicCost = frontier.pop(0)
#         print(node)
        
#         printState(node)
        hashNode = hash(frozenset(node.items()))
#         print(565)
        nodeCost = actualCost[hashNode]
#         print(4)
#         print("Node in while loop!")
#         printState(node)
#         print("states:",states)
#         print("frontier:",frontier)
#         print("explored:",explored)
#         print("cost:",actualCost)
        for action in actions:
#             print(action)
#             print(5)
            child = updateState(node.copy(),action)
            if child!= null:
#                 print("child")
#                 printState(child)
#                 print(6)
                if(not('P' in child.values())):
#                     printState(node)
                    return "done"
                childCost = nodeCost + 1
                hashChild = hash(frozenset(child.items()))
#                 print(7)
#                 if hashChild in actualCost:
#                     actualChildCost = actualCost[hashChild]
                    
#                 if(hashChild in frontier):
#                     if actualChildCost <= childCost:
#                         continue
#                 elif(hashChild in explored):
#                     if actualChildCost <= childCost:
#                         frontier[hashChild] = actualChildCost + huristic(child)
#                         explored.remove(hashChild)
#                 else:
# hashChild not in frontier and 
                if(hashChild not in explored):
#                     print(8)
                    frontier.append((child, childCost + huristic(child)))
                actualCost[hashChild] = childCost
#                 print(9)
        explored.add(hashNode)
#         print(10)
    return null


# /////////////////////////////////////////////////
# ALL LISTS- Cost are in one!

def AStar(start):
    seenStates = 0
    distinctSeenStates = 0
    initialState = initiateState(start)
    if(not('P' in initialState.values())):
        printState(initialState)
        return "done"
    frontier = []
    explored = set()
    costs = []
    frontierLen = 1
    
    frontier.append(initialState)
    costs.append((0,huristic(initialState)))
    while(frontier):
        distinctSeenStates+=1
        nodeIndex = 0
        nodeFCost = float('inf')
        for i in range(frontierLen):
            iCost = costs[i]
            temp = iCost[0] + iCost[1]
            if(temp < nodeFCost):
                nodeIndex = i
                nodeFCost = temp
        node = frontier.pop(nodeIndex)
        nodeCost = costs.pop(nodeIndex)
        frontierLen -= 1
        explored.add(hash(frozenset(node.items())))
        for action in actions:
#             print(action)
            child = updateState(node.copy(),action)
            if child!= null:
                seenStates += 1
#                 print("child")
#                 printState(child)
                if(not('P' in child.values())):
#                     printState(node)
                    return {'seen state': seenStates, 'distinct seen states': distinctSeenStates}
                childCost = nodeCost[0] + 1
                hashChild = hash(frozenset(child.items()))
                if(not(child in frontier) and not(hashChild in explored)):
                    frontier.append(child)
                    costs.append((childCost, huristic(child)))
                    frontierLen += 1
    return null