#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    from collections import defaultdict
    
    grafo = defaultdict(list)
    for u, v in zip (t_from, t_to):
        grafo[u].append(v)
        grafo[v].append(u)

    corter_posibles = 0
    
    def dfs(nodo, padre):
        
        nonlocal corter_posibles
        count = 1 
        
        for vecino in grafo[nodo]:
            if vecino != padre:
                tam_vecino = dfs(vecino, nodo)
                if tam_vecino % 2 == 0:
                    corter_posibles += 1
                else:
                    count += tam_vecino
                    
        return count
    
    dfs(1, -1)
    return corter_posibles
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
