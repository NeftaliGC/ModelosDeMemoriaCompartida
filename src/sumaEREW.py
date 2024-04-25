import threading
import math

def sumaEREW(A):
    n = len(A)
    logn = int(math.log2(n))
    ts = []
    for i in range(1, logn + 1):
        for j in range(1, (int)(a/2)+1):
            t = threading.Thread(target=sumaEREWThread, args=(A, j, i))
            ts.append(t)
            t.start()
    
        for t in ts:
            t.join()

def sumaEREWThread(A, j, i):
    x = (2 * j) % int(math.pow(2, i + 1))
    if (x == 0):
        A[2 * j] += A[int(((2 * j) - 1) - math.pow(2, i))]