class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        row = len(matrix)
        col = len(matrix[0])
        
        newarr = [[0]*col for _ in range(row)]
        for i in range(row):   ### nested for loop n*m time complexity
            for j in range(col):
                if i == 0:
                    newarr[i][j] = int(matrix[i][j])
                else: 
                    if matrix[i][j] == "1": newarr[i][j] = int(newarr[i-1][j]) + int(matrix[i][j])
                    else: newarr[i][j] = 0        
        
        def maxhistogram(row):   ### this is the max area of historgram, exact the same approach ... 
            row = [0]+row+[0]
            
            stack = []
            maxarea = 0
            for idx, val in enumerate(row):  ### this is O(n) complexity, n is number of column
                
                while stack and row[stack[-1]] > val:
                    tail = stack.pop()
                    maxarea = max(maxarea, (idx-stack[-1]-1)*row[tail])
                stack.append(idx)
            return maxarea
                            

        
        
        res = 0  
        for row in newarr:  ### O(m) complexity, m is number of row
            res = max(res, maxhistogram(row))
        return res
            
            

                    
        
        
