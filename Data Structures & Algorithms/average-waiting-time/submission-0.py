from collections import deque

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        finish = 0
    

        for arrival, order in customers:
            finish = max(finish, arrival) + order
            total += finish - arrival
        
        return total / len(customers)



       
        
        

                

            

            


        