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

import subprocess
import shlex
from core.pjf_factory import JsonFactory
from errors import PJFMissingArgument


class JsonExternalFuzzer(object):
    """
    Represent an instance of an external command line fuzzer
    """

    def __init__(self, **kwargs):
        """
        Init the class with fuzzer name (command), a boolean that represent whenever the fuzzer
        accept arguments form stdin, otherwise specify a command line. The special keyword "@@"
        will be replaced with the content of argument to fuzz
        """
        self.config = JsonFactory(kwargs)
        if not ["fuzzer", "stdin", "commandline"] in self.config:
            raise PJFMissingArgument()

    def execute(self, obj):
        """
        Perform the actual external fuzzing, you may replace this method in order to increase performance
        """
        cmdline = shlex.split(self.config["commandline"])
        if self.config["stdin"]:
            fuzzer = subprocess.Popen([self.config["fuzzer"]] + cmdline, stderr=subprocess.PIPE,
                                      stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            fuzzer.stdin.write(obj)
        else:
            if "@@" not in cmdline:
                raise PJFMissingArgument()
            cmdline[cmdline.index("@@")] = obj
            fuzzer = subprocess.Popen([self.config["fuzzer"]] + cmdline, stderr=subprocess.PIPE,
                                      stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        result = fuzzer.communicate()[0]
        fuzzer.wait()
        fuzzer.stdin.close()
        fuzzer.stdout.close()
        fuzzer.stderr.close()
        del fuzzer
        return result
