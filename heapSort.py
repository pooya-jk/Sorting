__author__ = 'Pooya Koshanfar'

"""
implementing heapsort
"""

import math


def heap_sort(array):
    """
    sorting the array with heap
    """

    build_max_heap(array)
    A_ = []
    for i in range((len(array)), 0, -1):
        A_.append(array[0])
        (array[0], array[i - 1]) = (array[i - 1], array[0])
        del array[i - 1]
        maxheapify(array, 0)
    return A_


def build_max_heap(array):
    """
    bulding the max heap
    """

    for i in range(int((math.floor(len(array) / 2))), -1, -1):
        maxheapify(array, i)


def maxheapify(array, i):
    """
    placing the specified index in the right palce
    """

    l = left(array, i + 1)
    r = right(array, i + 1)
    if l == 0 and r == 0:
        return
    largest = i
    if l != 0:
        if l - 1 <= len(array) and array[l - 1] > array[largest]:
            largest = l - 1
    if r != 0:
        if r - 1 <= len(array) and array[r - 1] > array[largest]:
            largest = r - 1
    if largest != i:
        (array[largest], array[i]) = (array[i], array[largest])
        maxheapify(array, largest)


def left(array, index):
    """
    finding the left node in the binary tree
    """

    l = (2 * index)
    if len(array) >= l:
        return l
    else:
        return 0


def right(array, index):
    """
    finding the right node in the binary tree
    """

    r = (2 * index) + 1
    if len(array) >= r:
        return r
    else:
        return 0


def parent(array, index):
    """
    finding the parent node in the binary tree
    """
    return math.floor(index / 2)


if __name__ == '__main__':
    pass
else:
    pass
