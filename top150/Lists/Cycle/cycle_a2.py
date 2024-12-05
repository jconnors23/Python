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
            # linked_map = {head.val: head.next for node in head}
            linked_map = {}
            while True:
                if head.next == None:
                    return False
                if head.next in visited:
                    return True
                linked_map[head.val] = head.next
                visited.append(head.next)
                head = head.next
            # for key in linked_map:
            #     if linked_map[key] == None:
            #         return False
            #     if linked_map[key] in visited:
            #         return True
            #     visited.append(linked_map[key])

