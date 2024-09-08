def bubble(arr):
    n=len(arr)
    for i in range(n-1):
        print("i:",i,"arr:",arr)
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                #swap
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=[23,2,10,5,1]
print(bubble(arr))
        