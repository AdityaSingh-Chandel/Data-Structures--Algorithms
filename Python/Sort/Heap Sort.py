'''
def buildHeap(arr):
    n = len(arr)
    # Build a max heap by heapifying from the bottom up
    for i in range((n - 2) // 2, -1, -1):
        maxHeapify(arr, n, i)
    
def maxHeapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    # Compare left child
    if left < n and arr[left] > arr[largest]:
        largest = left
    # Compare right child
    if right < n and arr[right] > arr[largest]:
        largest = right
    # Swap and continue heapifying if root is not the largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    # Step 1: Build a max heap
    buildHeap(arr)
    print("Initial max heap:", arr)
    # Step 2: Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify the reduced heap
        maxHeapify(arr, i, 0)
        print("i:", i, "arr:", arr)
    return arr

'''
def buildHeap(arr):
    n=len(arr)
    for i in range((n-2)//2,-1,-1):
        maxHeapify(arr,n,i)
    
        
def maxHeapify(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        maxHeapify(arr,n,largest)
    

def heapSort(arr):
    n=len(arr)
    buildHeap(arr)
    print(arr)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        maxHeapify(arr,i,0) 
        print("i:",i,"arr:",arr)
    return arr 


arr=[78,23,4,67,8,34,12]  
#print(buildHeap(arr))  
print(heapSort(arr))