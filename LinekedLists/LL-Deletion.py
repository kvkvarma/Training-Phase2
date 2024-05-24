class Box:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def printLinkedList(curr):
    while(curr !=None):
        print(curr.data,end="-->")
        curr=curr.next
    print()    
    
def insertatEnd(head,ele):
    temp=Box(ele)
    if head==None:
        return temp
    tail=head
    
    while tail.next!=None:
        tail=tail.next
    tail.next=temp
    return head

def deleteatEnd(head):
    
    if head==None or head.next==None:
        return None
    curr=head
        
    while curr.next.next!=None:
        curr=curr.next 
    curr.next=None
    return head.next

def deleteatBeginning(head):
    if head==None:
        return None
    
    #return head.next
    
    second=head.next
    head.next=None
    return second

    
def deleteatSpecificPosition(ele,pos):
    if pos==0:
        return deleteatBeginning(head)
    currIndex=0
    currNode=head
    while currIndex!=pos-1:
        currIndex+=1
        currNode=currNode.next
    nodetodelete=currNode.next
    currNode.next=nodetodelete.next
    nodetodelete.next=None

head=None
nums=[10,20,30,40,50]
for i in nums:
    head=insertatEnd(head,i)

printLinkedList(head)   
deleteatEnd(head)
printLinkedList(head)
head=deleteatBeginning(head)
printLinkedList(head)
deleteatSpecificPosition(head,2)
printLinkedList(head)