# -*- coding: utf-8 -*-
'''Snippets for prime.

Available functions:
- is_included: Determine whether it is a prime number.
'''


class Prime(object):
    '''Represents a snippet for prime numbers.
    '''

    def __init__(self, number):
        self.number = number

    def is_included(self) -> bool:
        '''Determine whether it is a prime number.

        Args:
            number: Int of number (greater than 0).

        Returns:
            True if the input number was prime.
            False if the input number was not prime.

        See:
            https://qiita.com/srtk86/items/874639e361917e5016d4
            https://docs.python.org/ja/3/library/2to3.html?highlight=isinstance#2to3fixer-isinstance
        '''

        from math import sqrt

        if (self.number <= 1) or (isinstance(self.number, float)):
            return False

        for i in range(2, int(sqrt(self.number)) + 1):
            if self.number % i == 0:
                return False

        return True
