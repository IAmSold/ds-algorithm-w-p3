import numpy as np

nodes = ['0', '1', '2', '3', '4', '5', '6']
edges = [('1', '3'), ('3', '4'), ('0', '1'), ('1', '2'), ('0', '2'), ('2', '4'), ('5', '4'), ('6', '5')]

a = np.zeros((len(nodes), len(nodes)))
for ele in edges:
    v, e = ele
    v = int(v)
    e = int(e)
    a[v, e] = 1
    a[e, v] = 1

def adjacentNodes(vertex):
    v = int(vertex)
    for i in range(len(a[v, :])):
        if a[v, i] == 1:
            print((v, i))

def matchingNodes(vertex, edge):
    v = int(vertex)
    e = int(edge)
    if a[v, e] == 1:
        return True
    return -1



print(a)
adjacentNodes('1')
print(matchingNodes('2', '4'))
print(matchingNodes('5', '3'))





