#Convert each character in a string to its 2-digit hexadecimal ASCII code.
def ascii_to_hex(s):
    return ' '.join(format(ord(c), '02x') for c in s)

print(ascii_to_hex("Hi"))

