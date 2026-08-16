# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=0
        curr=head
        while curr:
            i+=1
            curr=curr.next
        remove=i-n
        if remove==0:
            return head.next
        curr=head
        for k in range(i-1):
            if (k+1)==remove:
                curr.next=curr.next.next
                break
            curr=curr.next
        return head


        