def selectionSort(l):
    '''(list) -> (list)
    return an ordered list using selectionSort algorithm given the unordered list
    '''

    for i in range(len(l)-1):
        min_spot = i
        for j in range(i+1,len(l)):
            if l[j] < l[min_spot]:
                min_spot = j
        l[i],l[min_spot] = l[min_spot],l[i]
    return l

if __name__ == "__main__":

    l = [1,2,4,3,6,5]
    print(selectionSort(l))