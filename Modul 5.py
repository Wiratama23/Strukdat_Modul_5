class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            if isinstance(data, list):
                for item in data:
                    if self._insert(self.root, item):
                        print("Data already exists. Cannot insert duplicate data:", item)
            else:
                if self._insert(self.root, data):
                    print("Data already exists. Cannot insert duplicate data:", data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
                return False
            else:
                return self._insert(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
                return False
            else:
                return self._insert(node.right, data)
        else:
            return True
        
    def pre_order(self, node = None):
        if node is None:
            node = self.root
        if node is not None:
            print(node.data, end=" ")
            if node.left is not None:
                self.pre_order(node.left)
            if node.right is not None:
                self.pre_order(node.right)
                
    def in_order(self, node = None):
        if node is None:
            node = self.root
        if node is not None:
            if node.left is not None:
                self.in_order(node.left)
            print(node.data, end=" ")
            if node.right is not None:
                self.in_order(node.right)

    def post_order(self, node = None):
        if node is None:
            node = self.root
        if node is not None:
            if node.left is not None:
                self.post_order(node.left)
            if node.right is not None:
                self.post_order(node.right)
            print(node.data, end=" ")

    def display(self):
        print("Pre-order traversal:")
        self.pre_order()
        print("\nIn-order traversal:")
        self.in_order()
        print("\nPost-order traversal:")
        self.post_order()

# input
tree = BinaryTree()
tree.insert("IP12")
tree.insert("AP31")
tree.insert("AD12")
tree.insert(["IP51","IP90","AD12"])

tree.insert("IP12")
tree.display()