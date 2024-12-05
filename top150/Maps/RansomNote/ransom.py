from collections import defaultdict

def main():
     canConstruct("a", "b")
def canConstruct(ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        chars = defaultdict(int)
        for char in magazine:
            chars[char] += 1
        for char in ransomNote:
            if chars[char] == 0:
                return False
            else:
                chars[char] -=1
        return True 

if __name__ == "__main__":
     main()