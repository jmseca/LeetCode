class Solution:
    """
    It works, and beats 83% in CPU :D
    Did this all by myself ;)
    """
    
    def isMonotonic(self, nums) :
        if nums[0]>nums[-1]:
            return all( nums[i]>=nums[(i+1)] for i in range(len(nums)-1))
        else:
            return all( nums[i]<=nums[(i+1)] for i in range(len(nums)-1))