
### question: what if there are three different types of steps???


### the following is exact the same structure as combination sum IV, it is more a general solution template using dynamic programming and recursion.....
### The question is what is the template for iterative solution??????
class Solution:
    def climbStairs(self, n: int) -> int:
        seen = defaultdict(int)
        def helper(remain):
            if remain < 0 :return 0
            if remain == 0: return 1
            count = 0
            if remain not in seen:
                count += helper(remain-1)
                count += helper(remain-2)
            else:
                count = seen[remain]
            if remain not in seen: seen[remain] = count
            return count
        res=helper(n)
        return res
'''

### the following code pass the submission, exact the same as fibonacci sequence.....
class Solution:
    def climbStairs(self, n: int) -> int:
        second_prev = 1
        prev = 2
        if n == 1: return 1
        if n==2: return 2
            
        for i in range(3, n+1):
            curr = prev+ second_prev
            second_prev = prev
            prev = curr
        
        return curr
'''
