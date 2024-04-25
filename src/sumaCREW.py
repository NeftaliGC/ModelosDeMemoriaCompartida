import threading
import math
import time

def suma_CREW(A, hide_zeros):
    n = len(A)
    logn = int(math.log2(n))
    control = []

    for i in range(n):
        control.append(A[i])
        if hide_zeros and A[i] != 0:
            print(A[i], end=" ")
        elif not hide_zeros:
            print(A[i], end=" ")

    print()

    def calculate(j, pow2_i):
        A[j - 1] = control[j - 1] + control[(j - 1) - pow2_i]

    for i in range(logn + 1):
        pow2_i = 2 ** i
        threads = []
        for j in range(pow2_i + 1, n + 1):
            t = threading.Thread(target=calculate, args=(j, pow2_i))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        for i in range(n):
            control[i] = A[i]
            if hide_zeros and A[i] != 0:
                print(A[i], end=" ")
            elif not hide_zeros:
                print(A[i], end=" ")

        print()
        time.sleep(1)
