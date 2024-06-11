class Stack:
    def __init__(self):
        self.values = []
    
    def push(self, item):
        self.values.append(item)

    def pop(self):
        if not self.is_empty():
            return self.values.pop()
        else:
            print('Empty Stack')

    def is_empty(self):
        return len(self.values) == 0
        
    def peek(self):
        if not self.is_empty():
            return self.values[-1]
        else:
            return None
    
    def size(self):
        return len(self.values)
    
stack = Stack()

stack.peek()
#Empty Stack
stack.is_empty()
#True

stack.push(10)
stack.push(12)
stack.push(14)

stack.size()
#3
stack.peek()
#14
stack.pop()
stack.peek()
#12
stack.pop()
stack.peek()
#10
stack.pop()
stack.peek()
#Empty Stack
stack.is_empty()
#True
