class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_head(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode

    def insert_end(self, data):
        newNode = Node(data)
        # create a tempory pointer to work through the list starting at the head
        current = self.head
        # loop through the list until the next is not pointed at a node
        while (current.next is not None):
            current = current.next
        # set the next of the current node to the new node
        current.next = newNode

    def insertAfter(self, prev_node, new_data):

        current = self.head
        newNode = Node(new_data)

        if prev_node is None:
            return
        # set the new node next to the given node next
        newNode.next = current.next
        # set the given node next to the new node
        current.next = newNode

        current = current.next

    def __iter__(self):
        # set node to equal the head to start at the beginning of list
        node = self.head
        while node is not None:
            yield node
            # set the node to the next node in the list
            node = node.next

    def remove(self, value):
        # start at the head of the list
        current = self.head

        # if the node to be deleted is the head, set the head to the next node
        if current.data == value:
            self.head = self.head.next
            return

        # keep track of the previous node
        previous_node = self.head

    # loop through the list
        for node in self:
            # if the node to be deleted is found next the previous node next to the deleted node next
            if node.data == value:
                previous_node.next = node.next
                return
            # otherwise set the previous node to the node to keep going through the list
            previous_node = node

   # ***New function to get the count of the linke list***
    def getCount(self):
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next
        return count

# This function prints the list in a readable format
    def __str__(self):
        result = ""
        node = self.head
        while node:
            result += str(node.data) + ", "
            node = node.next

        result = result.strip(", ")
        if len(result):
            return "[" + result + "]"
        else:
            return "[]"


list = LinkedList()
list.insert_head("Chevy")
list.insert_end("Ford")
list.insert_end("GMC")
list.insert_end('BMW')
list.insert_end("KIA")
list.insert_end("Honda")
list.insert_end("Subaru")
print(list)  # [Chevy, Ford, GMC, BMW, KIA, Honda, Subaru]

print(list.getCount())  # 7
