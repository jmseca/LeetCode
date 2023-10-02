class Solution1:
    """
    It works, but there are 95% of people with faster solutions.
    I wonder what they did. 
    But this solutions beats 87% in terms of Mem
    """
    
    def sortArrayByParity(self, nums):
        new_l = []
        for el in nums:
            if el%2: #odd
                new_l = new_l + [el]
            else:
                new_l = [el] + new_l
        return new_l
    
    
class Solution2:
    """
    It works, but wastes more Mem with no CPU improvement
    I thought about this, because Python wouldnt need to resize new_l after some concatenations.
    But those changes in order really mess this up
    """
    
    def sortArrayByParity(self, nums):
        i = 0
        size = len(nums)
        while i<size:
            elem = nums[i]
            if elem%2:
                nums = nums[:i] + nums[(i+1):] + [elem]
                size -= 1
            else:
                i+=1
        return nums
    
class Solution3:
    """
    For this, I looked at the solutions Tab
    It does almost the same as my first, but with List comprehension
    
    I think one problem of Solution1 was concatenating on the right and left
    """
    def sortArrayByParity(self, nums):
        return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 == 1]