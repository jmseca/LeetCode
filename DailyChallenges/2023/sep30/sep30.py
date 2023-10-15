class Wrong_Solution1:
    """
    It works, but takes too much time );
    I have to find a way to optimize this
    """
    
    def binary_find(self, arr, target) -> int:
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
    
    def update_good(self, good, first, second):
        # Could optimize, but now will be like this
        for i in range(first+1, second):
            ind = self.binary_find(good, i)
            if ind < 0:
                good = good[:(-ind-1)] + [i] + good[(-ind-1):]
        return good
                
            
    
    
    def find132pattern(self, nums):
        first = 10**6
        second = - 10**6
        good = []
        for num in nums:
            print(good, num, second, first)
            if self.binary_d_find(good, num) > 0:
                return True
            elif num < first:
                first = num
                second = - 10**6
            elif num > second:
                second = num
                good = self.update_good(good, first, second)
        return False
    
    
class Solution2:
    """
    It Works :D
    
    But the runtime is really Bad :(.
    """
    
    def binary_delta_find(self, arr, target_range) -> int:
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


    def merge_delta_with_sorted(self, sorted, delta, i):
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
        i = max(0,i-1)
        done = False
        while ( (sorted[(i+1):]) and (sorted[i][1] > sorted[(i+1)][0])):
            sorted = sorted[:i] + [[sorted[i][0],max(sorted[i+1][1],sorted[i][1])]] + sorted[(i+2):]
        return sorted
    
    def update_good(self, good, first, second):
        ind = self.binary_delta_find(good, [first, second])
        return self.merge_delta_with_sorted(good, [first, second], (abs(ind)-1))
                
    
    
    def find132pattern(self, nums):
        first = 10**10 # The mistake was here xD. Numbers were too small for last test
        second = - 10**10 # The mistake was here xD. Numbers were too small for last test
        good = []
        i = 0
        for num in nums:
            if self.binary_delta_find(good, [num,num]) > 0:
                return True
            elif num < first:
                first = num
                second = - 10**6
            elif num > second:
                second = num
                # If first = n, and second = n+1, then there is no way to have a 132 pattern
                if first+1 <= second-1:
                    good = self.update_good(good, first+1, second-1)
            i+=1
        return False
    
    
    
class OnlineSolution:
    """
    Much more simple. It uses a stack approach, instead of a binary search approach.
    Third represents the third element in the 132 pattern.
    
    Transversing the array from the end to the start.
    The stack stores, in decreasing order, the elements that are greater than the third element.
    We need all these elements in the stack, to update the third element, in case we find a second element greater than stack[-1]
    """
    def find132pattern(self, nums) -> bool:
        stack, third = [], float('-inf')
        
        for num in reversed(nums):
            if num < third:
                return True
            while stack and stack[-1] < num:
                third = stack.pop()
            stack.append(num)
        return False