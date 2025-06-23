#Check if any word in a sentence contains duplicate letters.
def has_duplicate_letters(sentence):
    for word in sentence.split():
        if len(set(word)) < len(word):
            return True
    return False

print(has_duplicate_letters("apple banana car"))
