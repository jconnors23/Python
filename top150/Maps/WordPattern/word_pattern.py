def isBijective(pattern, s):
    # (pattern = "abba", s = "dog cat cat fish") 
    # (p = aba, s = c c c d )
    letter_map, word_map = {}, {}
    # LM: { a, b } WM: { dog cat fish }
    letters_seen, words_seen = [], []
    words = s.split()
    for word in words:
        if word not in word_map:
            word_map[word] = True
    for letter in pattern:
        if letter not in letter_map:
            letter_map[letter] = True
    if len(letter_map) != len(word_map):
        return False 
    
    for word in words:
      if word not in words_seen:
          if isSpace(letter_map):
            for letter in letter_map:
                if letter_map[letter] == True:
                    letter_map[letter] == False
                    words_seen.append(word)
          else:
              return False 
    return True 

def isSpace(_map):
    for key in _map:
        if _map[key] == True:
            return True
    return False


    
    
    
    
    
    #print(len(letter_map), len(word_map), words, letter_map, word_map)
    # for word in words:
    #     if word not in words_seen:
    #         safe = False
    #         for char in pat_map:
    #             # ensures that each char maps to at most one word 
    #             if len(pat_map[char]) == 0:
    #                 pat_map[char].append(word)
    #                 words_seen.append(word)
    #                 safe = True
    #                 break
    #         if safe == False:
    #             return False
    # for char in pattern:
    #     if char not in chars_seen:
    #         safe = False
    #         for word in word_map:
    #             # ensures that each word maps to at most one char 
    #             if len(word_map[word]) == 0:
    #                 word_map[word].append(char)
    #                 safe = True
    #                 break
    #         if safe == False:
    #             return False 
    # return True 