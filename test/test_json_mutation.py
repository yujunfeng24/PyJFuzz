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

import unittest
from core.pjf_mutation import JsonMutation

__TITLE__ = "Testing JsonMutation object"

class TestJsonMutation(unittest.TestCase):

    def test_string_mutation(self):
        with self.assertRaises(Exception):
            JsonMutation("TEST", 6).fuzz()
            raise Exception

    def test_boolean_mutation(self):
        with self.assertRaises(Exception):
            JsonMutation(False, 6).fuzz()
            raise Exception

    def test_int_mutation(self):
        with self.assertRaises(Exception):
            JsonMutation(1337, 6).fuzz()
            raise Exception

    def test_float_mutation(self):
        with self.assertRaises(Exception):
            JsonMutation(1337.56, 6).fuzz()
            raise Exception

    def test_null_mutation(self):
        with self.assertRaises(Exception):
            JsonMutation(None, 6).fuzz()
            raise Exception

def test():
    print "=" * len(__TITLE__)
    print __TITLE__
    print "=" * len(__TITLE__)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestJsonMutation)
    unittest.TextTestRunner(verbosity=2).run(suite)
