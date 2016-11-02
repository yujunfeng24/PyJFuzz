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

class PJFBaseException(BaseException):
    """
    Base Exception class
    """
    def __init__(self, message, errors=None):
        super(PJFBaseException, self).__init__(message)
        self.errors = errors

class PJFEnvironmentError(PJFBaseException):
    """
    Environment error e.g. missing dependencies
    """
    pass

class PJFMissingDependency(PJFEnvironmentError):
    """
    Missing dependency
    """
    pass

class PJFInvalidArgument(PJFBaseException):
    """
    Invalid argument passed to PyJFuzz
    """
    pass

class PJFMissingArgument(PJFInvalidArgument):
    """
    Invalid argument due to object type
    """
    def __init__(self):
        message = "Some arguments are missing"
        super(PJFInvalidArgument, self).__init__(message, None)

class PJFInvalidType(PJFInvalidArgument):
    """
    Invalid argument due to object type
    """
    def __init__(self, obj, expected):
        message = "Invalid object type ({0}) expecting ({1})".format(type(obj).__name__, expected.__name__)
        super(PJFInvalidType, self).__init__(message, None)

