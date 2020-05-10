
### Look at the explanation in here........ It shows a tree structure DP illustration...

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        seen = defaultdict(int)
        def helper(rest, seen):
            if  rest < 0 : return 0
            if rest == 0: 
                #count += 1
                return 1            
            count = 0
            for num in nums:
                if rest not in seen: 
                    count += helper(rest-num, seen) ## the count is calculated when trickling up..... passing the count down doesn't make any sense........ 
                    #seen[rest] = count
                else:
                    count = seen[rest]
            if rest not in seen: seen[rest] = count

            return count
                
        res=helper(target, seen)
        return res
            
