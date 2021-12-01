from unittest import TestCase
from cli_args_system.flags_content import FlagsContent


class TestFlagsContent(TestCase):

    def test_exist(self):
        flag = FlagsContent(content=[])
        self.assertTrue(flag.exist())

    def test_not_exist(self):
        flag = FlagsContent(content=None)
        self.assertFalse(flag.exist())

    def test_filled(self):
        flag = FlagsContent(content=['a', 1])
        self.assertTrue(flag.filled())

    def test_not_filled(self):
        flag = FlagsContent(content=[])
        self.assertFalse(flag.filled())
      
    def test_exist_and_empty(self):
        flag = FlagsContent(content=[])
        self.assertTrue(flag.exist_and_empty())

        flag2 = FlagsContent(content=None)
        self.assertFalse(flag2.exist_and_empty())
        
        flag3 = FlagsContent(content=['a','b'])
        self.assertFalse(flag3.exist_and_empty())

    def test_flags(self):
        flag = FlagsContent(content=['a.txt'])
        self.assertListEqual(flag.flags(),['a.txt'])
      