class TreeNode:
    def __init__(self, data):
        #  Set node value
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def maxValue(self, a, b):
        if (a > b):
            return a

        return b

    def maxIndependentSet(self, node):
        if (node == None):
            return 0

        a = self.maxIndependentSet(
            node.left) + self.maxIndependentSet(node.right)
        b = 1
        if (node.left != None):
            #  When node left child are not null
            b += self.maxIndependentSet(
                node.left.left) + self.maxIndependentSet(node.left.right)

        if (node.right != None):
            #  When node right child are not null
            b += self.maxIndependentSet(
                node.right.left) + self.maxIndependentSet(node.right.right)

        return self.maxValue(a, b)


def main():
    tree = BinaryTree()
    tree.root = TreeNode(1)
    tree.root.left = TreeNode(3)
    tree.root.left.left = TreeNode(2)
    tree.root.right = TreeNode(10)
    tree.root.right.right = TreeNode(11)
    tree.root.right.left = TreeNode(9)
    tree.root.right.left.left = TreeNode(5)
    tree.root.right.left.right = TreeNode(12)
    tree.root.right.right.right = TreeNode(13)
    tree.root.right.right.right.right = TreeNode(21)

    print(tree.maxIndependentSet(tree.root))
if __name__ == "__main__": main()