from unittest import TestCase
from flags_content import FlagsContent


class TestFlagsContent(TestCase):

    def test_exist(self):
        flag = FlagsContent(content=[])
        self.assertTrue(flag.exist)

    def test_not_exist(self):
        flag = FlagsContent(content=None)
        self.assertFalse(flag.exist)

    def test_filled(self):
        flag = FlagsContent(content=['a',1])
        self.assertTrue(flag.filled)

    def test_not_filled(self):
        flag = FlagsContent(content=[])
        self.assertFalse(flag.filled)