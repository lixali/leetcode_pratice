

### the following is iterative solution......
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        stack = []
        seen = []
        row = len(image)
        col = len(image[0])
        stack.append((sr,sc))
        oldcolor = image[sr][sc]
        
        while stack:
            x,y = stack.pop()
            
            if (x,y) not in seen and image[x][y] == oldcolor:
                image[x][y] = newColor
                seen.append((x,y))
                if x-1>=0: stack.append((x-1,y))
                if x+1<row: stack.append((x+1,y))
                if y-1>=0: stack.append((x,y-1))
                if y+1<col: stack.append((x,y+1))
        return image
        
        
        
        
        
        
        
        
        
        
        
        
        
        



'''
### the following is recursive solution...
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        seen = []
        def helper(x, y, oldcolor, newcolor):
            ## nonlocal seen
            if x<0 or y<0 or x >= row or y >= col or image[x][y] != oldcolor or (x,y) in seen: return
            
            image[x][y] = newcolor
            seen.append((x,y))
            
            helper(x-1,y, oldcolor, newcolor)
            helper(x+1,y, oldcolor, newcolor)
            helper(x,y-1, oldcolor, newcolor)
            helper(x,y+1, oldcolor, newcolor)
            
        helper(sr,sc,image[sr][sc], newColor)
        return image

'''
