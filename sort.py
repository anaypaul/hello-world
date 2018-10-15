def merge(arr, low, mid, high):
    l_len = mid - low + 1
    r_len = high - mid
    left = [0]*(l_len)
    right = [0]*(r_len)
    for i in range(l_len):
        left[i] = arr[low + i]
    for j in range(r_len):
        right[j] = arr[mid + 1 + j]
    i = 0
    j = 0
    k = low
    while(i<l_len and j<r_len):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1
    while(i<l_len):
        arr[k] = left[i]
        i+=1 
        k+=1
    while(j<r_len):
        arr[k] = right[j]
        j+=1
        k+=1

def mergesort(arr, low, high):
    if(low<high):
        mid = (low + high)/2 
        mid = int(mid)
        mergesort(arr,low, mid)
        mergesort(arr,mid+1, high)
        merge(arr, low, mid, high)