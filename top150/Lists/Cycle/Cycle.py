# Definition for singly-linked list.

class Solution(object):
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None
        
        def hasCycle(self, head):
            """
            :type head: ListNode
            :rtype: bool
            """
            if head is None:
                return False
            visited = []
            while True:
                if head.next == None:
                    return False
                visited.append(head)
                head = head.next
                for i in range(len(visited)):
                    first_copy = visited[i]
                    for j in range(len(visited)):
                        if i == j:
                            continue
                        if visited[j] == first_copy:
                            return True

