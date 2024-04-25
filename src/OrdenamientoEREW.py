import threading

def MergeSortPRAM(L):
    if len(L) >= 2:
        # Dividir la lista en dos partes
        mid = len(L) // 2
        left_half = L[:mid]
        right_half = L[mid:]

        # Llamar a MergeSortPRAM en paralelo para las dos mitades
        thread_left = threading.Thread(target=MergeSortPRAM, args=(left_half,))
        thread_right = threading.Thread(target=MergeSortPRAM, args=(right_half,))
        thread_left.start()
        thread_right.start()

        # Esperar a que ambos hilos terminen
        thread_left.join()
        thread_right.join()

        # Llamar a oddEvenMergePRAM
        oddEvenMergePRAM(L)

def oddEvenMergePRAM(L):
    if len(L) == 2:
        if L[0] > L[1]:
            interchange(L, 0, 1)
    else:
        odd = L[0::2]
        even = L[1::2]
        oddEvenMergePRAM(odd)
        oddEvenMergePRAM(even)
        for i in range(len(odd)):
            L[2*i] = odd[i]
            L[2*i + 1] = even[i]
        for i in range(len(odd) - 1):
            if L[2*i + 1] > L[2*i]:
                interchange(L, 2*i, 2*i + 1)

def interchange(L, i, j):
    L[i], L[j] = L[j], L[i]
