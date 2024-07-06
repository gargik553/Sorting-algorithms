"""
@author: Gargi Kshirsagar
@goal: To implement and test the insertion sort algorithm
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

    print(msg)
    for i in range(len(L)):
        print(f'L[{i}]:{L[i]}')


def insert_at_sorting_position(L: list[int], N: int) -> None:

    if type(L) != list or type(N) != int:
        raise TypeError("Bad type for input data")
    if N < 2:
        raise ValueError("N must be greater than or equal to 2")
    key = L[N - 1]
    i = N - 2
    while i > -1 and L[i] > key:
        L[i + 1] = L[i]
        i = i - 1
    L[i + 1] = key


def insertion_sort(L: list[int]) -> None:
    
    if type(L) != list:
        raise TypeError("Bad input data")
    if len(L) == 0 or len(L) == 1:
        return None

    N = len(L)
    for i in range(2, N + 1):
        insert_at_sorting_position(L, i)


def main():
    N = int(input("Enter the size of the list:(greater than 2):"))
    if N < 2:
        print("Bad size")
        sys.exit(-1)

    L = get_list(N)
    show_list(L, "Before sort:")
    insertion_sort(L)
    show_list(L, "After sort:")


main()