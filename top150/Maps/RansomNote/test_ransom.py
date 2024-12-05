from ransom import canConstruct

def test_construction():
    assert canConstruct("a", "b") == False
    assert canConstruct("aa", "ab") == False
    assert canConstruct("aa", "aab") == True