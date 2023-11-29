import numpy as np
import json
import random
from qiskit.test.mock import FakeTokyo

triangle = np.array([[0,1,0], [0,0,1], [1,0,0]])
ibmqx4 = np.array([[0,0,0,0,0],[1,0,0,0,0], [1,1,0,0,0], [0,0,1,0,1],[0,0,1,0,0]])
k5 = np.array([[0,1,1,1,1], [1,0,1,1,1], [1,1,0,1,1], [1,1,1,0,1],[1,1,1,1,0]])
ring5 = np.array([[0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1],[1,0,0,0,0]])
ibmqx5 = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                   [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                   [0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0], [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]])

ibmToronto = np.array([[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]] )

ibmTokyo = np.array([[0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0], [0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0], [0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0], 
                     [1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0], [0,1,1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0], [0,1,1,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0], [0,0,0,1,1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0], [0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0], 
                     [0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0], [0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,0,1,1,0,0], [0,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0,1,1,0,0], [0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,0,1,1], [0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1], 
                     [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0], [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0]])

def linearArch(n):
    graph = np.zeros((n,n))
    graph[0][1] = 1
    for i in range(1,n-1):
        graph[i][i+1] = 1
        graph[i][i-1] = 1
    graph[n-1][n-2] = 1
    return graph

def NN_2D(n):
    graph = np.zeros((n * n, n * n))
    for i in range(n):
        graph[i * n][i * n + 1] = 1
        for j in range(1, n - 1):
            graph[i * n + j][i * n + j + 1] = 1
            graph[i * n + j][i * n + j - 1] = 1
        graph[i * n + n - 1][i * n + n - 2] = 1
    for i in range(n):
        graph[i][i + n] = 1
        # row number
        for j in range(1, n - 1):
            graph[j * n + i][j * n + i + n] = 1
            graph[j * n + i][j * n + i - n] = 1
        graph[(n - 1) * n + i][(n - 1) * n + i - n] = 1
    return graph

def twoN(n):
    graph = np.zeros((2 * n,2 * n))
    for i in range(2):
        graph[i * n][i * n + 1] = 1
        for j in range(1, n - 1):
            graph[i * n + j][i * n + j + 1] = 1
            graph[i * n + j][i * n + j - 1] = 1
        graph[i * n + n - 1][i * n + n - 2] = 1
    for i in range(n):
        graph[i][i + n] = 1
        graph[i + n][i] = 1
    return graph

def Sycamore(n):
    graph = np.zeros((n * n, n * n))
    pos = []
    for i in range(int(n / 2)):
        u_l = []
        d_l = []
        for j in range(i * n * 2, i * n * 2 + n * 2):
            if j % 2 == 0:
                u_l.append(j)
            else:
                d_l.append(j)
        pos.append(u_l)
        pos.append(d_l)
    for i in range(n - 1):
        for j in range(n):
            node1 = pos[i][j]
            node2 = pos[i + 1][j]
            graph[node1][node2] = 1
            graph[node2][node1] = 1
        if i % 2 == 0:
            for j in range(1, n):
                node1 = pos[i][j]
                node2 = pos[i + 1][j - 1]
                graph[node1][node2] = 1
                graph[node2][node1] = 1
        else:
            for j in range(0, n - 1):
                node1 = pos[i][j]
                node2 = pos[i + 1][j + 1]
                graph[node1][node2] = 1
                graph[node2][node1] = 1
    return graph

def meshArch(n,m):
    graph = np.zeros((n*m,n*m))
    for i in range(n*m):
        for j in range(n*m):
            if neighbors(i,j,m):
                graph[i][j] = 1
    return graph

def neighbors(i,j,n):
    oneRowOver =  abs(j//n - i//n) == 1
    sameColumn = j % n  == i % n
    columnLeft = j % n  == (i % n - 1)
    columnRight =  (j%n)  == (i % n + 1)
    if (i // n) %  2 == 0:
        return oneRowOver and (sameColumn or columnLeft)
    else:   
        return oneRowOver and (sameColumn or columnRight)

def knockoutNQubits(arr, n):
    newCM = arr
    faulty = random.sample(range(len(arr)), n)
    newCM = np.delete(newCM, faulty, axis=0)
    newCM = np.delete(newCM, faulty, axis=1)
    return 

def tokyo_all_diags():
    graph = np.copy(ibmTokyo)
    for i in range(4):
        for j in range(3):
            topleft = j*5+i
            bottomRight = (j+1)*5+i+1
            graph[topleft][bottomRight] = 1
            graph[bottomRight][topleft] = 1
            topRight = j*5+i+1
            bottomLeft = (j+1)*5+i
            graph[topRight][bottomLeft] = 1
            graph[bottomLeft][topRight] = 1
    return graph

def tokyo_no_diags():
    graph = np.copy(ibmTokyo)
    for i in range(4):
        for j in range(3):
            topleft = j*5+i
            bottomRight = (j+1)*5+i+1
            graph[topleft][bottomRight] = 0
            graph[bottomRight][topleft] = 0
            topRight = j*5+i+1
            bottomLeft = (j+1)*5+i
            graph[topRight][bottomLeft] = 0
            graph[bottomLeft][topRight] = 0
    return graph


# tokyo has (0,1), (0,3), (1,0), (1,2), (2, 1), (2,3)
def tokyo_minus(squareList):
    graph = ibmTokyo
    for (j,i) in squareList:
            topleft = j*5+i
            bottomRight = (j+1)*5+i+1
            graph[topleft][bottomRight] = 0
            graph[bottomRight][topleft] = 0
            topRight = j*5+i+1
            bottomLeft = (j+1)*5+i
            graph[topRight][bottomLeft] = 0
            graph[bottomLeft][topRight] = 0
    return graph

def tokyo_plus(squareList):
    graph = ibmTokyo
    for (j,i) in squareList:
            topleft = j*5+i
            bottomRight = (j+1)*5+i+1
            graph[topleft][bottomRight] = 1
            graph[bottomRight][topleft] = 1
            topRight = j*5+i+1
            bottomLeft = (j+1)*5+i
            graph[topRight][bottomLeft] = 1
            graph[bottomLeft][topRight] = 1
    return graph

def tokyo_drop_worst_n(n, err_rates_map):
    graph = np.copy(ibmTokyo)
    worst_n = dict(sorted(err_rates_map.items(), key=lambda item: item[1], reverse=True)[:2*n]).keys()
    for (u,v) in np.argwhere(graph > 0):
        if (u,v) in worst_n:
            graph[u][v] = 0
            graph[v][u] = 0
    return graph 
                
def generateMQTFile(cm, fname):
    with open(fname, "w") as f:
        f.write(str(len(cm)) + "\n" )
        for (u, v) in np.argwhere(cm>0):
            f.write(str(u) + " " + str(v) + "\n" )


def generateEnfFile(cm, fname): 
    obj = {
        "qubits" : len(cm),
        "registers" : [{"name": "q" , "qubits": len(cm)}],
        "adj" : [ [ { "v" : "q[" + str(v) + "]"} for v in range(len(cm)) if cm[u][v]==1 ]  for u in range(len(cm)) ]
    }
    with open(fname, "w") as f:
        json.dump(obj, f)

        
def tokyo_error_list():
    return list(tokyo_error_map().values()) 

def tokyo_error_map():
    AVG = 0.03130722830688227
    errs = {}
    backend = FakeTokyo()
    props = backend.properties()
    for edge in np.argwhere(ibmTokyo > 0):
        if list(edge) in backend.configuration().coupling_map:
            errs[tuple(edge)]= props.gate_error('cx', edge)
        else:errs[tuple(edge)]= AVG
    return errs

def fake_linear_error_map():
    vals = [ 0.0120651070, 0.0120651070, 0.0219138264,0.0219138264, 0.0353320709,0.0353320709, 0.0434709196,0.0434709196, 0.0446780968, 0.0446780968]
    arch = linearArch(6)
    edges = [tuple(edge) for edge in np.argwhere(arch>0)]
    return dict(zip(edges, vals))

def fake_linear_error_list():
    return list(fake_linear_error_map().values()) 

def write_triq_files(error_map):
    with open("ibmtokyo_T.rlb", 'w') as f:
        f.write(str(len(error_map))+"\n")
        for (edge, error_rate) in error_map.items():
            f.write(str(edge[0]) + " " + str(edge[1]) + " " + str(1-error_rate) + "\n")
    with open("ibmtokyo_M.rlb", 'w') as f:
        f.write("20\n")
        for i in range(20):
            f.write(str(i) + " 1.0" + "\n")
    with open("ibmtokyo_S.rlb", 'w') as f:
        f.write("20\n")
        for i in range(20):
            f.write(str(i) + " 1.0" + "\n")
    
