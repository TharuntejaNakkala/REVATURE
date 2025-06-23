"""Write a function that groups a list of words into sets of anagrams. Two words are anagrams if they contain the same characters in different order."""
from collections import defaultdict

def group_anagrams(words):
    res = defaultdict(list)
    for word in words:
        res[tuple(sorted(word))].append(word)
    return list(res.values())


input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = group_anagrams(input_words)
print("Grouped Anagrams:", output)
