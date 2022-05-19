class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.next

    def add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    #Adding node after x
    def add_after(self,data, x):
        n =self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print("Node not found in linked list")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty.")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Node not found.")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")

    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty can't delete!")
        else:
            self.head=self.head.next

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty, cannot delete shit.")
        elif self.head.next is None:
            self.head = None
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None

    def delete_by_value(self, x):
        if self.head is None:
            print("Linked list is empty. Can't delete shit.")
            return
        if x == self.head.data:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Node not found")
        else:
            n.next = n.next.next




ll1 = LinkedList()
# ll1.add_before(20, 10)
# ll1.add_before(30, 10)
ll1.add_end(100)
# ll1.add_after(200, 100)
ll1.add_end(500)
ll1.add_begin(20)
# ll1.delete_begin()
# ll1.delete_end()
ll1.delete_by_value(20)

ll1.print_ll()

#     def list_length(self):
#         current_node = self.head
#         length = 0
#         while current_node is not None:
#             length += 1
#             current_node = current_node.next
#         return length

#     def insert_head(self, new_node):
#         temp_node = self.head
#         self.head = new_node
#         self.head.next = temp_node
#         del temp_node

#     def insert_at(self,new_node,position):
#         if position < 0 or position > self.list_length():
#             print("Invalid position")
#             return
#         if position == 0:
#             self.insert_head(new_node)
#             return
#         current_node = self.head
#         current_position = 0
#         while True:
#             if current_position == position:
#                 previous_node.next = new_node
#                 new_node.next = current_node
#                 break
#             previous_node = current_node
#             current_node = current_node.next
#             current_position += 1

#     def insert_end(self, new_node):
#         if self.head is None:
#             self.head = new_node
#         else:
#             last_node = self.head
#             while True:
#                 if last_node.next is None:
#                     break
#                 last_node = last_node.next
#             last_node.next = new_node


#     def delete_head(self):
#         previous_head = self.head
#         self.head = self.head.next
#         previous_head.next = None


#     def delete_end(self):
#         last_node = self.head
#         while last_node.next is not None:
#             previous_node = last_node
#             last_node = last_node.next
#         previous_node.next = None

#     def print_list(self):
#         if self.head is None:
#             print("List is empty")
#             return
#         current_node = self.head
#         while True:
#             if current_node is None:
#                 break
#             print(current_node.data)
#             current_node = current_node.next

    



# linked_list = LinkedList()
# first_node = Node("John")
# linked_list.insert_end(first_node)
# second_node = Node("Ben")
# linked_list.insert_end(second_node)

# linked_list.insert_head(third_node)
# third_node = Node("Matthew")
# linked_list.insert_end(third_node)
# linked_list.insert_at(third_node, 1)
# linked_list.delete_end()
# linked_list.delete_head()
# linked_list.print_list()
