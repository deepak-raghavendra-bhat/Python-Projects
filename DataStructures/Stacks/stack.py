class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return not self.items
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
if __name__ == "__main__":
    s = Stack()
    # print(s)
    # print(s.isEmpty())
    # s.push(1)
    # print(s)
    # s.push(2)
    # s.push(3)
    # s.push(4)
    # print(s)
    # print(s.peek())
    # print(s.pop())
    # print(s)    
    # print(s.size())