# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack=[root]
        result=[]
        while len(stack)>0:
            node=stack.pop()
            result.append(node.val)

            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return result[::-1]
        