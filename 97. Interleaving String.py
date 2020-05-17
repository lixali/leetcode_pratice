### I bascally just follow the instruction in https://www.youtube.com/watch?v=ih2OZ9-M3OM

## the gist of algorithm is to check whehter s1[:i] and s2[:j] can construct s3[:i+j]!!!!  It looks at the current i+j-1 index in s3, if it is different than both s1[i-1] and s2[j-1], it can't be contructed; if s3[i+j-1] == s1[i-1] and s[i+j-1] != s2[j-1], it means that there is only 1 way to construct s[:i+j], and it is uing s1[i-1] being last character in s3[i+j-1], and it means that the success of constructing depends on the previous constructon(s2[:j] and s1[:i-1]), and then dp[i][j] will be the same as dp[i-1][j]!!!! The same logic can be inferred in the other scenario when s[i+j-1] == s2[j-1] and s3[i+j-1] != s1[i-1], the success of constructing depends on the previous constructon(s2[:i] and s1[:j-1])

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s3=="" and s1=="" and s2=="": return True
        leng_s1 = len(s1)
        leng_s2 = len(s2)
        leng_s3 = len(s3)
        if leng_s1+leng_s2 != leng_s3: return False
        dp = [[None]*(leng_s2+1) for _ in range(leng_s1+1)]
        
        ## initialize the first row
        for j in range(1, leng_s2+1): 
            if s2[:j] == s3[:j]: 
                dp[0][j] = True
            else: dp[0][j] = False
        ## initialize the first column    
        for i in range(1, leng_s1+1):
            if s1[:i] == s3[:i]:
                dp[i][0] = True
            else: dp[i][0] = False                
                          

        for i in range(1, leng_s1+1):
            for j in range(1, leng_s2+1):
                if s2[j-1] == s3[i+j-1] and s1[i-1] == s3[i+j-1]:
                    if dp[i-1][j] == True or dp[i][j-1] == True:
                        dp[i][j] = True
                    else: dp[i][j] = False
                elif s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j-1]
                elif s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j]
                else: dp[i][j] = False
        
        return dp[-1][-1]
