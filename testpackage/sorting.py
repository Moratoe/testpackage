def bubble_sort(items):
    "Returns array of items, sorted in ascending order"
    """ Implementation of bubble sort """
    bubble = items.copy() # in place protection on items
    for i in range(len(bubble)):
        for j in range(len(bubble)-1-i):
            if bubble[j] > bubble[j+1]:
                bubble[j], bubble[j+1] = bubble[j+1], bubble[j]     # Swap!

    return bubble




def merge_sort(items):
    '''Return array of items, sorted in ascending order'''
    len_sort = len(items)
    # Base case. A list of size 1 is sorted.

    if len_sort == 1:
        return items
    # Recursive case. Find midpoint of list
    midp = int(len_sort / 2)

    index1 = merge_sort(items[:midp]) # divide list into two halves
    index2 = merge_sort(items[midp:]) # call merge_sort function on each half of list

    return merge(index1, index2)

def quick_sort(items):
    '''Return array of items, sorted in ascending order'''
    if len(items) == 1 or len(items) == 0:
        return items
    else:
        pivot = items[0]
        i = 0
        for j in range(len(items)-1):
            if items[j+1] < pivot:
                items[j+1],items[i+1] = items[i+1], items[j+1]
                i += 1
        items[0],items[i] = items[i],items[0]
        first_part = quick_sort(items[:i])
        second_part = quick_sort(items[i+1:])
        first_part.append(items[i])
        return first_part + second_part
