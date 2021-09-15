def is_palindrome_iterative(word):
    if not word:
        return False
    reverse_word = ''
    for letter in (range(len(word) - 1, - 1, - 1)):
        reverse_word += word[letter]
    if reverse_word == word.upper():
        return True
    return False
