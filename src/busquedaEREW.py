import threading
import math

def broadcast(A, x):
    A[0] = x
    log = int(math.log2(len(A)))
    for i in range(1, log):
        jInit = int(math.pow(2, i - 1)) + 1
        jEnd = int(math.pow(2, i))
        ts = []
        for j in range(jInit, jEnd):
            t = threading.Thread(target=broadcastParallel, args=(A, i, j))
            ts.append(t)
            t.start()
        
        for t in ts:
            t.join()

def broadcastParallel(A, i, j):
    A[j - 1] = A[j - int(math.pow(2, i - 1))]

def minimo(L):
    n = len(L)
    logMin = int(math.log2(n))
    ts = []
    for j in range(1, logMin):
        iEndMin = int(n / math.pow(2, j) - 1)

        for i in range(0, iEndMin):
            t = threading.Thread(target=minimoThread, args=(L, i, j))
            ts.append(t)
            t.start()
        
        for t in ts:
            t.join()
    return L

def minimoThread(L, i, j):
    index1 = int(math.pow(2, j) * i)
    index2 = int(index1 + math.pow(2, j - 1))
    if (L[index1] > L[index2]):
        temp = L[index1]
        L[index1] = L[index2]
        L[index2] = temp

def busquedaEREW(A, x):

    Temp = []
    for i in range(0, len(A)):
        Temp.append(0)


    t = threading.Thread(target=broadcast, args=(Temp, x))
    t.start()
    t.join()

    ts = []
    for i in range(1, len(A)):
        t = threading.Thread(target=busquedaEREWThread, args=(A, Temp, x, i))
        ts.append(t)
        t.start()
    
    for t in ts:
        t.join()
    
    return minimo(Temp)

def busquedaEREWThread(A, Temp, x, i):
    for i in range(0, len(A)):
        if (A[i] == Temp[i]):
            Temp[i] = i
        else:
            #infinito
            Temp[i] = float('inf')