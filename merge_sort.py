"""
@author: Gargi Kshirsagar
@goal: To implement and test the merge sort algorithm
"""
import sys


def get_list(N:int) -> list[int]:

    from random import randint

    if type(N) != int:
        raise TypeError("N must be an int")
    if N <= 0:
        raise ValueError("N must be postivie ")

    L = []

    starting_number = 0
    ending_number = 1001

    for i in range(N):
        L.append(randint(starting_number, ending_number))

    return L


def show_list(L: list[int], msg: str) -> None:

    print(msg)
    for i in range(len(L)):
        print(f'L[{i}]:{L[i]}')


def merge(L: list[int], p: int, q: int, r: int) -> None:

    N1 = q - p + 1
    N2 = r - q


    L1 = []
    i = 0
    while i < N1:
        L1.append(L[p + i])
        i = i + 1


    L2 = []
    i = 0
    while i < N2:
        L2.append(L[q + 1 + i])
        i = i + 1

    i = 0
    j = 0
    k = 0

    while True:
        if L1[i] <= L2[j]:
            L[p + k] = L1[i]
            k = k + 1
            i = i + 1
            if i == N1:
                while j < N2:
                    L[p + k] = L2[j]
                    k = k + 1
                    j = j + 1
                break

        else:
            L[p + k] = L2[j]
            k = k + 1
            j = j + 1
            if j == N2:
                while i < N1:
                    L[p + k] = L1[i]
                    k = k + 1
                    i = i + 1
                break


def merge_sort(L: list[int], p: int, r: int) -> None:

    if p < r:
        q = (p + r) // 2
        merge_sort(L, p, q)
        merge_sort(L, q + 1, r)
        merge(L, p, q, r)


def main():
    N = int(input("Enter the size of the list:(greater than 2):"))
    if N < 2:
        print("Bad size")
        sys.exit(-1)

    L = get_list(N)
    show_list(L, "Before sort:")
    merge_sort(L, 0, len(L) - 1)
    show_list(L, "After sort:")


main()