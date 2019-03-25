# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []

        stack = [root]
        result = deque()

        while stack:
            result.appendleft([s.val for s in stack])
            old_stack = stack

            stack = []

            for node in old_stack:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return list(result)
