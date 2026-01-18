from collections import deque
class solution:
    def calculateTime(self, tickets, k):
        #Write your code here...
        q = deque()
        time = 0
        for i in range(len(tickets)):
            q.append((i, tickets[i]))
        while q:
            index, value = q.popleft()
            time +=1
            value-=1
            if index==k and value==0:
                return time
            if value>0:
                q.append((index, value))
            
            
            
