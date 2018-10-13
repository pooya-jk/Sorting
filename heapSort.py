def maxheapify(A ,i):
    l = left(i)
    r = right(i)
    largest = i
    if l <= A.heap_size() and A[l] > A[largest]:
        largest = l
    if r <= A.heap_size() and A[r] > A[largest]:
        largest = r
    if largest != i:
        (A[largest],A[i]) = (A[i],A[largest])
        maxheapify(A,largest)


def left(i):
    pass

def right(i):
    pass

def heap_size() :
    pass