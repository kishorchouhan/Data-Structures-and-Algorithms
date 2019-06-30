"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def quicksort(array, low, high):
    if low >= high:
        return array
    
    pivot_position = low
    current = low
    pivot = array[high]
    
    while current < high :
        if array[current] < pivot:
            temp = array[current]
            array[current] = array[pivot_position]
            array[pivot_position] = temp
            pivot_position += 1
            current += 1
        else:
            current += 1

    array[high]  = array[pivot_position]
    array[pivot_position] = pivot

    # partition_index = array.index(pivot)
    # print 'abc'
    # print array
    # print array[partition_index]
    # # sub_array_one = array[:partition_index]
    #sub_array_two = array[partition_index+1:]

    quicksort(array, low, pivot_position - 1)
    quicksort(array, pivot_position + 1, high)

    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
#test = [5, 4, 6, 3, 6, 2, 7, 1, 4, 7, 1, 7, 4]
#test = [1]
#test = [10, 9, 8, 7, 4, 8, 23, 5]
#test = [50,30,10,100,20]
print quicksort(test, 0 , len(test)-1)


"""OR"""
"""
def quicksort(array):
    if len(array) < 2:
        return array
    stack_of_index = []
    # index stores beginning and the end boundaries
    index = (0, len(array) - 1)
    stack_of_index.append(index)
    for index in stack_of_index:
        # first value is the element to compare
        e_index = index[0]
        # second value is the pivot
        pivot_index = index[1]
        # until they cross paths, keep executing the following:
        while pivot_index > e_index:
            pivot = array[pivot_index]
            e = array[e_index]
            if e > pivot:
                array[pivot_index] = e
                array[e_index] = array[pivot_index - 1]
                array[pivot_index - 1] = pivot
                pivot_index -= 1
            else: # it's in the correct side of the pivot, so move on
                e_index += 1
        low = index[0]
        high = index[1]
        if pivot_index > 1 and low < pivot_index - 1:
            stack_of_index.append((low, pivot_index - 1))
        if pivot_index < len(array) -1 and pivot_index + 1 < high:
            stack_of_index.append((pivot_index + 1, high))
    return array
            

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
"""
