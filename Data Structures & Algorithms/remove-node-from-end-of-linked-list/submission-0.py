# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def countNodes(self, head: Optional[ListNode]) -> int:
        count = 0
        while head:
            count += 1
            head = head.next
        
        return count


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count = self.countNodes(head)


        dummy = ListNode()
        first = dummy

        if (count - n == 0):
            first.next = head.next
            return dummy.next
        first.next = head
        i = 0
        while i < (count - n - 1):
            head = head.next
            i+=1
        
        head.next = head.next.next

        return dummy.next


        



    
