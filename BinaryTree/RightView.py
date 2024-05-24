class Box:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


#Function to return a list containing elements of right view of the binary tree.
def RightView(root):
    
    # code here
    if root ==None:
        return []
    result=[]
    Q=[root]
    while len(Q)>0:
        n=len(Q)
        for i in range(n):
            curr=Q.pop(0)
            if i==n-1:
                result.append(curr.data)
            if curr.left!=None:
                Q.append(curr.left)
            if curr.right!=None:
                Q.append(curr.right)
    return result

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

print(RightView(obj1))