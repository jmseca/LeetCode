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


def binary_range_find(arr, target_range) -> int:
    """
    Similar to the binary find above, but it works with ranges
    This means that 'arr' is a list of sorted ranges.
    
    For example:
    [[0,10], [15,30], [40,40]]
    """ 
    target = target_range[0]
    if not(len(arr)):
        return -1
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2 
        
        if arr[mid][0] <= target and arr[mid][1] >= target:
            # Target found, return its index
            return (mid+1)
        elif arr[mid][1] < target:
            left = mid + 1
        else:
            right = mid - 1 
    # Target not found in the array
    if arr[mid][0]<target:
        return -(mid+2)   
    return -(mid+1)


def merge_delta_with_sorted(sorted, delta, i):
    '''
    Given a list of sorted deltas ([x,y], with both ints and x<=y) 'sorted'.
    And 'i' the position where a new delta 'delta' should be placed.
    It adds the new delta to the sorted deltas list, merging any existing deltas, if necessary.
    
    For example:
    sorted = [[0,10], [20,30], [35,40]]
    delta = [8,21]
    
    It returns:
    sorted = [[0,30], [35,40]]
    '''
    sorted = sorted[:i] + [delta] + sorted[i:]
    done = False
    while ( (sorted[(i+1):]) and (sorted[i][1] > sorted[(i+1)][0])):
        sorted = sorted[:i] + [[sorted[i][0],max(sorted[i+1][1],sorted[i][1])]] + sorted[(i+2):]
    return sorted