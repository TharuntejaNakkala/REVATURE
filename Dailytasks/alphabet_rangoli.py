#Print a rangoli (pattern) using the alphabet up to a given size.
def print_pattern(size):
    width = size * 4 - 3

    def generate_line(n):
        letters = [chr(ord('a') + i) for i in range(size - 1, size - 1 - n, -1)]
        mid = letters + letters[-2::-1]
        return '-'.join(mid).center(width, '-')

    for i in range(1, size):
        print(generate_line(i))

    letters = [chr(ord('a') + i) for i in range(size - 1, -1, -1)]
    full = letters + letters[1:]
    print('-'.join(full).center(width, '-'))

    for i in range(size - 1, 0, -1):
        print(generate_line(i))

print("Size 3 pattern:\n")
print_pattern(3)

print("\nSize 5 pattern:\n")
print_pattern(5)
