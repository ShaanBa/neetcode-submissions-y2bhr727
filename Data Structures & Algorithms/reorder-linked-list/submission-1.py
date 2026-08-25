# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head
        n = 0


        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
        
        second_half = slow.next

        slow.next = None

        rev = None
        curr = second_half

        while curr:
            rest_of_list = curr.next
            curr.next = rev
            rev = curr
            curr = rest_of_list
        
        first = head 
        second = rev

        while second:
            temp1 = first.next
            temp2 = second.next 
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

        