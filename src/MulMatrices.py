class MulMatrices:
    @staticmethod
    def print_matrix(matrix):
        for row in matrix:
            print('\t'.join(map(str, row)))
        print()

    @staticmethod
    def multiply_matrices(A, B, n):
        C = np.zeros((n, n, n), dtype=int)

        # Paso 1: Multiplicación de elementos individuales
        def multiply(i, j, k):
            C[i, j, k] = A[i, k] * B[k, j]
            print(f'C[{i},{j},{k}] = A[{i},{k}] * B[{k},{j}] = {C[i, j, k]}')

        threads = []
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    thread = threading.Thread(target=multiply, args=(i, j, k))
                    threads.append(thread)
                    thread.start()

        for thread in threads:
            thread.join()

        # Paso 2: Suma de elementos para obtener el resultado final
        for L in range(1, int(np.log2(n)) + 1):
            for i in range(n):
                for j in range(n):
                    for k in range(1, n // 2 + 1):
                        if (2 * k) % 2 ** L == 0:
                            C[i, j, 2 * k - 1] += C[i, j, 2 * k - 1 - 2 ** (L - 1)]
                            print(f'C[{i},{j},{2 * k - 1}] += C[{i},{j},{2 * k - 1 - 2 ** (L - 1)}]')

        return C
