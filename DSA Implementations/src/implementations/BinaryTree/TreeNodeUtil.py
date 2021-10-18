from TreeNode import *
from collections import deque
def createTree(arr) :
    tree = Tree()
    root = TreeNode(arr[0])
    tree.root = root
    elem = deque([root])
    for i in range(1,len(arr)) :
        node = TreeNode(arr[i])
        parent = elem[0]
        if not parent.left :
            parent.left = node
        else :
            parent.right = node
            elem.popleft()
        elem.append(node)
    return tree

def insert(tree : Tree, val : int) :
    elem = deque([tree.root])
    node = TreeNode(val)
    while elem :
        tmp = elem.popleft()
        if tmp.left :
            elem.append(tmp.left)
        else :
            tmp.left = node
            break

        if tmp.right :
            elem.append(tmp.right)
        else :
            tmp.right= node
            break

#find the node to delete and find right most leaf node.
#replace val of node to delete with right most leaf and then delete right most leaf
def deleteNode(tree : Tree, val : int) :
    elem = deque([tree.root])
    while elem :
        last = elem.popleft()
        if last.val == val :
            delete = last
        if last.left :
            elem.append(last.left)
        if last.right :
            elem.append(last.right)
    last.val, delete.val = delete.val, last.val
    elem = deque([tree.root])
    while elem :
        val = elem.popleft()
        if val.left == last :
            val.left = None
            break
        if val.right == last:
            val.right = None
            break
        if val.left : 
            elem.append(val.left)
        if val.right : 
            elem.append(val.right)
         

#root -> left -> right
def print_preorder(root : TreeNode) :
    if root :
        print(root.val, end = ' ')
        print_preorder(root.left)
        print_preorder(root.right)

#lft -> root -> right
def print_inorder(root : TreeNode) :
    if root :
        print_inorder(root.left)
        print(root, end =' ')
        print_inorder(root.right)

#left -> right -> root
def print_postorder(root : TreeNode) :
    if root :
        print_postorder(root.left)
        print_postorder(root.right)
        print(root, end = ' ')


if __name__ == '__main__' :
    arr = list(map(int, input().split()))
    tree = createTree(arr)
    print('inorder traversal')
    print_inorder(tree.root)
    print()

    print('preorder traversal')
    print_preorder(tree.root)
    print()

    print('postorder traversal')
    print_postorder(tree.root)
    print()

    print('level order traversal')
    print(tree)
    print()
    
    insert(tree, 10)
    print(tree)
    print()

    deleteNode(tree, 4)
    print(tree)
    print()




    