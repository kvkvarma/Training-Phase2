
class Box:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root, val):
    if root==None:
        return Box(val)
    elif root.val >val:
        root.left=insertIntoBST(root.left,val)
    else:
        root.right=insertIntoBST(root.right,val)
    return root

def PrintBST(root):
    if root==None:
        return None
    res=[]
    Q=[root]
    
    while len(Q)>0:
        y=Q.pop(0)
        res.append(y.val)
        if y.left !=None:
            Q.append(y.left)
        if y.right !=None:
            Q.append(y.right)
    
    return res


root = None
liss=[10,8,15,22,28,5,6,7]
for i in liss:
    print(i)
    root = insertIntoBST(root, i)


insertIntoBST(root,16)
print(PrintBST(root))