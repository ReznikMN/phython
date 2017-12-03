def search4vowels(phrase:str) -> set:
 """Возвращает гласные, найденные в указанном слове."""
vowels = set('aeiou')
return vowels.intersection(set(phrase))