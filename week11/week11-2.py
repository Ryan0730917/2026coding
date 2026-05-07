#week11-2.py leetcode 236 找到p,q的共同祖先
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a = []  #負責放答案
        def helper(root):
            count = 0 #請問你下面累積幾個p 或 q的 node
            if root==None: return 0 #沒有東西
            if root==p or root==q: count += 1 #找到一個
            count += helper(root.left)
            count += helper(root.right)
            if count==2:
                a.append(root)
            return count
        helper(root)
        return a[0]
