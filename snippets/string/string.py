# -*- coding: utf-8 -*-


'''Snippets for string.

Available functions:
- get_offset  : Get offset between the base_alphabet and alphabet.
- to_titlecase: Convert the character string to titlecase.
'''


def get_offset(alphabet: str, base_alphabet: str = 'A') -> int:
    '''Get offset between the base_alphabet and alphabet.

    Args:
        alphabet: The alphabet to use. 
        base_alphabet: The base alphabet to use.

    Returns:
        difference between the base_alphabet and alphabet.
    
    See:
    https://docs.python.org/3.11/library/functions.html?highlight=chr#ord
    '''   

    return ord(alphabet) - ord(base_alphabet)


def to_titlecase(s: str) -> str:
    '''For example:
        >>> 'Hello world'.title()
        'Hello World'

    Args:
        str: String excluding apostrophes in contractions and possessives
             form word boundaries.

    Returns:
        A titlecased version of the string where words start with an
        uppercase character and the remaining characters are lowercase.

    See:
        https://docs.python.org/3.6/library/stdtypes.html#str.title
    '''

    return s.title()
