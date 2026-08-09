# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        def reverse(curr):
            prev = None

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev


        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        for _ in range(left-1):
            prev = prev.next
        
        sublist_head = prev.next
        sublist_tail = sublist_head
        for _ in range(right-left):
            sublist_tail = sublist_tail.next
        
        head2 = sublist_tail.next
        sublist_tail.next = None
        prev.next = reverse(sublist_head)
        sublist_head.next = head2
        return dummy.next


        
