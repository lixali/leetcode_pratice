### this can be catergorized as prefix even vowels state problem.....

### loop through each character in string, each s[:idx] will have a "vowels" state; if 2 prefix substring have a same vowels state, the substraction of the substring will be a valid substring that has even number of vowels(including 0 number vowels), and by doing max operation for each valid case, we find the max length........... 

### I find some good explanation in here.... 


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        state = defaultdict()
        vowels = set()
        vowels = ("a", "e", "i", "o", "u")
        firststate = 0
        currstate = 0
        maxleng = 0
        for idx,char in enumerate(s):
            
            if char == "a":
                currstate ^= 16
            if char == "e":
                currstate ^= 8
            if char == "i":
                currstate ^= 4
            if char == "o":
                currstate ^= 2
            if char == "u":
                currstate ^= 1
            
            if currstate == firststate: 
                maxleng = max(maxleng, idx+1)
            else:
                if currstate in state:
                    maxleng = max(maxleng, idx-state[currstate])
                else:
                    state[currstate] = idx
        return maxleng
            
