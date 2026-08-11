# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
  
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            #store the next numbers in our list so we don't lose them 
            nxt = curr.next
            #point it backwards to prev
            curr.next = prev
            #move prev forward
            prev = curr
            #move curr forward as well
            curr = nxt
        #at some point prev becomes the very last thing i.e it beomes the new head so return it
        return prev




