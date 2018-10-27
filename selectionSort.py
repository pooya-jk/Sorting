__author__ = 'Pooya Kooshanfar'

"""
implementing selectionsort
"""


def selection_sort(array):
    """

    :param array:
    sort the given array
    """
    temp = 0
    for i in range(len(array)):
        local_max_index = find_max_by_index(array, temp)
        (array[i], array[local_max_index]) = (array[local_max_index], array[i])
        temp = temp + 1


def find_max_by_index(array, start_index=0):
    """

    :param array:
    :param start_index:
    :return: the index of maximum value in the array
    """
    max_index = start_index
    for i in range(start_index, len(array)):
        if array[i] > array[max_index]:
            max_index = i
    return max_index


if __name__ == '__main__':
    pass
else:
    pass
