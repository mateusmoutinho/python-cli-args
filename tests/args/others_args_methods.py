from unittest import TestCase
from cli_args.args import Args


class GetItem(TestCase):

    def test_numbers(self):
        args = Args(args=['a', 'b', '-a', 'a1', 'a2', '-1', 'c1', 'c2'])
        self.assertEqual(args[0], 'b')
        self.assertEqual(args[1], '-a')
        self.assertEqual(args[-1], 'c2')

    def test_slices(self):
        args = Args(args=['a', 'b', '-a', 'a1', 'a2', '--c', 'c1', 'c2'])
        self.assertEqual(['b', '-a'], args[0:2])

    def test_none_numbers(self):
        args = Args(args=['a', 'b', '-a', 'a1', 'a2', '--c', 'c1', 'c2'])
        self.assertRaises(IndexError, lambda: args[20])


class TestFlagsNames(TestCase):

    def test_flags_name(self):
        args = Args(args=['a', 'b', '-a', 'a1', 'a2', '--c', 'c1', 'c2'])
        self.assertEqual(args.flags_names, ['default', 'a', 'c'])


class TestLen(TestCase):

    def test_flags_name(self):
        args = Args(args=['a', 'b', 'c'], consider_first=True)
        self.assertEqual(len(args), 3)
        args = Args(args=['a', 'b', 'c'])
        self.assertEqual(len(args), 2)
