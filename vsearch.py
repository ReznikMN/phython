def search4vowels(phrase:str) -> set:
   """Возвращает гласные, найденные в указанном слове."""
   vowels = set('aeiou')
   return vowels.intersection(set(phrase))


def search4letters(phrase:str, letters:str='aeiou') -> set :
    """Возвращает гласные, найденные в указанном слове."""
    return  set(letters).intersection(set(phrase))