

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def contains(self, data):
        runner = self.head
        while runner:
            if runner.data == data:
                return True
            runner = runner.next
        return False

    def length(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def display(self):
        node = Node(10)
        while node:
            print node.data
            node = node.next

    def min_to_front(h):
        if h == None or h.next == None:
            return h

        # find part
        temp = h
        myList = []
        while temp != None:
            myList.append(temp.element)
            temp = temp.next
        myList.sort()
        sv = myList[0]

        # remove part
        if h.element == sv and h.next != None:
            h = h.next
        else:
            start = h
            while start != None:
                if start.next.element == sv and start.next.next != None:
                    start.next = start.next.next
                    break
                if start.next.element == sv and start.next.next == None:
                    start.next = None
                    break
                start = start.next

        # Insert part
        newNode=Node(sv)
        newNode.next=h
        h=newNode
        return h

    def max_to_front(self):
        #I couldn't figure this one out
        pass

    def insert_head(self,new_node):
        # Data=>Matthew, Next=None
        temp_node = self.head #John
        self.head = new_node #Matthew
        self.head.next = temp_node
        del temp_node

    def insert_end(self, new_node):
        # Head=John --> None
        if self.head is None:
            self.head = new_node
        else:
            # Head=John --> Ben -->None
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = new_node

    def print_list(self):
        if self.head is None:
            print("List is empty.")
            return
        # Head=John--> Ben --> Matthew --> None
        current_node = self.head
        while True:
            if current_node is None:
                break
            print(current_node.data)
            current_node = current_node.next

    def add_front(self, data):
        new_node = Node(10)
        new_node.next = self.head
        self.head = new_node

    def insert_at(self, new_node, idx):
        current_node = self.head
        current_idx = 0
        while True:
            if current_idx == idx:
                previous_node.next = new_node
                new_node.next =current_node
                break
            previous_node = current_node
            current_node = current_node.next
            current_idx += 1

    def front(self, data):
        if self.head is None:
            return None
        else:
            return self.head.data
        return self.head
  

# first_node = Node(10)
# linked_list = LinkedList()
# linked_list.insert_end(first_node)
# second_node = Node(20)
# linked_list.insert_end(second_node)
# # linked_list.print_list()
# third_node = Node(15)
# linked_list.insert_at(third_node, 1)
# linked_list.print_list()


first_node = Node("John")
linked_list = LinkedList()
linked_list.insert_end(first_node)
second_node = Node("Ben")
linked_list.insert_end(second_node)
third_node = Node("Matthew")
linked_list.insert_head(third_node)
linked_list.print_list()




    # def front(self):
    #     if not self.head:
    #         return None
    #     else:
    #         self.head = Node(30)
    #         print(self.head.data)
    #         return self.head.data

    # def remove_front(head):
    #     if not head:
    #         return None
    #     temp = head

    #     # Move the head pointer to the next node
    #     head = head.next
    #     temp = None
    #     return head

    # def print_LL(self):
    #     if self.head is None:
    #         print("linked list is empty")
    #     else:
    #         n = self.head
    #         while n is not None:
    #             print(n.data)
    #             n = n.next


