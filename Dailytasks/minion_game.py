"""Play a game where:

Kevin scores using substrings starting with vowels.

Stuart scores using substrings starting with consonants"""

def minion_game(string):
    vowels = 'AEIOU'
    kevin = sum(len(string) - i for i in range(len(string)) if string[i] in vowels)
    stuart = sum(len(string) - i for i in range(len(string)) if string[i] not in vowels)
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

minion_game("BANANA")
