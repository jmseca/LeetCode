# Beat 92.33%

def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # Representing indices only as positive
    dangerous_indx = -1
    can_reach_end = True
    for i in range(len(nums)-2, -1, -1):
        if (nums[i] == 0) and (i > dangerous_indx):
            dangerous_indx = i
            can_reach_end = False
        elif ((i + nums[i]) > dangerous_indx) and (not(can_reach_end)):
            dangerous_indx = -1
            can_reach_end = True

    return can_reach_end