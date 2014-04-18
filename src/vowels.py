
def get_words():
    """Returns a Python-list of words from the wordlist.txt"""
    with open('wordlist.txt', 'r') as f:
        return list(f.readlines())


def ordered_vowels():
    """Checks words for ordered vowels.
    
    Accepts a list of words and returns only those which have all of the
    vowels a-e-i-o-u-y in alphabetical order.

    For bonus, add the paramater `andY=False` to additionally return those
    words that have just a-e-i-o-u.
    """
    

    return
