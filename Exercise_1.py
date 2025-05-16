# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1

# Time Complexity:
# Best case: O(1), element found at middle
# Worst case: O(log n)
# Space Complexity: O(1)

def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2  # Calculate middle index

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore the left
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore the right
        else:
            r = mid - 1

    # If we reach here, then the element was not present
    return -1
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print(f"Element is present at index {result}")
else: 
    print("Element is not present in array")
