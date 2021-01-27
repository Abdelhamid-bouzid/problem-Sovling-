'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:

Could you solve the problem in O(1) extra memory space?
You may not alter the values in the list's nodes, only nodes itself may be changed.
 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
Example 4:

Input: head = [1], k = 1
Output: [1]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        if head == None or k==1: 
            return head
        
        dummy      = ListNode(0)
        dummy.next = head
        start      = dummy  #  start =0.   Given this linked list: 1->2->3->4->5    #    For k = 2, you should return: 2->1->4->3->5
        while start.next:
            end = start                                # end = 0
            for i in range(k-1):
                end = end.next                         # end = 1
                if end.next == None: 
                    return dummy.next
            (start.next, start)=self.reverse(start.next, end.next)  #  (start.next=3, start=1)=self.reverse(start.next=1, end.next=2)
        return dummy.next
        
    def reverse(self, start, end):
        dummy = ListNode(0)
        dummy.next = start
        while dummy.next != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = dummy.next
            dummy.next = tmp
            #start.next, start.next.next, dummy.next = start.next.next, dummy.next, start.next
            # The above line is wrong! But WHY?
        return (end, start)
