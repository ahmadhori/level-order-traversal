from Binary_Search_Trees import BST as bst
from collections import deque


def level_order_traversal(root):
    curr_level_queue = deque()
    next_level_queue = deque()

    curr_level_queue.append(root)
    while len(curr_level_queue) != 0:
        node = curr_level_queue.popleft()
        if node:
            print(node.data)
            next_level_queue.append(node.left)
            next_level_queue.append(node.right)

        if len(curr_level_queue) == 0:
            curr_level_queue = next_level_queue
            next_level_queue = deque()


root = bst.CreateBST()
bst.Insert(root, [100, 50, 200, 25, 75, 350])  # passing list
level_order_traversal(root)
