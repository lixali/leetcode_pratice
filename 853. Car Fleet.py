### there are some nice visulization in here  https://leetcode.com/problems/car-fleet/discuss/255589/Python-Code-with-Explanations-and-Visualization-Beats-95

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position: return 0
        dicSpeed = defaultdict(int)
        
        for i,pos in enumerate(position):
            dicSpeed[pos] = speed[i]
            
        position.sort(reverse=True)
        fleet = 0
        leng = len(position)
        print(dicSpeed)
        print(position)
        time1 = float('-inf')
        for i in range(1, leng):
            time1 = max(time1, (target-position[i-1])/dicSpeed[position[i-1]])  ### time for car ahead of it to arrive distination
            ### max is here because if two car meet, the faster car can't go faster, and the speed will be slowed down. According to this the car fleet time ahead of the current position should be max of time1 and previous car time 
            time2 = (target-position[i])/dicSpeed[position[i]] ### time for curr car to arrive distination
            
            if time2 > time1:   ### it means that the curr car can't catch up the car ahead of it
                fleet += 1
        return fleet+1
