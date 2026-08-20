# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #example 1->2->3->4->//
    def reorderList(self, head: Optional[ListNode]) -> None:
        f = head.next
        s = head
        while f and f.next:
            f = f.next.next 
            s = s.next
        #              s     f
        # here it is 1-2->3->4->//
        
        right = s.next # right side of the list
        # right is 3->4
        #             \

        s.next = None # disconnect the list 
        # s is now 1->2 

        prev = None # reversed right 
        curr = right

        while curr:
            rest = curr.next 
            curr.next = prev
            prev = curr
            curr = rest

        # now we have s = 1->2 and also prev = 4-->3

        first = head
        second = prev


        while first and second:
            rest_first = first.next
            first.next = second
            rest_second = second.next
            second.next = rest_first
            # rest_first.next = rest_second
            first = rest_first 
            second = rest_second

        return second







