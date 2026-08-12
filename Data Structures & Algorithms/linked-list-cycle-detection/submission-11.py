# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        if head is None:
            return False

        if head.next is None:
            return False
        elif head == head.next:
            return True

        while fast and fast.next:
            if (fast.next.next == slow.next):
                return True
            else:
                fast = fast.next.next
                slow = slow.next
        return False

        