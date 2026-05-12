# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.rightview = []
        def deepright(node,depth):
            if node is None:
                return
            if depth == len(self.rightview):
                self.rightview.append(node.val)
            deepright(node.right, depth + 1)
            deepright(node.left,  depth + 1)
            return
        deepright(root,0)
        return self.rightview
        