from threading import Thread

def merge_sort_pram(L, n):
    if n >= 2:
        threads = [
            Thread(target=merge_sort_pram, args=(L, n // 2)),
            Thread(target=merge_sort_pram, args=(L, n - n // 2))
        ]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        odd_even_merge_pram(L, n)

def odd_even_merge_pram(L, n):
    if n == 2:
        if L[0] > L[1]:
            interchange(L, 0, 1)
    else:
        odd = [0] * (n // 2)
        even = [0] * (n // 2)
        odd_even_split(L, odd, even, n)

        threads = [
            Thread(target=odd_even_merge_pram, args=(odd, n // 2)),
            Thread(target=odd_even_merge_pram, args=(even, n // 2))
        ]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        for i in range(0,n // 2):
            L[2 * i] = odd[i]
            L[2 * i + 1] = even[i]

        for i in range(1, n // 2):
            if L[2 * i] < L[2 * i - 1]:
                interchange(L, 2 * i, 2 * i - 1)

        odd.clear()
        even.clear()

def interchange(L, a, b):
    L[a], L[b] = L[b], L[a]

def odd_even_split(L, left, right, n):
    for i in range(n // 2):
        left[i] = L[2 * i]
        right[i] = L[2 * i + 1]