# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode):
        un = []
        ori0 = ListNode(0)
        ori  = ori0
        while head is not None:
            if head.val not in un:
                un.append(head.val)
                ori.next  = ListNode(head.val)
                ori  = ori.next
                
            head = head.next
        return ori0.next
