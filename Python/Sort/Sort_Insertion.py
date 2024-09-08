def sort_insert(arr):
    n=len(arr)
    
    for i in range(1,n):
        print("i:",i,"arr:",arr)
        
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    print()
    return arr
arr=[23,1,10,5,2]
print(sort_insert(arr))