def main():
    t1 = Stack()
    t1.push(1)
    t1.push(2)
    t1.push(3)
    t1.pop()
    print(t1)
    print(t1.top())
    print(t1.getMin())

class Stack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def __str__(self):
        return str(self.stack)
    
    def push(self, val):
        if not self.minstack or val <= self.minstack[-1]:
             self.minstack.append(val)
        self.stack.append(val)

    def pop(self):
        if self.stack[-1] <= self.minstack[-1]:
            self.minstack = self.minstack[:-1]
        self.stack = self.stack[:-1]

    def getMin(self):
        return self.minstack[-1]
    
    def top(self):
        return self.stack[-1]
    
if __name__ == "__main__":
    main()