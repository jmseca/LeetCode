# 79/97 (lezz gooooooooo)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        seen = set()
        length = 0
        L, R = 0, 0
        size_s = len(s)

        while R < size_s:
            char = s[R]
            if char not in seen:
                seen.add(char)
            else:
                # No need to check L<R
                while char!=s[L]:
                    seen.remove(s[L])
                    L += 1
                L+=1

            if (R-L+1)>length:
                length = R-L+1

            R += 1 

        return length