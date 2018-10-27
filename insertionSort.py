__author__ = 'Pooya Kooshanfar'

"""
implementing insertionsort
"""


def insertion_sort(array):
    """
    sorting with insertion sort
    :param array: array
    :return:
    """
    for i in range(1, len(array)):
        print(i)
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


if __name__ == '__main__':
    pass
else:
    pass
