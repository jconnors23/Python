class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split() # split the string s into a list of words
        if len(pattern) != len(words): # if the lengths don't match, there can't be a bijection
            return False
        
        pattern_to_word = {} # dictionary to store the mapping from pattern letters to words
        word_to_pattern = {} # dictionary to store the mapping from words to pattern letters
        
        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]
            if p in pattern_to_word and pattern_to_word[p] != w: # if p already maps to a different word, there's no bijection
                return False
            if w in word_to_pattern and word_to_pattern[w] != p: # if w already maps to a different pattern letter, there's no bijection
                return False
            pattern_to_word[p] = w # add the mapping from p to w
            word_to_pattern[w] = p # add the mapping from w to p
            
        return True # if we get here, there's a bijection between pattern letters and words