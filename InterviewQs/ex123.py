def printDP(dp):
    for row in dp:
        print(row)
    print()

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    dp = []
    maxs = [0 for _ in prices]
    mins = [0 for _ in prices]

    for i1 in range(len(prices)):
        add_to_dp = []
        for i2 in range(i1,len(prices)):
            add_to_dp += [max(0, prices[i2] - prices[i1])]
        dp+=[add_to_dp]

    for i1 in range(len(prices)-2,-1,-1):
        m = max(dp[i1])
        ms = maxs[i1+1]
        maxs[i1] = max(m,ms)     
    for i1 in range(len(prices)):
        mins[i1] = max([dp[i2][i1-i2] for i2 in range(0,i1+1)])
    
        
    return max(map(lambda x,y: x+y, maxs, mins))


prices = [3,3,5,0,0,3,1,4]
print(maxProfit(prices))