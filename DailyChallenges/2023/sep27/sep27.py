class Solution1:
    """
    This solution takes too much time. It works, but is not ideal.
    What I do here is make many recursive for loops building the final string that can be used to check
    the kth element
    
    For example, with big params, such as:
    param_1 = "y959q969u3hb22odq595"
    param_2 = 222280369
    It takes a really loooooooong time
    
    So I needed to improve this (And make this less confusing)
    """

    def getKth(self, lst: list, curr: list, k:int, i:int, char: str, lvl: int):
        if curr or (i>=k): 
            for _ in range(curr[1]):

                if len(lst)>0:
                    char, i = self.getKth(lst[:-1],lst[-1], k, i, char, lvl+1)

                if (i>k):
                    break
                
                if (i==k):
                    char = curr[0][0]
                elif (k-i) > len(curr[0]):
                    i+=len(curr[0])
                else:
                    char = curr[0][(k-i-1)]
                    i = k + 1
        return char, i


    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        i = 0
        lst = []
        curr = ""
        while size<k:
            char = s[i]
            if char.isdigit():
                if curr=="":
                    
                    lst[-1][1] *= int(char)
                else:
                    lst += [[curr, int(char)]]
                curr = ""
                size = size*int(char)
            else:
                curr += char
                size+=1
            i+=1
        if curr!='':
            lst += [[curr, 1]]
        if k==1:
            return lst[0][0][0]
        print(lst)
        return self.getKth(lst[:-1] , lst[-1], (k-1), -1, "", 0)[0]
    
    
    
class Solution:
    
    """
    It works!!!
    Really happy beacause this the first problem I solve on LeetCode without looking at the solutions.
    (It is only the 3rd, so it is not that bad)
    
    Here a build a list with the chars and how many times they repeat themselves. For example "ha22vz3c34" turns into:
    [['ha',4],['vz',3],['c',12]]
    And I only build this list as long as I need the chars to find the kth element
    
    Afterward, I keep dividing the "strings" until I find my kth element.
    I know that, if I have a string with size 20, that repeats 4 times, and the k I want is 74, then 
    k will be the (74%20)th element of the string that repeats itself.
    Might be confusing here, without a whiteboard.
    
    But with the values of the list I created above, going right to left, I can now exactly the size of the string that
    repeats itself, and the size of the substrings that repeat themselves on that "main" string.
    """
    
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        i = 0
        lst = []
        curr = ""
        while size<k:
            char = s[i]
            if char.isdigit():
                if curr=="":
                    lst[-1][1] *= int(char)
                else:
                    lst += [[curr, int(char)]]
                    curr = ""
                size = size*int(char)
            else:
                curr += char
                size+=1
            i+=1
        if curr!='':
            return curr[-1]
        while size>=k and k!=0:
            elem = lst[-1]
            size = size//elem[1]
            k = k%size
            size = size - len(elem[0])
            lst = lst[:-1]
        if k==0:
            return elem[0][-1]
        else:
            return elem[0][k-size-1]
        



#This code works, but takes too much time