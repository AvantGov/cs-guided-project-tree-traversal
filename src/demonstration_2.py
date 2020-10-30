"""
You are given the values from a preorder and an inorder tree traversal. Write a
function that can take those inputs and output a binary tree.

*Note: assume that there will not be any duplicates in the tree.*

Example:
Inputs:
preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]

Output:
    5
   / \
  7  22
    /  \
   13   9
"""

"""
UNDERSTAND:
- we are given two sets of numbers from a in order and preorder traversal 
- with these sets, we should be able to construct a binary search tree 

PLAN:
1. we know that the first item in the preorder traversal is the root 

2. if i = index of root in order
    - everything left of i will be a part of the left subtree
    - everything right of i will be part of the right sub tree 
    (this is applicable if we know 5 is the root, and look at the preorder list)

3. use the lengths of the inorder left/right subtrees to find the preorder left/right subtrees
    preorder_left = [1: 1 + len(inorder_left)] 
    preorder_right = [len(preorder) - len(inorder_right) : len(preorder)] 

4. recurse 
in order to be able to recurse, we need ... 
    - we need in-order and pre-order arrays that will represent the side of the sub tree
        - we can derive these numbers from the preorder sub tree,
        - then analyze the inorder sub tree to further determine the depth of the tree
            - i = index of root in inorder
            - inorder_left = [22, 7] :: inorder_right = [9, 13]
            - recurse on (preorder_left, inorder_left) and recurse on (preorder_right, inorder_right)

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder, inorder):
    # if list is empty, return None 
    in len(preorder) == 0:
        return None

    # defining the beginning of the tree (with a class)
    root = TreeNode()
    root.value = preorder[0]    

    root_index = 0
    while inorder[root_index] != root.value:
        root_index += 1
    
    inorder_left = inorder[:root_index]

    inorder_right = inorder[root_index + 1:]

    preorder_left = [1:1 + len(inorder_left)]
    preorder_right = [-len(inorder_right:)]

    root.left = build_tree(preorder_left, inorder_left)
    root.right = build_tree(preorder_right, inorder_right)

    return root

