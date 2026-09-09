def has_all_vowels(word):
    required = {"a", "e", "i", "o", "u"}
    word = word.lower()

    word_set = set(word)
    return required.issubset(word_set)
    
print(has_all_vowels('education'))
print(has_all_vowels('hello'))