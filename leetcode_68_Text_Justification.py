
### this is a pracitce round .... 


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        
        
        ### ["This", "is", "an", "example", "of", "text", "justification."]
        
        def whehterfit(arr, i, j, maxWidth):
            
            leng = 0
            
            for x in range(i, j+1):
                leng += len(arr[x])
            
            leng += (j-i)
            
            if leng <= maxWidth: return True
            return False
        
        def centerJust(arr, i, j, maxWidth):
            if i == j:
                string = arr[i]
                leng = len(string)
                space = maxWidth-leng
                string += " "*space
                return string
            leng = 0
            for x in range(i, j+1):
                leng += len(arr[x])
            
            totalspace = maxWidth-leng
            
            space = totalspace//(j-i)
            remainder = totalspace%(j-i)
            
            string = ""
            
            for x in range(i, j+1):
                if x == j: 
                    string += arr[x]
                    break
                string += arr[x]
                string += " "*space
                if remainder > 0:
                    string += " "
                    remainder -= 1
                    
            return string

        
        def leftJust(arr, i, j, maxWidth):
            string = ""
            
            for x in range(i, j+1):
                if x == j: 
                    string += arr[x]
                    break
                string += arr[x]
                string += " "
            leng = len(string)
            space = maxWidth-leng
            string += " "*space
            return string
        #print(centerJust(words, 0, 2, maxWidth))
        #print(leftJust(words, 6, 6, maxWidth))
        
        i, j = 0, 0
        length = len(words)
        res = []
        while j <= length-1:
        
            if whehterfit(words, i, j, maxWidth) == True and j == length-1: ## last line, needs to leftjust
                curr = leftJust(words, i, j, maxWidth)
                res.append(curr)
                return res
            
            elif whehterfit(words, i, j, maxWidth) == True and j != length-1: ## greedily continue to expand 
                j += 1                
                
            elif whehterfit(words, i, j, maxWidth) == False: ## whetherfit is False
                curr = centerJust(words, i, j-1, maxWidth)
                res.append(curr)
                i = j
        print(res)
        return res
                
                
                
                
                
                
                
                
                
            
            
