from threading import Thread, Lock

def min_thread(L):
    win = [0] * len(L)
    index_min = -1
    lock_obj = Lock()

    def compare(i, j):
        nonlocal win
        if L[i] > L[j]:
            win[i] = 1
        else:
            win[j] = 1

    def search(i):
        nonlocal index_min
        if win[i] == 0:
            with lock_obj:
                index_min = i

    threads = []
    for i in range(len(L)):
        win[i] = 0

    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            t = Thread(target=compare, args=(i, j))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()

    for i in range(len(L)):
        t = Thread(target=search, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return L[index_min]

def sort_thread(L):
    win = [0] * len(L)

    def compare(i, j):
        nonlocal win
        if L[i] > L[j]:
            win[i] += 1
        else:
            win[j] += 1

    threads = []
    for i in range(len(L)):
        win[i] = 0

    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            t = Thread(target=compare, args=(i, j))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()

    sorted_list = [0] * len(L)
    for i in range(len(L)):
        index = win[i]
        sorted_list[index] = L[i]

    L[:] = sorted_list

