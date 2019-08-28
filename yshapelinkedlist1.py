# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:31:24 2018

@author: amit
"""

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
            currentA,currentB = headA,headB
            intersection={}
            while 1 :
                print("Intersection map value : "+str(intersection))
                # print(currentA.value)
                # print(currentB.value)
    
                if not currentA.next and not currentB.next:
                    print("No intersection found")
                    return -1
                # Check for A
                if currentA.next :
                    print("Current A value now : "+str(currentA.value))
                    # Check if it exists in map
                    if currentA.next.value in intersection :
                        print("Returning from A")
                        return currentA.next.value
                    else :
                        intersection[currentA.next.value]=currentA.value
                        currentA = currentA.next
                        print("Going next A :"+str(currentA.value))
                # Check for B
                if currentB.next :
                    print("Current B value now : "+str(currentA.value))
                    # Check if it exists in map
                    if currentB.next.value in intersection :
                        print("Returning from B")
                        return currentB.next.value
                    else :
                        intersection[currentB.next.value]=currentB.value
                        currentB = currentB.next
                        print("Going next B : "+str(currentA.value))
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
b3=Element(2)
b4=Element(0)
#b5=Element(3)

l2=Linkedlist()
l2.append(b1)
l2.append(b2)
l2.append(b3)
l2.append(b4)
#l2.append(b5)


l2.printlist()

print(l1.getIntersectionNode(l2))