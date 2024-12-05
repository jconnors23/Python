# Create a dictionary representing the pairs pairings = {"()", "{}", "[]"}
# Create stack data structure...
# Traverse each charater in input string...
# If open parentheses are present, append it to stack...
# If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not...
# If not, we need to return false...
# At last, we check if the stack is empty or not...
# If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false..


def main():
   print(Solution().isValid("){"))
   print(Solution().isValid("()[]{}"))
   print(Solution().isValid("(]"))
   print(Solution().isValid("([])"))

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return False
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            elif char == ")":
                if len(stack) == 0 or stack.pop() != "(":
                    return False
            elif char == "}":
                if len(stack) == 0 or stack.pop() != "{":
                    return False
            elif char == "]":
                if len(stack) == 0 or stack.pop() != "[":
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    main()
