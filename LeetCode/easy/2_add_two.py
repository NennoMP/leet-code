# https://leetcode.com/problems/add-two-numbers/

from typing import Optional


class ListNode:
    """Definition for singly-linked list."""
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result: Optional[ListNode] = ListNode()
        aux: Optional[ListNode] = result
            
        remainder = 0
        while l1 or l2:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            
            remainder, quotient = divmod(val1 + val2 + remainder, 10)
            
            aux.next = ListNode(quotient)
            aux = aux.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        if remainder:
            aux.next = ListNode(remainder)
            aux = aux.next
        
        
        return result
