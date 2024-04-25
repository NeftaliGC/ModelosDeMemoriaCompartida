import threading

import threading

def merge_sort_pram(L, n):
    if n >= 2:
        t1 = threading.Thread(target=merge_sort_pram, args=(L[:n // 2], n // 2))
        t2 = threading.Thread(target=merge_sort_pram, args=(L[n // 2:], n - n // 2))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        odd_even_merge_pram(L, n)

def odd_even_merge_pram(L, n):
    if n == 2:
        if L[0] > L[1]:
            L[0], L[1] = L[1], L[0]
    else:
        odd = [0] * (n // 2)
        even = [0] * (n // 2)
        odd_even_split(L, odd, even, n)

        t1 = threading.Thread(target=odd_even_merge_pram, args=(odd, n // 2))
        t2 = threading.Thread(target=odd_even_merge_pram, args=(even, n // 2))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        for i in range(n // 2):
            L[2 * i] = odd[i]
            L[2 * i + 1] = even[i]

        for i in range(1, n // 2):
            if L[2 * i] < L[2 * i - 1]:
                L[2 * i], L[2 * i - 1] = L[2 * i - 1], L[2 * i]

def odd_even_split(L, left, right, n):
    for i in range(n // 2):
        left[i] = L[2 * i]
        right[i] = L[2 * i + 1]