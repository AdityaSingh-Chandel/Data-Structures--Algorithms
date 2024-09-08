
def partition(arr,low,high):
    pi=arr[high]
    i=low-1
    
    for j in range(low,high):
        if arr[j]<=pi:
            i+=1
            #swap
            arr[i],arr[j]=arr[j],arr[i]
            #i+=1
    #swap
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quick(arr,low,high):
    if low<high:
        p=partition(arr,low,high)
    
        quick(arr,low,p-1)
        quick(arr,p+1,high)
    
    return arr
arr=[23,25,46,12,3,56]
arr1=[10,80,30,90,40,50,70]
print(quick(arr1,0,6))