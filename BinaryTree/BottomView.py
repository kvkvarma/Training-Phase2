class Box:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def bottomViewHelper(root, store, hd, level):
    if root == None:
        return 
 
    if hd not in store or store[hd][0] <= level:
        store[hd] = [level, root.data]
 
    bottomViewHelper(root.left, store, hd - 1, level + 1)
    bottomViewHelper(root.right, store, hd + 1, level + 1)
 
def findBottomView(root):
    result = []
    if root == None:
        return result
 
    store = {}
    bottomViewHelper(root, store, 0, 0)
    sortedKeys = sorted(store.keys())
    for key in sortedKeys:
        result.append(store[key][1])
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

print(findBottomView(obj1))