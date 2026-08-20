class Node:
    def __init__(self, name, time, purpose):
        self.name = name
        self.time = time
        self.purpose = purpose
        self.left = self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, name, time, purpose):
        if not self.root:
            self.root = Node(name, time, purpose)
            return
        cur = self.root
        while True:
            if name < cur.name:
                if not cur.left:
                    cur.left = Node(name, time, purpose)
                    return
                cur = cur.left
            elif name > cur.name:
                if not cur.right:
                    cur.right = Node(name, time, purpose)
                    return
                cur = cur.right
            else:
                print("Visitor already exists.")
                return
    def search(self, name):
        cur = self.root
        while cur:
            if name == cur.name:
                print("\nName:", cur.name)
                print("Time:", cur.time)
                print("Purpose:", cur.purpose)
                return
            cur = cur.left if name < cur.name else cur.right
        print("Visitor not found.")
    def delete(self, root, name):
        if not root:
            return None
        if name < root.name:
            root.left = self.delete(root.left, name)
        elif name > root.name:
            root.right = self.delete(root.right, name)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            temp = root.right
            while temp.left:
                temp = temp.left
            root.name, root.time, root.purpose = (
                temp.name, temp.time, temp.purpose
            )
            root.right = self.delete(root.right, temp.name)
        return root
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.name, "-", root.time, "-", root.purpose)
            self.inorder(root.right)
    def preorder(self, root):
        if root:
            print(root.name, "-", root.time, "-", root.purpose)
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.name, "-", root.time, "-", root.purpose)
    def count(self, root):
        return 0 if not root else 1 + self.count(root.left) + self.count(root.right)
bst = BST()
while True:
    print("\n===== VISITOR LOG BOOK =====")
    print("1.Insert")
    print("2.Delete")
    print("3.Search")
    print("4.Inorder")
    print("5.Preorder")
    print("6.Postorder")
    print("7.Count")
    print("8.Exit")
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Enter a number from 1 to 8.")
        continue
    if choice == 1:
        name = input("Name: ")
        time = input("Time: ")
        purpose = input("Purpose: ")
        bst.insert(name, time, purpose)
    elif choice == 2:
        name = input("Enter Name to delete: ")
        bst.root = bst.delete(bst.root, name)
    elif choice == 3:
        bst.search(input("Enter Name to search: "))
    elif choice == 4:
        bst.inorder(bst.root)
    elif choice == 5:
        bst.preorder(bst.root)
    elif choice == 6:
        bst.postorder(bst.root)
    elif choice == 7:
        print("Total Entries:", bst.count(bst.root))
    elif choice == 8:
        print("Program terminated.")
        break
    else:
        print("Invalid choice.")
