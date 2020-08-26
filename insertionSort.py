def insertionSort(l):
    '''(list) -> (list)
    return sorted list using insertionSort algorithm given unordered list, l
    '''

    for i in range(1,len(l)):
        j = i - 1
        key = l[i]
        while l[j] > key and j >= 0:
            l[j+1] = l[j]
            j-=1
        l[j+1] = key
    return l

if __name__ == "__main__":

    l = [5,6,2,1,3,4]
    print(insertionSort(l))
