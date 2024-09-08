def sort_select(arr):
    n=len(arr)
    
    for i in range(n-1):
        print("i:",i,"arr:",arr)
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                #swap
                arr[j],arr[min_idx]=arr[min_idx],arr[j]
    return arr
arr=[23,1,10,5,2]
print(sort_select(arr))