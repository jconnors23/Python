from typing import Dict, List
# thanks apple 
# S = [T, H, A, N, K] T = [A, P, P, L, E]
# mapped [ {
#  t: [a]
 #  h: [p]
#     a: [p ]
#}]
def sameShape(s, t):
    s, t = list(s), list(t)
    mapped_s: Dict[str, List[str]] = {char: [] for char in s}
    mapped_t: Dict[str, List[str]] = {char: [] for char in t}
    for i in range(len(s)):
        s_char, t_char = s[i], t[i]
        # if t_char in mapped_s[s_char] or s_char in mapped_t[t_char]:
        #     return False
        if t_char not in mapped_s[s_char]:
            mapped_s[s_char].append(t_char)
        if s_char not in mapped_t[t_char]:
            mapped_t[t_char].append(s_char)                    
    for key in mapped_s:
        if len(mapped_s[key]) > 1:
            return False 
    for key in mapped_t:
        if len(mapped_t[key]) > 1:
            return False 
    # print(f"s map: {mapped_s}\n")
    # print(f"t map: {mapped_t}\n")
    return True 
