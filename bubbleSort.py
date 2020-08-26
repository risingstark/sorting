def bubbleSort(l):
    '''(list) -> (list)
    Given l is unordered list and return ordered list using bubbleSort Algorithm 
    '''
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1], l[j]
    return l

if __name__ == "__main__":

    l = [5,6,2,1,3,4]
    print(bubbleSort(l))
