# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        dummy = ListNode()
        first = dummy
        l1, l2 = list1, list2

        while l1 and l2:
            if l1.val <= l2.val:
                first.next = l1
                first = l1
                l1 = l1.next
            else:
                first.next = l2
                first = l2
                l2 = l2.next
        
        first.next = l1 if l1 else l2
        return dummy.next


            


        