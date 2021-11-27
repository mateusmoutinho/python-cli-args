from unittest import TestCase
from cli_args_system.args import Args


class TestArgsFlagsContent(TestCase):

    def test_none(self):
        args = Args(args=['a', 'b', 'c'])
        flag = args.flags_content()
        self.assertFalse(flag.exist)

    def test_empty_flag(self):
        args = Args(args=['a', '-b'])
        flag = args.flags_content('b')
        self.assertTrue(flag.exist)
        self.assertFalse(flag.filled)

    def test_filled_flag(self):
        args = Args(args=['a', '-b', 'b1', 'b2'])
        flag = args.flags_content('b')
        self.assertTrue(flag.exist)
        self.assertTrue(flag.filled)
        self.assertListEqual(flag._args, ['b1', 'b2'])

    def test_synonym(self):
        args = Args(args=['a', '-out', 'a.txt', 'b.txt'])
        flag = args.flags_content('out', 'out-file', 'o')
        self.assertListEqual(flag._args, ['a.txt', 'b.txt'])

    def test_double_synonym(self):
        args = Args(args=['a', '-out', 'a.txt', 'b.txt', '-o', 'c.txt'])
        flag = args.flags_content('out', 'out-file', 'o')
        self.assertListEqual(flag._args, ['a.txt', 'b.txt', 'c.txt'])
