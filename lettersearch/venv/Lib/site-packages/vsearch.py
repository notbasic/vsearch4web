

def search4vowels(phrase: str) ->set:
    """Display any vowels found in the an asked-for word"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

search4vowels('hitch-hiker')


def search4letters(phrase: str, letters: str = 'aeiou') ->set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))

search4letters('hitch-hiker','r')