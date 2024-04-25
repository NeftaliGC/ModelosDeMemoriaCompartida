import threading
import math

# Función para multiplicar matrices C = A * B
def multiply_matrices(A, B, C, n, start, end):
    for i in range(start, end):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

# Función para realizar el paso 2 del algoritmo
def step_two(C, n, L):
    for i in range(n):
        for j in range(n):
            for k in range(n // 2):
                if (2 * k) % (2 ** L) == 0:
                    C[i][j][2 * k] += C[i][j][2 * k - 2 ** (L - 1)]

# Función principal para el algoritmo MatMultCREW
def MatMultCREW(A, B, C, n):
    # Paso 1: Multiplicar matrices
    threads = []
    for i in range(n):
        thread = threading.Thread(target=multiply_matrices, args=(A, B, C, n, i, i+1))
        thread.start()
        threads.append(thread)

    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()

    # Paso 2: Realizar la suma acumulativa
    for L in range(1, int(math.log2(n)) + 1):
        step_two(C, n, L)