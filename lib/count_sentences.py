#!/usr/bin/env python3

class MyString:


    def __init__(self, value=""):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")
            self._value = ""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        '''Returns True if the value ends with a period.'''
        return self._value.endswith('.')

    def is_question(self):
        '''Returns True if the value ends with a question mark.'''
        return self._value.endswith('?')

    def is_exclamation(self):
        '''Returns True if the value ends with an exclamation mark.'''
        return self._value.endswith('!')

    def count_sentences(self):
        '''Counts the number of sentences in the value.'''
        if not self._value:
            return 0
        
        sentence_endings = {'.', '!', '?'}
        count = 0
        for char in self._value:
            if char in sentence_endings:
                count += 1
        return count
 
