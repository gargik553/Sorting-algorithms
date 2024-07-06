"""
@author: Gargi Kshirsagar
@goal: To implement and test the quick sort algorithm
"""

import sys


def get_list(N: int) -> list[int]:

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

    for i in range(len(L)):
        print(f'L[{i}]:{L[i]}')


def partition(L: [int], p: int, r: int) -> int:

    pivot = L[r]
    i = p - 1
    for j in range(p, r):
        if L[j] <= pivot:
            i = i + 1
            L[i], L[j] = L[j], L[i]
    L[i + 1], L[r] = L[r], L[i + 1]
    return (i + 1)


def quick_sort(L: [int], p: int, r: int):
    if p < r:
        if type(L) != list:
            raise TypeError("L must be a list of integers")
        if len(L) == 0:
            raise ValueError("L must be a non-empty list of integers")

        q = partition(L, p, r)
        quick_sort(L, p, q - 1)
        quick_sort(L, q + 1, r)


def main():
    N = int(input("Enter the size of the list:(greater than 2):"))
    if N < 2:
        print("Bad size")
        sys.exit(-1)

    L = get_list(N)
    show_list(L, "Before sort:")
    quick_sort(L, 0, len(L) - 1)
    show_list(L, "After sort:")


main()