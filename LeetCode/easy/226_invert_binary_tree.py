# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional


"""Definition for a binary tree node."""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""BFS (Breadth-first search) visit solution."""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def bfs_invert(node: Optional[TreeNode]):
            if node is None:
                return 
            
            node.left, node.right = node.right, node.left # Swap

            bfs_invert(node.left)
            bfs_invert(node.right)
            
        bfs_invert(root)
        return root
