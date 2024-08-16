# given a string {"1,2,3"} convert to [1, 2, 3]

class Solution():
    def string_to_split(s):
        s_new = s.split(",")
        return s_new 

print(Solution.string_to_split("1,2,3,4"))
            
