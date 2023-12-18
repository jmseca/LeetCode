def printDP(dp):
    for row in dp:
        print(row)
    print()


def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """

    size1, size2 = len(word1), len(word2)

    if not(word1) or not(word2):
        return len(word1) + len(word2)

    dp = [[0 for _ in range(size1+1)] for _ in range(size2+1)]

    # Calculate the dp[0][0] outside the loop and save 2n memory

    found = False
    for i1 in range(1, size1+1):
        if found or word2[0] != word1[i1-1]:
            dp[1][i1] = dp[1][i1-1] + 1
        else:
            found = True
            dp[1][i1] = dp[1][i1-1]
            
    printDP(dp)

    found = False
    for i2 in range(1, size2+1):
        if found or word1[0] != word2[i2-1]:
            dp[i2][1] = dp[i2-1][1] + 1
        else:
            found = True
            dp[i2][1] = dp[i2-1][1]
            
    printDP(dp)


    for i1 in range(2,size1+1):
        for i2 in range(2, size2+1):
            
            if word1[i1-1] == word2[i2-1]:
                dp[i2][i1] = dp[i2-1][i1-1]
            else:
                dp[i2][i1] = min(dp[i2-1][i1], dp[i2][i1-1], dp[i2-1][i1-1]) + 1
    return dp[-1][-1]


word1 = "horse"
word2 = "ros"

print(minDistance(word1, word2))
        