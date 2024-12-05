import pytest
from reverse_words import Solution

@pytest.fixture
def solution():
    return Solution()

def test_reverse_words_single_word(solution):
    assert solution.reverseWords("hello") == "hello"

def test_reverse_words_multiple_words(solution):
    assert solution.reverseWords("hello world") == "world hello"

def test_reverse_words_with_extra_spaces(solution):
    assert solution.reverseWords("  hello   world  ") == "world hello"

def test_reverse_words_empty_string(solution):
    assert solution.reverseWords("") == ""

def test_reverse_words_only_spaces(solution):
    assert solution.reverseWords("     ") == ""

def test_reverse_words_with_punctuation(solution):
    assert solution.reverseWords("hello, world!") == "world! hello,"

def test_reverse_words_with_newlines(solution):
    assert solution.reverseWords("hello\nworld") == "world hello"

def test_reverse_words_with_tabs(solution):
    assert solution.reverseWords("hello\tworld") == "world hello"