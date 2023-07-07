class TreeNode:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.data = value

    def insert(self, data):
        # if the node has no value set it to the given value
        if self.data is None:
            self.data = data
            return

        # If the value is already in the tree return
        if self.data == data:
            return

        # if the value is less than the node search the left side recursively
        # until there is an empty spot to insert the new node
        if data < self.data:
            if self.left:
                self.left.insert(data)
                return
            self.left = TreeNode(data)
            return

        # do the same for the right side if the value is greater than the node
        if data > self.data:
            if self.right:
                self.right.insert(data)
                return
            self.right = TreeNode(data)

    def search(self, value):
        # if the value equals the current node return true
        if value == self.data:
            return True

        # if the value is less than the current node search the left side of the tree
        if value < self.data:
            # when it gets to the end of the left side the value is not in the tree
            if self.left is None:
                return False
           # recursive function to search all of the nodes to the left
            return self.left.search(value)

        # do the same for the right if the value is greater than the current node
        if value > self.data:
            if self.right is None:
                return False
            return self.right.search(value)

    # since the left side of the tree contains values smaller than the root
    # we only need to search the left edge nodes for the smallest value
    def minValue(self):
        while self.left is not None:
            self = self.left
        return self.data

    def maxValue(self):
        while self.right is not None:
            self = self.right
        return self.data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()


tree = TreeNode()
tree.insert(10)
tree.insert(25)
tree.insert(86)
tree.insert(98)
tree.insert(45)
tree.insert(65)
tree.insert(85)
tree.insert(21)
tree.insert(32)
tree.insert(62)

tree.printTree()

print("Minimum value: %d" % tree.minValue())
print("Maximum value: %d" % tree.maxValue())
