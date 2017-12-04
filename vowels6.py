<<<<<<< Updated upstream
vowels=['a','e','i','o','u',]
word=input("Provide a word to search fo vowels:")
=======
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search fo vowels:")
>>>>>>> Stashed changes
found = {}
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
<<<<<<< Updated upstream
        found[letter]+=1
for k,v in sorted(found.items()):
    print(k, 'was found', v,'time(s).')
print('fuck them all!')
=======
        found[letter] += 1
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')
>>>>>>> Stashed changes
