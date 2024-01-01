#print(field)
# { (0,0): 'S', (0, 1): '7', (1,0): 'L', (1:1): 'J'}
# def find_connected(path):
# look at all directions
# if connected and not in path already,
# or s and len(path) > 0,
    # add to result
import sys
sys.setrecursionlimit(100000)

class Graph:
    def __init__(self, vertices, start):
        self.V = vertices

        self.start = start
        self.graph = {}

    def addEdge(self, v, w):
        if v in self.graph:
            self.graph[v].append(w)
        else:
            self.graph[v] = [w]
        if w in self.graph:
            self.graph[w].append(v)
        else:
            self.graph[w] = [v]
    def is_cyclic_util(self, v, visited, parent, count):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                if self.is_cyclic_util(i, visited, v, count + 1):
                    return True
            elif parent != i:
                print(f"result: {(count + 1) / 2}")
                return True
        return False

    def is_cyclic(self):
        visited = {}
        for coord in self.graph.keys():
            visited[coord] = False

        if self.is_cyclic_util(self.start, visited, -1, 0):
            print("found a cycle")


def is_north_connected(cur, goal):
    return cur in ('S', 'J', '|', 'L') and goal in ('|', '7', 'F')
def is_south_connected(cur, goal):
    return cur in ('S', '7', '|', 'F') and goal in ('|', 'J', 'L')
def is_east_connected(cur, goal):
    return cur in ('S', '-', 'F', 'L') and goal in ('-', 'J', '7')
def is_west_connected(cur, goal):
    return cur in ('S', '-', 'J', '7') and goal in ('-', 'F', 'L')

# inp: [(0,0),(1,0)]
# out: [(1,1)]
def find_next(cur):
    north = (cur[0] - 1, cur[1])
    south = (cur[0] + 1, cur[1])
    east = (cur[0], cur[1] + 1)
    west = (cur[0], cur[1] - 1)
    result = []
    if north in field:
        if is_north_connected(field[cur], field[north]):
            result.append(north)
    if south in field:
        if is_south_connected(field[cur], field[south]):
            result.append(south)
    if east in field:
        if is_east_connected(field[cur], field[east]):
            result.append(east)
    if west in field:
        if is_west_connected(field[cur], field[west]):
            result.append(west)
    return result

# paths = [[(S,0,0)]]

f = open("input", "r")
lines = f.readlines()
# parse input to field
field = {}
for y, line in enumerate(lines):
    line = line.strip()
    for x, letter in enumerate(line):
        if letter == 'S':
            start = (y,x)
        field[(y,x)] = letter

graph = Graph(list(field.keys()), start)
print()
for key, value in field.items():
    if value != '.':
        adjs = find_next(key)
        for adj in adjs:
            graph.addEdge(key, adj)
graph.is_cyclic()
