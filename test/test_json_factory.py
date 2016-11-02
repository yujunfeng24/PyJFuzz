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
from core.pjf_factory import JsonFactory

__TITLE__ = "Testing JsonFactory Object"

class TestJsonFactory(unittest.TestCase):

    def test_nested_object(self):
        self.assertTrue(JsonFactory({"t": 1, "foo": {"cow": True}}))

    def test_object_subtraction(self):
        json = JsonFactory({"test": 1, "test2": {"nested": 1}})
        json["test2"] = json["test2"] - ["nested"]
        self.assertTrue(json == {"test": 1, "test2": {}})
        self.assertFalse(json == {"test": 1, "test2": {"nested": 1}})

    def test_object_addition(self):
        json = JsonFactory({"a": 1})
        json += {"foo": True}
        self.assertTrue(json["foo"])

    def test_object_equal(self):
        json = JsonFactory({"a": 1})
        self.assertEquals(json, {"a": 1})
        self.assertNotEqual(json, {"a": 0})

    def test_object_contains(self):
        json = JsonFactory({"a": 1})
        self.assertTrue(["a"] in json)
        self.assertFalse(["A"] in json)

    def test_object_setitem(self):
        json = JsonFactory({"a": False})
        json["a"] = True
        self.assertTrue(json["a"])

    def test_object_representation(self):
        json = JsonFactory({"a": 1})
        self.assertTrue(str(json) == "{'a': 1}")
        self.assertTrue(type(str(json)) == str)

def test():
    print "=" * len(__TITLE__)
    print __TITLE__
    print "=" * len(__TITLE__)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestJsonFactory)
    unittest.TextTestRunner(verbosity=2).run(suite)
