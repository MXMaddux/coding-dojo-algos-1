class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root:
            runner = self.root
            while runner:
                if data > runner.data:
                    if runner.right:
                        runner = runner.right
                    else:
                        runner.right = Node(data);
                        return self
                else:
                    if runner.left:
                        runner = runner.left
                    else:
                        runner.left = Node(data);
                        return self
        self.root = Node(data)
        return self

    def contains(self, data):
        runner = self.root
        while runner:
            if data == runner.data:
                return True
            if data < runner.data:
                if not runner.left:
                    return False
                runner = runner.left
            else:
                if not runner.right:
                    return False
                runner = runner.right
        return False

    def min(self):
        runner = self.root
        min = self.root.data
        while runner.left:
            if runner.left.data < min:
                min = runner.left.data
            runner = runner.left
        return min

    def max(self):
        runner = self.root
        max = self.root.data
        while runner.right:
            if runner.right.data > max:
                max = runner.right.data
            runner = runner.right
        return max

    def size(self):
        if self.root == None:
            return 0
        def size_help(runner):
            if not runner:
                return 0
            return 1 + size_help(runner.left) + size_help(runner.right)
        return size_help(self.root)

    def is_empty(self):
        if self.root:
            return False
        return True

tree = BST()
tree.add(10).add(20).add(5).add(7).add(21).add(2).add(9).add(17).add(6).add(4)
print(tree.size())
