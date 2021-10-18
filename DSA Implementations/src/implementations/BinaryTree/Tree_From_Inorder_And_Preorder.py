from TreeNode import * 

'''
In case of postorder, we would make last index of post order as root
'''
def findIndexInInorder(inorder, val) :
    for i in range(len(inorder)) :
        if inorder[i] == val :
            return i
    return -1

def construct(inorder, preorder, start, end) :
    global preindex
    if start >= end:
        return None
    root = TreeNode(preorder[preindex])
    index = findIndexInInorder(inorder, preorder[preindex])
    preindex += 1
    if index != -1 :
        root.left = construct(inorder, preorder,start, index)
        root.right =construct(inorder, preorder, index+1, end)
    return root


__name__ = '__main__'
global preindex
preindex = 0
inorder = list(map(str, input().split()))
preorder = list(map(str, input().split()))

root = construct(inorder, preorder, 0, len(preorder))
tree = Tree()
tree.root = root
print(tree)


