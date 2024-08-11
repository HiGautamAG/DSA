class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
#creating a binary tree

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(root.left.right.val)