'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        head1 = ListNode(0)
        head2 = head1
        while head!=None:
            if head.val!=val:
                head1.next = ListNode(head.val) 
                head  = head.next
                head1 = head1.next
            else:
                head  = head.next
                
        return head2.next
