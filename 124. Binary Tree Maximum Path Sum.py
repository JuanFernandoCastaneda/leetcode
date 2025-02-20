from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root: Optional[TreeNode]) -> int:
    return pathRec(root)[1]

def pathRec(root: Optional[TreeNode]) -> tuple[int, int]:
    if root == None: return -float("inf"), -float("inf")
    right_beginning_max, right_historic_max = pathRec(root.right)
    left_beginning_max, left_historic_max = pathRec(root.left)
    root_beginning_max = root.val + max(right_beginning_max, left_beginning_max, 0)
    # Assuming we take root, assuming we don't take root, and assuming 
    return root_beginning_max, max(root_beginning_max, right_historic_max, left_historic_max, root.val + right_beginning_max + left_beginning_max)
         