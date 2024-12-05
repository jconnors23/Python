from is_anagram import isAnagram

def test_isAnagram():
    assert isAnagram(s = "anagram", t = "nagaram") == True
    assert isAnagram(s = "rat", t = "car") == False
    assert isAnagram(s = "cinema", t = "iceman") == True