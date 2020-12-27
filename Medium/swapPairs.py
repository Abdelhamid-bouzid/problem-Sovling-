'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head==None:
            return head
        if head.next==None:
            return head
        
        i = 0
        head1 = head
        while head.next:
            p             = head.val
            head.val      = head.next.val
            head.next.val = p
            
            if head.next.next:
                head = head.next.next
            else:
                break
        return head1
