def hasCycle(self, head):
        if head is None:
            return False
        visited = []
        while True:
            if head.next == None:
                return False
            if head.next in visited:
                return True
            visited.append(head.next)
            head = head.next