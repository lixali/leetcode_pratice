#### people are able to do all kinds of sorting in here https://leetcode.com/problems/sort-an-array/discuss/276916/Python-bubble-insertion-selection-quick-merge-heap   and https://leetcode.com/problems/sort-an-array/discuss/492042/7-Sorting-Algorithms-(quick-sort-top-downbottom-up-merge-sort-heap-sort-etc.)

#### 7 lins of quicksort in here https://leetcode.com/problems/sort-an-array/discuss/277127/7-line-quicksort-to-write-in-interviews-(Python)


### the following is merge sort......... it is not done in place, should it be done in placed???????
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def divide(arr):
            start = 0
            end = len(arr)-1
            mid = (start+end)//2
            
            arr1 = arr[:mid+1]
            arr2 = arr[mid+1:]
            
            return arr1, arr2
        
        
        def merged(arr1, arr2):
            p1 = 0
            p2 = 0
            merged = []
            while p1 < len(arr1) and p2 < len(arr2): ### this while will not error out evene arr1 or arr2 are empty.....
                if arr1[p1] < arr2[p2]:
                    merged.append(arr1[p1])
                    p1 += 1
                else:
                    merged.append(arr2[p2])
                    p2 += 1
                    
            if p1 <= len(arr1)-1: merged.extend(arr1[p1:])
            if p2 <= len(arr2)-1: merged.extend(arr2[p2:])
            return merged
        
        def helper(nlist):
            
            if len(nlist) ==1: return nlist
            if not nlist: return
            arr1, arr2 = divide(nlist)  
            new1=helper(arr1)
            new2=helper(arr2)
            #print("new1 is", new1)
            #print("new2 is", new2)
            
            new_merged=merged(new1, new2)
            
            return new_merged
        res=helper(nums)
        return res
        
        
            
            
            
                    
                
        
