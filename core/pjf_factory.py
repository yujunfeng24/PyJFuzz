"""
The MIT License (MIT)

Copyright (c) 2016 Daniele Linguaglossa <d.linguaglossa@mseclab.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from errors import PJFInvalidType


class JsonFactory(object):

    def __init__(self, other):
        """
        Class that represent a JSON object
        """
        if type(other) == dict:
            for k in other:
                if type(other[k]) == dict:
                    other[k] = JsonFactory(other[k])
            self.__dict__ = other
        else:
            raise PJFInvalidType(other, dict)

    def __add__(self, other):
        """
        Add keys to dictionary merging with another dictionary object
        """
        self.__dict__.update(other)
        return self

    def __sub__(self, other):
        """
        Removes keys from self dictionary based on provided list
        """
        if type(other) == list:
            for element in other:
                if element in self.__dict__:
                    del self.__dict__[element]
            return self
        else:
            raise PJFInvalidType(other, list)

    def __eq__(self, other):
        """
        Check if two object are equal
        """
        return self.__dict__ == other

    def __getitem__(self, item):
        """
        Extract an item from the JSON object
        """
        if type(item) == str:
            return self.__dict__[item]
        else:
            return self.__dict__

    def __setitem__(self, key, value):
        """
        Set a JSON attribute
        """
        self.__dict__[key] = value

    def __contains__(self, items):
        """
        Check if JSON object contains a key
        """
        if type(items) != list:
            raise PJFInvalidType(items, list)
        ret = 0
        for item in items:
            for key in self.__dict__:
                if isinstance(self.__dict__[key], JsonFactory):
                    ret += item in self.__dict__[key]
                elif item == key:
                    ret += 1
        return len(items) == ret

    def __repr__(self):
        """
        Represent the JSON object
        """
        return str(self.__dict__)
