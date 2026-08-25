# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeLists(l1, l2):
            dummy = ListNode()
            tail = dummy
    


            while l1 and l2:
                if l1.val >= l2.val:
                    tail.next = l2
                    l2 = l2.next
                    tail = tail.next
                else:
                    tail.next = l1
                    l1 = l1.next
                    tail = tail.next

            if not l1:
                tail.next = l2
            if not l2:
                tail.next = l1

                
            return dummy.next
        result = ListNode()
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]

        M = len(lists) // 2

        left_winner = self.mergeKLists(lists[:M])
        right_winner = self.mergeKLists(lists[M:])

        return mergeLists(left_winner, right_winner)


        