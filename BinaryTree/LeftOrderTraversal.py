class Box:
    def __init__(self,data) -> None:
        self.data=data 
        self.left=None 
        self.right=None
def levelOrderTraversal(root):
    if root==None:
        return 
    result=[]
    Q=[root]
    
    while len(Q)>0:
        n=len(Q)
        subResult=[]
        for i in range(n):
            #step-1
            currNode = Q.pop(0)
 
            # step - 2
            subResult.append(currNode.data)
 
            # step - 3
            if currNode.left != None:
                Q.append(currNode.left)
 
            # step - 4
            if currNode.right != None:
                Q.append(currNode.right)
 
        result.append(subResult)
 
    print(result)
            
        
obj1=Box(50)
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

levelOrderTraversal(obj1)