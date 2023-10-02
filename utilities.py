def binary_find(arr, target) -> int:
    """
    A binary search, but can also say in which index* should the target be if it was present in the array
    In the case above, the value returned is negative to indicate that it was not found
    
    All indices are returned +1. This means the output 1 refers to 0. This is to solve the problem where the target does not
    exist, but should in the first position
    """ 
    if not(len(arr)):
        return -1
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2 
        
        if arr[mid] == target:
            # Target found, return its index
            return (mid+1)
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1 
    # Target not found in the array
    if arr[mid]<target:
        return -(mid+2)   
    return -(mid+1)