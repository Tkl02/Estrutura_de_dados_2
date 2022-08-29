def insertion_sort(arr):
    y=0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key
        y=y+1

    print("movimentos:",y)
  
arr = [5371, 3724, -13805, 16190, 3945] 
insertion_sort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i])