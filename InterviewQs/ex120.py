def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """

    if not(triangle):
        return 0
    
    prev_sums = [triangle[0][0]]

    for i1 in range(1,len(triangle)):
        print(prev_sums)
        curr_sums = [prev_sums[0]+triangle[i1][0]]
        for i2 in range(1, len(triangle[i1])-1):
            val = triangle[i1][i2]
            curr_sums += [val+min(prev_sums[i2-1], prev_sums[i2])]
        prev_sums = curr_sums + [prev_sums[-1]+triangle[i1][-1]]
        
    return min(prev_sums)


triangle = [[-7],[-2,1],[-5,-5,9],[-4,-5,4,4],[-6,-6,2,-1,-5],[3,7,8,-3,7,-9],[-9,-1,-9,6,9,0,7],[-7,0,-6,-8,7,1,-4,9],[-3,2,-6,-9,-7,-6,-9,4,0],[-8,-6,-3,-9,-2,-6,7,-5,0,7],[-9,-1,-2,4,-2,4,4,-1,2,-5,5],[1,1,-6,1,-2,-4,4,-2,6,-6,0,6],[-3,-3,-6,-2,-6,-2,7,-9,-5,-7,-5,5,1]]

minimumTotal(triangle)