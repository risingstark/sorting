import random

def merge_sort(l):
    '''(list) -> (list)
    return sorted list using Merge Sort algorithm given unsorted list l
    '''

    if len(l) <= 1:
        return l
    mid = len(l)//2
    left_list = l[:mid]
    right_list = l[mid:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)

def merge(left, right):
    '''(list, list) -> (list)
    return sorted list by comparing and merging given two lists, left and right
    '''

    sorted_list = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                sorted_list.append(left[0])
                left = left[1:]
            else:  # left[0] < right[0]:
                sorted_list.append(right[0])
                right = right[1:]
        elif len(left) > 0 and len(right) == 0:
            sorted_list += left
            break 
        elif len(right) > 0 and len(left) == 0:
            sorted_list += right
            break
    return sorted_list


if __name__ == "__main__":

    unsorted_list = random.sample(range(1, 10),9)
    print(unsorted_list)
    print(merge_sort(unsorted_list))