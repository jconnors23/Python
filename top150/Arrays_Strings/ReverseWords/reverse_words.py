class Solution(object):
    
    def reverseWords(self, s):
        stripped_s = s.strip()
        clean_s = ' '.join(stripped_s.split())
        rev_s = clean_s[::-1]
        words = ''
        track = 0
        last_space = 0
        for i in range(len(rev_s)):
            if rev_s[i] == ' ':
                last_space = i
                word = rev_s[track: i]
                rev_word = word[::-1]
                if track == 0:
                    word = rev_s[track: i]
                    rev_word = word[::-1]
                    words += rev_word
                    track = i+1
                    continue
                else: 
                    words += " " 
                    track = i+1
                    words += rev_word
            elif not rev_s[i] == ' ' and i == len(rev_s)-1:
                if last_space == 0:
                    words += clean_s 
                    return words
                words += " " 
                word = rev_s[last_space+1:]
                rev_word = word[::-1]
                words += rev_word
        
        return words

solution_instance = Solution() 


# print(solution_instance.reverseWords(s="  hello world  "))
# print(solution_instance.reverseWords(s="the sky is blue f     "))
# print(solution_instance.reverseWords(s="a good   example"))
# def reverseWords(self, s):
#     return " ".join(s.split()[::-1])
# print(solution_instance.reverseWords(s="EPY2giL"))
# print(f"cur char: {rev_s[i]}")
# print(f"word to reverse: {word}, i: {i}")