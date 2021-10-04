# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        pre = dummy
        node = head
        while node:
            cur = node
            node = node.next
            if cur.val < pre.val:
                pre = dummy
            while pre.next and cur.val > pre.next.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            
        return dummy.next
