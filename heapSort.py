import math


def build_heap(A):
    for i in range(int((math.floor(len(A)/2))),-1,-1):
        print(i)
        maxheapify(A,i)


def maxheapify(A ,i):
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
    l = (2*index)
    if len(A) > l:
        return l
    else:
        return 0

def right(A,index):
    r = (2 * index)+1
    if len(A) > r:
        return r
    else:
        return 0
"""    
def parent(A,index):
    return math.floor(index/2)
"""
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
maxheapify(a,0)
print(a)
build_heap(a)
print(a)
