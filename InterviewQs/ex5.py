#9/66

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    palString = s[0]
    palLen = 1

    for i in range(1,len(s)):
        charR = s[i]

        j = 0
        while ((i-j+1) > palLen):
            #print(f'i = {i}, j = {j}\ns[i] = {s[i]}, s[j] = {s[j]}')
            prev_i = i
            if charR != s[j]:
                j+=1
            else:
                possLen = 0
                prev_j = j
                while s[i]==s[j] and i>=j:
                    possLen = possLen + 1 if i==j else possLen + 2
                    j+=1
                    i-=1
                if i<j and possLen > palLen:
                    palLen = possLen
                    palString = ""
                    for k in range(prev_j,prev_i+1):
                        palString += s[k]
                i = prev_i
                j = prev_j + 1
    return palString


s = "aaaabaaa"

print(longestPalindrome(s))