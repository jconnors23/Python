def main():
    t1 = MinStack()
    t1.push(1)
    t1.push(2)
    t1.push(3)
    t1.pop()
    print(t1)
    print(t1.top())
    print(t1.getMin())

class MinStack(object):

    def __init__(self):
        self.stack = []
    
    def __str__(self):
        return str(self.stack)

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        return None
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack = self.stack[:len(self.stack)-1]
        return None
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        min = self.stack[0]
        for val in self.stack:
            if val < min:
                min = val
        return min
        
if __name__ == "__main__":
    main()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()