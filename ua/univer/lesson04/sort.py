def bubblesort(arr):
    count = 0
    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):
            count+=1
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] =temp
    print("count =",count)

def partion(arr,start, end):
    marker = start
    for i in range (start, end+1):
        if arr[i]<=arr[end]:
            temp = arr[marker]
            arr[marker] = arr[i]
            arr[i] = temp
            marker+=1
    print(marker)
    return marker-1


def quick_sort(arr, start, end):
    if start>=end:
        return
    pivot = partion(arr,start, end)
    quick_sort(arr, start, pivot-1)
    quick_sort(arr, pivot+1, end)

def qsort(L):
    if L: return qsort([x for x in L[1:] if x<L[0]]) + L[0:1] + qsort([x for x in L[1:] if x>=L[0]])
    return []

if __name__ == '__main__':
    arr1 = [x for x in range(10) if x%2 == 0]
    print(arr1)
    arr = [10,2,44,2,4,2,4,6,7]
    bubblesort(arr)
    #quick_sort(arr,0,len(arr)-1)
    print(arr)