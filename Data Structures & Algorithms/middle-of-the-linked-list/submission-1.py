# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:


        curr = head
        lag = head

        while curr and curr.next:
            curr = curr.next
            if curr:
                curr = curr.next
            lag = lag.next
        return lag
        