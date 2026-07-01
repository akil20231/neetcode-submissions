# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        max_sum = 0

        place = 1
        while l1:
            max_sum += l1.val * place
            place *= 10
            l1 = l1.next

        place = 1
        while l2:
            max_sum += l2.val * place
            place *= 10
            l2 = l2.next
        
        dummy = ListNode()
        curr = dummy

        if max_sum == 0:
            return ListNode(0)
        
        while max_sum > 0:
            digit = max_sum % 10
            curr.next = ListNode(digit)
            curr = curr.next

            max_sum //= 10
        
        return dummy.next
        
        

