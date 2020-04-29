### some explanation can be found in here https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/154-find-minimum-in-rotated-sorted-array-ii-by-jyd/
### also look at the following post https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/er-fen-cha-zhao-by-putvoy584m/



class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        
        while l < r:            
            mid = (l+r)//2
            
            if nums[mid] > nums[r]: ### if nums[mid] > nums[right], mid must be in first asending portion of the list
                l += 1
            elif nums[mid] < nums[l]: ### nums[pivot] < nums[r] will also work
                r = mid
            else:   ### this else is condition is "when it can not determine the smallest number is in which portion of the list"
                r -= 1   ### if l += 1 doesn't work???
                         ### I think the rest of the siuaton will not work is because if nums is 1,2,3 in assending order, l += 1 will get rid of the correct answer, r -= 1 will not; 
        
        return nums[l]
            
        


















'''
### the following code does not pass submission, and the thought process is a scramble and it definitely fail the interview.....
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = None
        def helper(arr, start, end):
            nonlocal res
            mid = (start+end)//2
            print("start and end are", start, end)
            if start == end:
                res = arr[start]
                return
            if start == mid == end-1:
                res = min(arr[start], arr[end])
                return
            if arr[start] == arr[mid] == arr[end]: 
                res = arr[start]
                return
            if arr[start] <= arr[mid] <= arr[end]:
                res = arr[start]
                return
            elif arr[start] == arr[end] and arr[mid] <= arr[start]:
                helper(arr, start+1, mid)
            elif arr[start] == arr[end] and arr[mid] <= arr[end]:
                helper(arr, mid, end)
            elif arr[mid] >= arr[end] and arr[mid]>= arr[start]:
                helper(arr, mid, end)
            
            elif arr[mid] <= arr[start] and arr[mid]<= arr[end]:
                helper(arr, start+1, mid)
        leng = len(nums)
        helper(nums, 0, leng-1)
        return res
'''
