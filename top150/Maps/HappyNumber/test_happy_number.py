from happy_number import isHappy

def test_isHappy():
    assert isHappy(19) == True
    assert isHappy(2) == False
    assert isHappy(7) == True
    assert isHappy(1111111) == True 