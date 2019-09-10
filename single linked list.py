class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
        self.last=None

    def append(self,data):
         if self.last==None:
             self.head=Node(data)
             self.last=self.head
         else:
             self.last.next=Node(data)   # inserting at end which is after last node
             self.last=self.last.next    # stating last pointer to the new last node

def traversal(L):
    tmp=L.head
    a=' '
    while tmp!=None:
        a=a+str(tmp.data)+' '
        tmp=tmp.next
    print(a)

def insertbeg(l, n):
  n.next = l.head
  l.head = n
  print("inserted to linked list")

def insertend(l, n):
  temp = l.head

  while temp.next != None:
    temp = temp.next

  temp.next = n
  print("inserted to linked list")

def insertpos(L, ndata, p):
    tmp=L.head
    nnode = Node(ndata)
    a=L.head
    print("pos,",p)
    i=0
    while i<p :
        l=tmp
        tmp = tmp.next
        i=i+1
        print(i)

    nnode.next=l.next
    l.next=nnode
    print("inserted to linked list")

def delete(l, n):
  temp = l.head
  a=l.head
  i=1
  if n == 1: #node to be deleted is head
    l.head = temp.next
    del temp
  else: #node to be deleted is not head
    while i<n:
        a=temp
        temp=temp.next
        i=i+1
        print(a.data)

    a.next=temp.next
    del temp


if __name__ == '__main__':

 newlist=linkedlist()
 n=int(input("Number of nodes: "))
 for i in range(n):
     data= int(input("Enter node: "))
     newlist.append(data)

traversal(newlist)

lhead=newlist.head

c = str(input("Do you want to insert a new node (Y/N): "))
while c != 'N':
    val=int(input("Enter new data to be added in the linked list: "))
    nnode=Node(val)
    c2 = int(input("Enter 1 To insert at beginning  2 To insert at end  3 To insert after specific node: "))
    if c2==1:
        insertbeg(newlist,nnode)
    elif c2==2:
        insertend(newlist,nnode)
    elif c2==3:
        pnode=int(input("Enter position after which to insert node: "))
        insertpos(newlist,val,pnode)
    else:
        print("Error")
    c3 = str(input("Do you want to exit or insert another node? (press Y to exit): "))
    if c3 != 'Y':
       c = 'Y'
    else:
        print("New List after insertion: ")
        traversal(newlist)
        c = 'N'

cd=str(input("Do you want to delete a node? (Enter Y/N): "))
while cd!='N':
    dpos=int (input("Enter the position of the node in the list to be deleted: "))
    delete(newlist, dpos)
    cd1=str(input("Do you want to delete another node? (Press Y to continue,press any key to exit): "))
    if cd1 == 'Y':
        print("Node deleted")
        print("New list")
        traversal(newlist)
        cd='Y'
    else:
        print("Node deleted")
        print("New list")
        traversal(newlist)
        cd='N'













