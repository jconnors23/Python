import pytest
from find_first import Solution

@pytest.fixture
def solution():
    return Solution()

def test_strStr_found(solution):
    assert solution.strStr("hello", "ll") == 2

def test_strStr_not_found(solution):
    assert solution.strStr("hello", "world") == -1

def test_strStr_empty_needle(solution):
    assert solution.strStr("hello", "") == 0

def test_strStr_empty_haystack(solution):
    assert solution.strStr("", "a") == -1

def test_strStr_both_empty(solution):
    assert solution.strStr("", "") == 0

def test_strStr_needle_at_start(solution):
    assert solution.strStr("hello", "he") == 0

def test_strStr_needle_at_end(solution):
    assert solution.strStr("hello", "lo") == 3

def test_strStr_needle_longer_than_haystack(solution):
    assert solution.strStr("hi", "hello") == -1