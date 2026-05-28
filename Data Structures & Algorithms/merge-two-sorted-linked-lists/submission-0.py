# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newlist=ListNode()
        lastnode=newlist
        while list1 and list2 is not None:
            if list1.val<list2.val:
                lastnode.next=list1
                list1=list1.next
            else:
                lastnode.next=list2
                list2=list2.next
            lastnode=lastnode.next
        if list1 is not None:
            lastnode.next=list1
        else:
            lastnode.next=list2
        return newlist.next



        