# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoSorted(a, b) -> ListNode | None:
            a1 = a
            b1 = b

            dummy = ListNode(0)
            curr = dummy

            while a1 and b1:
                if a1.val <= b1.val:
                    next_node = a1
                    a1 = a1.next
                else:
                    next_node = b1
                    b1 = b1.next

                curr.next = next_node
                curr = curr.next
            
            curr.next = a1 if a1 else b1
            return dummy.next

        
        if len(lists) == 0:
            return None
            
        sol = lists[0]

        for i in range(1, len(lists)):
            sol = mergeTwoSorted(sol, lists[i])
        
        return sol


        
        