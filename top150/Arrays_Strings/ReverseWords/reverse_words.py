class Solution(object):

    def reverseWords(self, s):
        stripped_s = s.strip()
        print(f"strip: {stripped_s}")
        rev_s = stripped_s[::-1]
        print(f"reversed: {rev_s}")
        words = ''
        track = 0
        for i in range(len(rev_s)):
            if rev_s[i] == ' ':
                print("reached")
                word = rev_s[track: i]
                (f"word to reverse: {word}, i: {i}")
                rev_word = word[::-1]
                if track == 0:
                    word = rev_s[track: i]
                    (f"word to reverse: {word}, i: {i}")
                    rev_word = word[::-1]
                    words += rev_word
                    print(words)
                    track = i+1
                    continue
                else: 
                    print("reached")
                    words += " " 
                    track = i+1
                    words += rev_word
                    print(words)
            print(f"tracker: {track}")
        return words

solution_instance = Solution() 
print(solution_instance.reverseWords(s="  hello world  "))
