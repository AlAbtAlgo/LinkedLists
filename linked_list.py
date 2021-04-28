'''
@author: vnaazleen
Program: Singly linked list
Basic operations:
Traversing the list - Time complexity - O(n) space complexity- O(1)
Inserting an item in the list 
 - at the beginning     => Time complexity - O(1) space complexity - O(1)
 - at the end           => Time complexity - O(n) space complexity - O(1)
 - at random position   => Time complexity - O(n) space complexity - O(1)
Deleting an item from the list
 - deleting first node  => Time complexity - O(1) space complexity - O(1)
 - deleting last node   => Time complexity - O(n) space complexity - O(1)
 - deleting an intermediate node => Time complexity - O(n) space complexity - O(1)

'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def prepend(self, data):
        '''Insert a element at beginning'''
        node = Node(data, self.head)
        self.head = node

    def append(self, data):
        '''Inserting an element at the end'''
        if self.head is None:
            self.head = Node(data)
            return
        node = Node(data)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node

    def insert(self, index : int, data : int):
        '''Insert an element at given position'''
        node = Node(data)
        itr = self.head
        while itr.next and index > 1:
            itr = itr.next
            index -= 1
        if index == 1:
            node.next = itr.next
            itr.next = node
        
    def pop(self):
        '''Deletes an element at end of the linked list'''
        if not self.head:
            return 

        if not self.head.next:
            self.head = None
            return 
        
        itr = self.head
        while itr.next.next:
            itr = itr.next 
        itr.next = None

    def pop_front(self):
        '''Deletes an element at front of linked list'''
        ll.pop()
        if not self.head:
            return 
            
        self.head = self.head.next

    def pop_position(self, index : int):
        '''Deletes an element at given position in linked list'''
        if (index == 0):
            self.pop_front()
        itr = self.head
        while itr.next and index > 1:
            itr = itr.next
            index -= 1
        if index == 1 and itr.next:
            itr.next = itr.next.next

    def print(self):
        '''Prints the Linked list'''
        if self.head is None:
            print("List is Empty")
            return
        itr = self.head
        llstr = "[" + str(itr.data) + "] ->"
        while itr.next.next:
            itr = itr.next
            llstr += "[" + str(itr.data) + "] ->"
        print(llstr + "[" + str(itr.next.data) + "]")



    
if __name__ == '__main__':
    ll = LinkedList()
    ll.prepend(25)
    ll.prepend(20)
    ll.prepend(10)
    ll.prepend(5)
    ll.append(30)
    ll.append(35)
    ll.insert(2, 15)
    print("Linked list:",end=" ")
    ll.print()

    print("Pop front:",end=" ")
    ll.pop_front()
    ll.print()

    print("Pop:",end=" ")
    ll.pop()
    ll.print()

    print("Pop index 2:",end=" ")
    ll.pop_position(2)
    ll.print()

    """
    Ouput:
    =====
    Linked list: [5] ->[10] ->[15] ->[20] ->[25] ->[30] ->[35]
    Pop front: [10] ->[15] ->[20] ->[25] ->[30]
    Pop: [10] ->[15] ->[20] ->[25]
    Pop index 2: [10] ->[15] ->[25]
    
    """

    
