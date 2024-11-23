class Queue:
    def __init__(self):
        self.queue = []  # Initialize an empty list to represent the queue
    
    # Enqueue: Add an element to the rear of the queue
    def enqueue(self, item):
        self.queue.append(item)
    
    # Dequeue: Remove and return the front element of the queue
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # Remove and return the front element
        else:
            return "Queue is empty"
    
    # Peek: Return the front element without removing it
    def peek(self):
        if not self.is_empty():
            return self.queue[0]  # Return the front element
        else:
            return "Queue is empty"
    
    # Is empty: Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

# Testing the Queue implementation
queue = Queue()

# Enqueue three elements: 10, 20, 30
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# Dequeue one element and display the result
dequeued_element = queue.dequeue()
print(f"Dequeued element: {dequeued_element}")

# Peek at the front element of the queue
front_element = queue.peek()
print(f"Front element after dequeue: {front_element}")

