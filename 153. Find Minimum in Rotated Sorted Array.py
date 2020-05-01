### Definitely this question, I need more practice.........
### practice this with leetcode 215 https://leetcode.com/problems/kth-largest-element-in-an-array/
### pratice this question with leetcode 148 https://leetcode.com/problems/sort-list/




### this is a practice round....
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums)-1
        
        while l < r: ### the reason that it is not "while l <=r" is because that there is no need to calculate the final nums[mid] when l == r, because we know that when l == r, it is the answer than we want.... In other question when there is a target, we do want to know if nums[mid] equals to target, that is why we do "while l<r"..... 
            mid = (l+r)//2 
            print("l, r and mid are", l, r, mid)
            if nums[mid] > nums[r]:  ### I have to compare it with nums[r], if I do it with nums[l], it does not work
                l = mid+1  ### nums[]
            else:
            #elif nums[mid] < nums[r]:  ### nums[mid] < nums[l] will not work because "mid" can the same as "l" before it break the while loop(when there are only 2 numbers in the list), but before it break the while loop, mid can not be "r"
                r = mid   ### nums[mid] is less than nums[r], there is a possibility that nums[mid] is the smallest number, mid-1 will knock the it out of the range, 

            #print("l, r and mid are", l, r, mid)        
        return nums[l]
