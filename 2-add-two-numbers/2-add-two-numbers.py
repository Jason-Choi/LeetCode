# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        up = 0
        l_sum = ListNode()
        l_sum_0 = l_sum
        tmp = 0
        while l1 != None or l2 != None or up:
            if l1 == None:
                tmp_l1 = 0
            else:
                tmp_l1 = l1.val if l1.val else 0
            if l2 == None:
                tmp_l2 = 0
            else:  
                tmp_l2 = l2.val if l2.val else 0
            tmp = tmp_l1 + tmp_l2 + up
            if tmp > 9:
                up = 1
                tmp = tmp % 10
            else:
                up = 0
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None 
            l_sum.val = tmp
            
            if l1 != None or l2 != None or up:
                l_sum.next = ListNode()
                l_sum = l_sum.next
        return l_sum_0