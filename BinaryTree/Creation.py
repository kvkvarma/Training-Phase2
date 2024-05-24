class Box:
    def __init__(self,data) -> None:
        self.data=data 
        self.left=None 
        self.right=None
def printInOrderTraversal(root):
    if root==None:
        return 
    printInOrderTraversal(root.left)
    print(root.data,end=" ")
    printInOrderTraversal(root.right)
    
def printPreOrderTraversal(root):
    if root==None:
        return
    print(root.data,end=" ")
    printPreOrderTraversal(root.left)
    printPreOrderTraversal(root.right)
    
def printPostOrderTraversal(root):
    if root==None:
        return
    printPostOrderTraversal(root.left)
    printPostOrderTraversal(root.right)
    print(root.data,end=" ")
    
obj1=Box(10)
obj2=Box(40)
obj3=Box(30)
obj4=Box(20)
obj5=Box(80)
obj6=Box(60)
obj7=Box(70)

obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj2.right=obj5
obj3.left=obj6
obj3.right=obj7

printInOrderTraversal(obj1)
print()
printPreOrderTraversal(obj1)
print()
printPostOrderTraversal(obj1)