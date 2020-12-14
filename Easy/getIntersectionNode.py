# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        a = headA
        b = headB
        
        while a!=None or b!=None:
            if a!=None:
                a = a.next 
            else:
                headB = headB.next
            
            if b!=None:
                b = b.next 
            else:
                headA = headA.next
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
