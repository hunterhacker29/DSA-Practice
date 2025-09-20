class Node:
    def __init__(self, data):
        self.data = data
        self.left = None   # use left for smaller values
        self.right = None  # use right for larger values


def searchBST(root, value):
    temp = root
    while temp is not None:
        if temp.data == value:
            print("Found:", value)
            return temp
        elif value < temp.data:
            temp = temp.left
        else:
            temp = temp.right
    print("Not Found:", value)
    return None


# --- Manually constructing the BST from your diagram ---
node9 = Node(9)
node3 = Node(3)
node11 = Node(11)
node2 = Node(2)
node7 = Node(7)
node10 = Node(10)
node15 = Node(15)
node4 = Node(4)
node8 = Node(8)
node14 = Node(14)

# Connect the nodes
node9.left = node3
node9.right = node11

node3.left = node2
node3.right = node7

node7.left = node4
node7.right = node8

node11.left = node10
node11.right = node15

node15.left = node14

# --- Run search ---
searchBST(node9, 10)   # should print "Found: 10"
searchBST(node9, 5)    # should print "Not Found: 5"
