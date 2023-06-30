"""
CSE212 
(c) BYU-Idaho
04-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class Priority_Queue:
    """
    This queue follows the same FIFO process except that higher priority
    nodes will be dequeued before lower priority nodes.  Nodes of the same
    priority will follow the same FIFO process.
    """

    class Node:
        """
        Each node is the queue will have both a value and a priority.
        """

        def __init__(self, value, priority):
            """
            Initialize a new node
            """
            self.value = value
            self.priority = priority

        def __str__(self):
            """
            Display a single node
            """
            return "{} (Pri:{})".format(self.value, self.priority)

    def __init__(self):
        """ 
        Initialize an empty priority queue
        """
        self.queue = []

    def enqueue(self, value, priority):
        """
        Add a new value to the queue with an associated priority.  The
        node is always added to the back of the queue irregardless of 
        the priority.
        """
        new_node = Priority_Queue.Node(value, priority)  #needed to flip value and priority -- was new_node = Priority_Queue.Node(value, priority)
        self.queue.append(new_node)

    def dequeue(self):
        """
        Remove the next value from the queue based on the priority.  The 
        highest priority item will be removed.  In the case of multiple
        values with the same high priority, the one closest to the front
        (in traditional FIFO order) will be removed.  Priority values are
        interpreted as higher numbers have higher priority.  For example, 
        10 is a higher priority than 5.
        """
        if len(self.queue) == 0:  # Verify the queue is not empty
            print("The queue is empty.")
            return None
        # Find the index of the item with the highest priority to remove
        high_pri_index = 0
        for index in range(1, len(self.queue)):
            if self.queue[index].priority > self.queue[high_pri_index].priority:  #changed >= to just > so that it will not replace the next value with the same priority
                    high_pri_index = index
        # Remove and return the item with the highest priority
        value = self.queue[high_pri_index].value
        del self.queue[high_pri_index]    #this line was missing 
        return value
        
    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """ 
        Suppport the str() function to provide a string representation of the
        priority queue.  This is useful for debugging.  If you have a 
        Priority_Queue object called pq, then you run print(pq) to see the 
        contents.
        """
        if self.queue == []:
            return('Queue is empty') #needed to add this error messge if queue is empty

        result = "["
        for node in self.queue:
            result += str(node)  # This uses the __str__ from the Node class
            result += ", "
        result += "]"
        return result

# Test Cases

# Test 1
# Scenario: Create a queque with the new number added to the end of the queque. 
# Expected Result: [5 (Pri: 1), 8 (Pri: 4), 9 (Pri: 2), 85 (Pri: 3)]
print("Test 1")
nodes = Priority_Queue()
nodes.enqueue(5, 1)
nodes.enqueue(8, 4)
nodes.enqueue(9, 2)
nodes.enqueue(85, 3)
print(nodes)

# Defect(s) Found: The output is flipping the number and priority. The first input should be the number and the
# second input should be the priority. In the enqueque function where the new_node is set the priority and value needed
# swapped
# new_node = Priority_Queue.Node(priority, value)

print("=================")

# Test 2
# Scenario: Using the queue created in Test 1: [5 (Pri: 1), 8 (Pri: 4), 9 (Pri: 2), 85 (Pri: 3)], 
# delete the node with the highest priority.
# Expected Result: [5 (Pri:1), 9 (Pri:2), 85 (Pri:3)]
print("Test 2")
nodes.dequeue()
print(nodes)

# Defect(s) Found: The dequeue function was only returning the value of the node with the highest priority.
# It needed this line del self.queue[high_pri_index] added to delete the node. 

print("=================")

# Add more Test Cases As Needed Below

# Test 3
# Scenario: Create a queque that has the values [3 (Pri: 1), 10 (Pri: 4), 9 (Pri: 2), 85 (Pri: 3), 40 (Pri: 4)]
# If two nodes have the same priority, delete the item closest to the front of the queue.
# Expected Result: [3 (Pri: 1), 9 (Pri: 2), 85 (Pri: 3), 40 (Pri: 4)]
print("Test 3")
nodes = Priority_Queue()
nodes.enqueue(3, 1)
nodes.enqueue(10, 4)
nodes.enqueue(9, 2)
nodes.enqueue(85, 3)
nodes.enqueue(40, 4)
#print(pq)
nodes.dequeue()
print(nodes)

# Defect(s) Found: The dequeue function loops through the queue starting at the front and sets the index
# to the number with the highest priority. If there is a number with the same priority farther back in the queue
# the index is then replaced with that number's index. Then it will delete the number with that index, so the last
# number with the same highest priority is deleted. In the if statement, instead of looking for greater than and equal to
# priorities, if it just looks for priorities that are greater than the current highest, it will delete the first one 
# it finds instead of the last. 

print("=================")

# Test 4
# Scenario: If there are no nodes in the queue an error message will be displayed.
# Expected Result: Error message
print("Test 4")
nodes = Priority_Queue()
print(nodes)

# Defect(s) Found: It was returning an empty queue instead of an error message. 
