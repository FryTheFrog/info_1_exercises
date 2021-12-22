#!/usr/bin/env python3

import builtins, sys
from unittest import TestCase

# replace input implementation
class YouCannotUseInputInACCESSException(Exception): pass
def crashing_input(prompt):
    raise YouCannotUseInputInACCESSException()
builtins.input_orig = builtins.input
builtins.input = crashing_input

# catch potential exception from import
import_ex = None
try:
    from public.script import ProfanityFilter
except:
    import_ex = sys.exc_info()[0].__name__

class PrivateSmokeTestSuite(TestCase):

    def _run_example(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEquals(expected, actual)

    def test0_example(self):
        if import_ex:
            m = "@@Failed to import the implementation of ProfanityFilter due to an '{}'.@@".format(import_ex)
            self.fail(m)

        try:
            self._run_example()
        except AssertionError:
            m = "@@Running the provided example has an incorrect result. Make sure that " +\
                "the public test suite passes, before you attempt any submissions.@@"
            self.fail(m)
        except:
            m = "@@Failed to run the provided example. Make sure that the public test" +\
                "suite passes, before you attempt any submissions.@@"
            self.fail(m)

    def test1_repeatability(self):
        try:
            self._run_example()
            self._run_example()
        except:
            m = "@@Failed to run the provided example a second time. This might be caused by shared " +\
                "class variables that introduce unexpected side effects. We highly encourage you to " +\
                "add your own tests to the public test suite before you attempt any submissions.@@"
            self.fail(m)
