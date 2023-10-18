from node import Node
from binary_tree import BinaryTree

# tree = BinaryTree(Node(9))
# tree.add(Node(5))
# tree.add(Node(11))

# print(tree.head)
# print(tree.head.left)
# print(tree.head.right)

# print("In Order")
# tree.inorder()
# print("\n")
# print("In pre-Oroder")
# tree.preorder()
# print(tree.find(11))

tree = BinaryTree(Node(6))
nodes = [5, 3, 9, 7, 8, 7.5, 12, 11]

for n in nodes:
    tree.add(Node(n))

tree.delete(9)
tree.inorder()
