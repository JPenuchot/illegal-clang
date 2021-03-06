import lldb
from lldbsuite.test.decorators import *
from lldbsuite.test.lldbtest import *
from lldbsuite.test import lldbutil


class TestCase(TestBase):

    mydir = TestBase.compute_mydir(__file__)

    @skipUnlessDarwin
    @no_debug_info_test
    def test_keyword(self):
      # Make sure that C++ keywords work in the expression parser when using
      # Objective-C++.
      self.expect("expr -l objective-c++ -- constexpr int i = 3 + 3; i", substrs=["= 6"])
