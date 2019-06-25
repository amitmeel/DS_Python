class Singly_ll:

    def __init__(self):
        self.data = None
        self.next = None

    def setData(self,data):
        """method for setting the data of node"""
        self.data = data

    def getData(self):
        """method for getting the data of node"""
        return self.data

    def setNext(self,next):
        """method for setting the next field of the node"""
        self.next = next
    
    def getNext(self):
        """method for getting the next field of the node"""
        return self.next
    
    def hasNext(self):
        """method returns True if the node points to the next node"""
        return self.next != None

    def listLength(self):
        """method return the count of node in the list.
        Time Complexity: O(n), for scanning the ljst of size 11. 
        Space Complexity: 0(1), for creating a temporary variable.
        """
        count = 0
        current = self.head

        while current != None:
            count += 1
            current = current.getNext()

        return count

    def insertAtBegin(self,data):
        """method for inserting a new node at the beginning of the list."""
        newnode = Singly_ll()
        newnode.setData(data)

        if self.length == 0:
            self.head = newnode

        else:
            newnode.setNext(self.head)
            self.head = newnode
        self.length += 1

    def insertAtEnd(self,data):
        """method for inserting a new node at the end of the list."""
        newnode = Singly_ll()
        newnode.setData(data)

        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        
        current.setNext(data)
        self.length += 1

    def insertAtPosition(self,pos,data):
        """method for inserting a node for a given position"""
        if pos > self.length or pos < 0 :
            return None
        else:
            if pos == 0:
                self.insertAtBegin(data)
            else:
                newnode = Singly_ll()
                newnode.setData(data)
                count = 0 
                current = self.head
                while count < pos-1:
                    count += 1
                    current = current.getNext()
                newnode.setNext(current.getNext())
                current.setNext(newnode)
                self.length += 1

    def deleteFromBegin(self):
        """method tp delete the first node of list"""
        if self.length == 0:
            print("The List is empty")
        else:
            self.head = self.head.getNext()
            self.length -= 1

    def deletefromLast(self):
        """method to delete the last node of the list"""
        if self.length == 0:
            print("The list is empty")
        else:
            currentnode = self.head
            previousnode = self.head
            while currentnode.getNext() != None:
                previousnode = currentnode
                currentnode = currentnode.getNext()
            previousnode.setNext(None)
            self.length -= 1

    def deleteIntermediateNode(self,node):
        """method for deleting with node from the list"""
        if self.length == 0:
            raise ValueError('List is Empty')
        else:
            current = self.head
            previous = None
            found = False

            while not found:
                if current == node:
                    found = True
                elif current is None:
                    raise ValueError('Node not in list')
                else:
                    previous = current
                    current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.length -= 1 

    def deleteValue(self,value):
        """method for delete a perticular value from the list"""
        currentnode = self.head
        previousnode = self.head

        while currentnode.next != None or currentnode.value != value:
            if currentnode.value == value:
                previousnode.next = currentnode.next
                self.length -= 1
                return
            else:
                previousnode = currentnode
                currentnode = currentnode.next
        print("the value provided is not present")

    def deleteAtPoition(self,pos):
        """method to delete from a given position"""
        count = 0
        currentnode = self.head
        previousnode = self.head
        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        else:
            while currennode.next != None or count < pos:
                count += l
                if count== pos:
                    previousnode.next = currentnode.next
                    self.length -= 1
                    return
                else:
                    previousnode = currentnode
                    currentnode = currentnode.next

    def clearlist(self):
        """method for deleting singly linked list"""
        self.head = None






    










    


    