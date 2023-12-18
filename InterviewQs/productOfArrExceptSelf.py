def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    answer = []
    size = len(nums)
    for i in range(size):
        prod = 1
        nums_without_i = nums[:i] + nums[(i+1):]
        n = 0
        print(nums_without_i)
        while prod and n<(size-1):
            prod = prod * nums_without_i[n]
            n += 1
        answer += [prod]
    return answer 

print(productExceptSelf([1,2,3,4]))