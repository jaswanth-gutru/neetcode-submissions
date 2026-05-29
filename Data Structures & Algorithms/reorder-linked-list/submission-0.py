# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow=head
        fast=head
        while fast and fast.next is not None:
            slow=slow.next
            fast=fast.next.next


        prev=None 
        cur=slow.next
        slow.next=None 
        while cur is not None:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next

        first=head
        second=prev
        while second is not None:
            temp1=first.next
            temp2=second.next

            first.next=second
            second.next=temp1

            first=temp1
            second=temp2
            

