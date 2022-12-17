# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional


"""Definition for singly-linked list."""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        aux = result = ListNode()
        
        while list1 and list2:
            if list1.val == list2.val: # advance both pointers
                aux.next = list1
                list1, aux = list1.next, list1
                aux.next = list2
                list2, aux = list2.next, list2
            elif list1.val < list2.val:
                aux.next = list1
                list1, aux = list1.next, list1
            else:
                aux.next = list2
                list2, aux = list2.next, list2
        
        # add remaining
        aux.next = list1 or list2
        
        return result.next