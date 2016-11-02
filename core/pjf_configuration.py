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

from argparse import Namespace

class JsonConfiguration(Namespace):
    """
    A class that represent PyJFuzz startup configuration , it makes the standard checks
    """
    def __init__(self, namespace):
        """
        Start PyJFuzz based on configuration
        """
        super(JsonConfiguration, self).__init__(**namespace.__dict__)


import argparse
import sys

sys.argv.append("--j")
sys.argv.append("1")
sys.argv.append("--F")
sys.argv.append("2")

parser = argparse.ArgumentParser(description='Trivial Python JSON Fuzzer (c) DZONERZY',
                                     formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('--j', metavar='JSON', help='Original JSON serialized object', type=str, default=None)
parser.add_argument('--F', metavar='FILE', help='Fuzz a file', type=str, default=None)
parser.add_argument('--m', metavar='COMMAND', help='Process command to start and monitor', type=str, required=False)
parser.add_argument('--update', action='store_true', help='Check for updates', dest='update', default=False,
                       required=False)

parsed = parser.parse_args()
args = JsonConfiguration(parsed)


print args.__dict__ == parsed.__dict__
