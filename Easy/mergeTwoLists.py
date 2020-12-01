class Solution:
    def mergeTwoLists(self, l1, l2):
        
        lo = ListNode(0)
        l  = lo
        while (l1 is not None) or (l2 is not None):
            
            if (l1 is not None) and (l2 is not None):
                if l1.val<l2.val:
                    l.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    l.next = ListNode(l2.val)
                    l2 = l2.next
            elif l1 is None:
                l.next = ListNode(l2.val)
                l2 = l2.next
                
            else:
                l.next = ListNode(l1.val)
                l1 = l1.next
                
            l = l.next
        return lo.next
