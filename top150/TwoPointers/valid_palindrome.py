class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower().strip().replace(" ", "")
        for i in range(len(s)):
            if s[i].isdigit():
                s = s[:i] + s[i+1:]

        return s
        
solution_instance = Solution()
print(solution_instance.isPalindrome("A man, a plan, a canal: Pana124AAAAma   "))