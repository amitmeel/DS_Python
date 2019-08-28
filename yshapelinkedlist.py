# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:30:17 2018

@author: amit
"""

 #Definition for singly-linked list.
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist(object):
    def __init__(self, head=None):
        self.head = head
        
        #This method will add a new Element to the end of our LinkedList."""    
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def printlist(self):
        current = self.head
        while current:
            print(current.value,"->",end="")
            current = current.next
        print()
            
    def getIntersectionNode(self, l2):
        headA =self.head
        headB=l2.head
        
        #finding the length of both linked list
        currentA,currentB = headA,headB
        lenA,lenB = 0,0
        while currentA is not None:
            lenA += 1
            currentA = currentA.next
        while currentB is not None:
            lenB += 1
            currentB = currentB.next
        

        currentA,currentB = headA,headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                currentA = currentA.next
        elif lenB > lenA:
            for i in range(lenB-lenA):
                currentB = currentB.next
                
        while currentB.value != currentA.value:
            currentB = currentB.next
            currentA = currentA.next
            return currentA
        else:
            return "No intersection found"
        
        
e1=Element(1)
e2=Element(2)
e3=Element(4)
e4=Element(5)
e5=Element(7)

l1 =Linkedlist()
l1.append(e1) 
l1.append(e2) 
l1.append(e3) 
l1.append(e4) 
l1.append(e5)

l1.printlist()



b1=Element(3)
b2=Element(6)
b3=Element(7)
b4=Element(8)
b5=Element(9)

l2=Linkedlist()
l2.append(b1)
l2.append(b2)
l2.append(b3)
l2.append(b4)
l2.append(b5)


l2.printlist()

print(l1.getIntersectionNode(l2).value)













"""
int FindMergeNode(Node headA, Node headB) {
    Node currentA = headA;
    Node currentB = headB;

    //Do till the two nodes are the same
    while(currentA != currentB){
        //If you reached the end of one list start at the beginning of the other one
        //currentA
        if(currentA.next == null){
            currentA = headB;
        }else{
            currentA = currentA.next;
        }
        //currentB
        if(currentB.next == null){
            currentB = headA;
        }else{
            currentB = currentB.next;
        }
    }
    return currentB.data;
}

"""