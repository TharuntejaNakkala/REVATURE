"""Find the length of the longest substring without repeating characters in a given string."""
def length_of_longest_substring(s):
    seen = {}
    start = max_len = 0
    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = i
        max_len = max(max_len, i - start + 1)
    return max_len


input_str = "abcabcbb"
output = length_of_longest_substring(input_str)
print("Length of Longest Unique Substring:", output)
