# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# Time complexity: Avg - O(n log n), worst - O(n^2)
# Spcae Complexity: O(n)
def partition(arr,low,high):
  
    # Choosing the rightmost element as pivot
    pivot = arr[high]
    i = low - 1  # Index of smaller element

    # Traverse through all elements, compare each with pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1  # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than pivot

    # Swap the pivot element with the element at i+1, so pivot is placed at its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the pivot index

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        # Find pivot element such that arr[pivot] is at correct position
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quickSort(arr, low, pi - 1)  # Sort the left subarray
        quickSort(arr, pi + 1, high)  # Sort the right subarray
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print("%d" %arr[i]),
  
 
