from word_pattern import isBijective

def test_isBijective():
    assert isBijective(pattern = "abba", s = "dog cat cat fish") == False
    assert isBijective(pattern = "aaaa", s = "dog cat cat dog") == False
    assert isBijective(pattern = "abba", s = "dog cat cat dog") == True
    assert isBijective(pattern = "abba", s = "dog dog dog dog") == False 