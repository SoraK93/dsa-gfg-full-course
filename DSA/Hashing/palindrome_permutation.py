"""Check for Palindrome Permutation"""
from collections import Counter

NO_OF_CHAR = 256


def has_palindrome(text):
    """Using collections.Counter() to store count of all distinct characters,
    later check if there is more than 1 odd count"""
    count = Counter(text)
    odd = 0
    for key in count.values():
        if key % 2 != 0:
            odd += 1
            if odd > 1:
                return False
    return True


def can_form_palindrome(text):
    """Using ASCII to store count of occurrence in an array, later checking if there is more than 1 odd count"""
    count = [0] * NO_OF_CHAR
    for char in text:
        count[ord(char)] += 1

    odd = 0
    for cnt in count:
        if cnt & 1:
            odd += 1
        if odd > 1:
            return False
    return True


word = "geeksgeeks"

print(has_palindrome(word))
print(can_form_palindrome(word))
