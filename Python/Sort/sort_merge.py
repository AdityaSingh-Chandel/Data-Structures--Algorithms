def merge(l_arr,r_arr):
    new=[]
    i,j=0,0
    
    while i<len(l_arr) and j<len(r_arr):
        if l_arr[i]<r_arr[j]:
            new.append(l_arr[i])
            i+=1
        elif l_arr[i]>r_arr[j]:
            new.append(r_arr[j])
            j+=1
        else:
            new.append(r_arr[j])
            j+=1
            new.append(l_arr[i])
            i+=1
    print("New:",new)
    new.extend(l_arr[i:])
    new.extend(r_arr[j:])
    print("New2:",new)
    return new
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    n=len(arr)
    m=n//2
    l_arr=arr[:m]
    r_arr=arr[m:]
    print("BEFORE:::","l_arr:",l_arr,"   r_arr:",r_arr)
    l_arr=merge_sort(l_arr)
    r_arr=merge_sort(r_arr)
    print("After::","l_arr:",l_arr,"   r_arr:",r_arr)
    print()
    return merge(l_arr,r_arr)

#Driver's code/ Calling    
arr=[38,27,43,10]
arr1=[23,1,10,5,2]
print(merge_sort(arr1))

            