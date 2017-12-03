vowels = set('aeiou')
word = input("Provide a word to search fo vowels:")
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)


