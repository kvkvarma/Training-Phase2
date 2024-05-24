class Box:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def printLinkedList(curr):
    while curr !=None:
        print(curr.data)
        curr=curr.next
        
#inserting at the tail 
def insertAtTailNode(head,ele):
    temp=Box(ele)
    if head ==None:
        return temp
    tail=head
    
    while tail.next!=None:
        tail=tail.next
    tail.next=temp
    return head
    
#insertion at insertatBeginning

def insertatBeginning(head,ele):
    temp=Box(ele)
    if head==None:
        return temp
    temp.next=head
    return temp
    
#insertion at specific position
def insertAtSpecificPosition(head, position, ele):
    if position == 0:
        return insertatBeginning(head, ele)
 
    temp = Box(ele)
    currentIndex = 0 
    currentNode = head 
    while currentIndex != position - 1:
        currentIndex += 1 
        currentNode = currentNode.next 
 
    temp.next = currentNode.next 
    currentNode.next = temp 
    return head
    
head=None
nums=[10,20,30,40,50,60,70,80,90,100]
for ele in nums:
    head=insertAtTailNode(head,ele)

## block creation is happening below
# obj1=Box(10)
# obj2=Box(20)
# obj3=Box(30)
# obj4=Box(40)

# #establiahing links in below four lines
# obj1.next=obj2
# obj2.next=obj3
# obj3.next=obj4
# obj4.next=None

insertAtTailNode(head,5)
head=insertatBeginning(head,56)
head=insertAtSpecificPosition(head,5,34)
printLinkedList(head)