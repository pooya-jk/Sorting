__author__ = 'Pooya Koshanfar'


"""
implementing heapsort
"""

import math


def heap_sort(A):
    """
    sorting the array with heap
    """

    build_max_heap(A)
    A_ = []
    for i in range((len(A)),0,-1):
        A_.append(A[0])
        (A[0], A[i-1]) = (A[i-1], A[0])
        del A[i-1]
        maxheapify(A,0)
    return A_


def build_max_heap(A):
    """
    bulding the max heap
    """

    for i in range(int((math.floor(len(A)/2))),-1,-1):
        maxheapify(A,i)


def maxheapify(A ,i):
    """
    placing the specified index in the right palce
    """

    l = left(A,i+1)
    r = right(A,i+1)
    if l == 0 and r == 0:
        return
    largest = i
    if l != 0:
        if l-1 <= len(A) and A[l-1] > A[largest]:
            largest = l-1
    if r != 0:
        if r-1 <= len(A) and A[r-1] > A[largest]:
            largest = r-1
    if largest != i:
        (A[largest],A[i]) = (A[i],A[largest])
        maxheapify(A,largest)


def left(A,index):
    """
    finding the left node in the binary tree
    """

    l = (2*index)
    if len(A) >= l:
        return l
    else:
        return 0


def right(A,index):
    """
    finding the right node in the binary tree
    """

    r = (2 * index)+1
    if len(A) >= r:
        return r
    else:
        return 0


def parent(A,index):
    """
    finding the parent node in the binary tree
    """
    return math.floor(index/2)


if __name__ == '__main__':
    pass
else:
    pass



