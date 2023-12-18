#Beat 31%

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        jumps_to_end = [0]*size

        for i in range(size-2, -1, -1):
            i_jumps = 10**4 if not(nums[i]) else min(jumps_to_end[(i+1) : min(size,i+1+nums[i])])

            jumps_to_end[i] = i_jumps+1
        

        return jumps_to_end[0]
        
        