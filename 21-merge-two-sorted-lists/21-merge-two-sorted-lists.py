# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        currentNode = root
        
        while list1 or list2: 
            if list1 and list2:
                if list1.val < list2.val:
                    currentNode.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    currentNode.next= ListNode(list2.val)
                    list2 = list2.next
            elif list1:
                currentNode.next = ListNode(list1.val)
                list1 = list1.next
            else:
                currentNode.next= ListNode(list2.val)
                list2 = list2.next
            currentNode = currentNode.next
                
        return root.next