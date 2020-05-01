
### maybe take a look at the following article in here, it can be useful, there are some insight in the analysis in there, take it with grain of salt https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/yi-wen-jie-jue-4-dao-sou-suo-xuan-zhuan-pai-xu-s-3/



### this is a practice round
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l = 0
        r = len(nums)-1
        
        while l<=r:
            
            mid = (l+r)//2
            if nums[mid] == target or nums[l] == target or nums[r] == target: return True
            if nums[mid] == nums[l]:
                l += 1
                continue
            if nums[mid] == nums[r]:
                r -= 1
                continue
            if nums[mid] < nums[r]:
                if nums[mid] < target < nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            elif nums[mid] > nums[r]:
                if nums[l] < target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
        return False
                    
