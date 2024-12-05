from same_shape import sameShape

def test_sameShape():
    assert sameShape("thank", "apple") == False
    assert sameShape("s", "r") == True
    assert sameShape("foo", "bar") == False
    assert sameShape("foe", "bar") == True