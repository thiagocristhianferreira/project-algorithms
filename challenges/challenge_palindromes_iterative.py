def is_palindrome_iterative(word):
    if not word:
        return False
    # word[::-1] => interte a string
    if word == word[::-1]:
        return True
    return False
