class Solution:

    def removeDuplicateLetters(self, s: str) -> str:
        dix_last_seen = {c : i for i,c in enumerate(s)}
        out = ""
        i = 0
        for i,char in enumerate(s):

            if char in out:
                continue

            while out and char < out[-1] and i<dix_last_seen[out[-1]]:
                out = out[:-1]

            out += char
            
        return out
    
    
"""
Possible optimizations:
- looking for used vars in set() instead of the returning varialble ('out')
- list methods might be faster

-> This was my first Daily Challenge. I needed help
"""