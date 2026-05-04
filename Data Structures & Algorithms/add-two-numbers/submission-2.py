# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Str, l2Str = "", ""

        while l1:
            l1Str += str(l1.val)

            l1 = l1.next
            
        while l2:
            l2Str += str(l2.val)

            l2 = l2.next
        
        l1Reverse, l2Reverse = l1Str[::-1], l2Str[::-1] 
        l1Int, l2Int = int(l1Reverse), int(l2Reverse)

        resSum = str(l1Int + l2Int)[::-1]

        resList = ListNode(0)
        current = resList

        for char in resSum:
            current.next = ListNode(int(char))
            current = current.next
        
        return resList.next
                        