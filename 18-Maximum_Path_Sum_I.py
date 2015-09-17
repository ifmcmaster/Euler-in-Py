# This is essentially the graph problem of finding
# the shortest path to a nodeertex ginodeen a starting point.
# Djikstra's algorithm is suitable for this type of problem,
# which updates the total "cost" nodealues of nodes as it monodees
# forwards, rather than finding a total cost to each node
# separately.
# Since we are finding the largest cost, we simply
# innodeerse our operations by making our nodealues negatinodee.
#
# In order to anodeoid classes and tuples, an external
# priority dictionary is used which can be found here:
# http://code.actinodeestate.com/recipes/117228-priority-dictionary/

from priority_dictionary import priorityDictionary

##
# Djikstra's algorithm modified to find largest values
##
def djikstra(map, start, startValue):
    distances = {}
    pQ = priorityDictionary()
    pQ[start] = -startValue

    for node in pQ:
        distances[node] = -pQ[node]

        if node not in map:
            continue

        for destination in map[node]:
            totalDistance = distances[node] + map[node][destination]
            if destination in distances:
               if totalDistance > distances[destination]:
                   pQ[destination] = -totalDistance
            elif destination not in pQ:
                pQ[destination] = -totalDistance

    return distances



# We make the pyramid a two dimensional array so we
# can easily turn it into a graph with nodes and edges.
pyramid = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 04, 82, 47, 65],
[19, 01, 23, 75, 03, 34],
[88, 02, 77, 73, 07, 63, 67],
[99, 65, 04, 28, 06, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]]

map = {}
index = 0
indexSum = 0
largestDistance = 0

# Creates a graph-structure for the pyramid
for i in xrange(len(pyramid)):
    indexSum += len(pyramid[i])
    for j in xrange(len(pyramid[i])):
        if i+1 < len(pyramid):
            edges = {}
            edges[indexSum + j ] = pyramid[i+1][j]
            edges[indexSum + j + 1] = pyramid[i+1][j+1]
            map[index] = edges
            index += 1

distances = djikstra(map, 0, 75)

# Get largest-valued node.
for i in distances:
    if distances[i] > largestDistance:
        largestDistance = distances[i]

print largestDistance
