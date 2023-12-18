# Beat 52%

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        opp_sorted_citations = sorted(citations, key = lambda x : -x)
        h_index = 0
        for el in opp_sorted_citations:
            if el > h_index:
                h_index+=1
        return h_index