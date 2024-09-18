N = int(input())

class Node():
    def __init__(self,data,prev_node = None,next_node = None) -> None:
        self.data = data
        self.prev = prev_node
        self.next = next_node

class DoublyLinkedList():

    def __init__(self,head_node = None) -> None:
        self.head = head_node

    def insert(self,data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        self.head = new_node
        new_node.next = current_node
        current_node.prev = new_node

    def delete(self,data) -> None:
        current_node = self.head
        if current_node and current_node.data == data:
            if current_node.next is None:
                self.head = None
                current_node = None
                return
            else:
                next_node = current_node.next
                self.head = next_node
                next_node.prev = None
                current_node = None
                return

        while current_node and current_node.data != data:
            current_node = current_node.next

        if current_node is None:
            return

        if current_node.next is None:
            prev_node = current_node.prev
            prev_node.next = None
            current_node = None
            return
        else:
            next_node = current_node.next
            prev_node = current_node.prev
            next_node.prev = prev_node
            prev_node.next = next_node
            current_node = None
            return
    
    def delete_first(self) -> None:
        current_node = self.head
        if current_node.next is None:
            self.head = None
            current_node = None
            return
        next_node = current_node.next
        next_node.prev = None
        self.head = next_node
        return
        
    def delete_last(self) -> None:
        current_node = self.head
        if current_node.next is None:
            self.head = None
            current_node = None
            return
        
        while not current_node.next is None:
            current_node = current_node.next

        prev_node = current_node.prev
        prev_node.next = None
        current_node = None
        
    def print(self) -> None:
        current_node = self.head
        print_list = []
        while current_node:
            print_list.append(current_node.data)
            current_node = current_node.next
        print(" ".join(map(str,print_list)))

linkedlist = DoublyLinkedList()

for _ in range(N):
    input_str = input()
    if input_str == "deleteFirst":
        linkedlist.delete_first()
    elif input_str == "deleteLast":
        linkedlist.delete_last()
    else:
        command,num = input_str.split()
        if command == "insert":
            linkedlist.insert(int(num))
        if command == "delete":
            linkedlist.delete(int(num))



linkedlist.print()