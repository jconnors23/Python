def isAnagram(s, t):
    if len(s) != len(t):
        return False
    chars_t = {char: 0 for char in t}
    for char in t:
        chars_t[char]+=1
    chars_s = {char: 0 for char in s}
    for char in s:
        chars_s[char]+=1
    return chars_t == chars_s
