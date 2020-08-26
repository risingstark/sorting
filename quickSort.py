def partition(l, start, end):
    pivot = l[start]
    low = start + 1
    high = end
    done = False
    while not done:
        while low <= high and l[low] <= pivot:
            low += 1
        while low <= high and pivot <= l[high]:
            high -= 1
        if high < low:
            done = True
        else:
            l[low], l[high] = l[high], l[low]
    l[start], l[high] = l[high], l[start]
    return high


def quick_sort(l, start, end):
    if start < end:
        pivot = partition(l, start, end)
        quick_sort(l, start, pivot - 1)
        quick_sort(l, pivot + 1, end)
    return l

if __name__ == "__main__":

    l = [4, 1, 8, 2, 3, 9, 6, 5, 7]
    print(quick_sort(l, 0,len(l)-1))