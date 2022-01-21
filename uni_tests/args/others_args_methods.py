from unittest import TestCase
from cli_args_system.args import Args
from json import dumps

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
        self.assertEqual(args.flags_names(include_default=True), ['default', 'a', 'c'])
        self.assertEqual(args.flags_names(include_default=False), [ 'a', 'c'])




class TestLen(TestCase):

    def test_len(self):
        args = Args(args=['a', 'b', 'c'], consider_first=True)
        self.assertEqual(len(args), 3)
        args = Args(args=['a', 'b', 'c'])
        self.assertEqual(len(args), 2)

class TestArgs(TestCase):

    def test_args_method(self):
        args = Args(args=['a', 'b', 'c','1'])
        self.assertListEqual(args.args(),['b','c',1])
      
      
class TestFlags(TestCase):

    def test_flags_method(self):
        args = Args(args=['a','a1', '-b', 'c','1'])
        expected = {
            'default':['a1'],
            'b':['c',1]
        }
        self.assertDictEqual(args.flags_dict(),expected)
      

      

class TestTotal_flags(TestCase):

    def test_total_flags(self):
        args = Args(args=['a', 'b', 'c'])
        self.assertEqual(args.total_flags(include_default=False), 0)

        args = Args(args=['a', '-b', 'c'])
        self.assertEqual(args.total_flags(), 1)
        args = Args(args=['a', '-b', '-c'])
        self.assertEqual(args.total_flags(), 2)

        #test default inclusion
        args = Args(args=['a', '-b', '-c'])
        self.assertEqual(args.total_flags(include_default=True), 3)



class TestUnusedFlags(TestCase):

    def test_unused(self):
        args = Args(args=['a','a1', '-b', 'c','1'])
        b = args.flags_content('b')
        expected = {
            'default':['a1']
        }
        self.assertDictEqual(args.unused_flags(),expected)

    def test_unused_with_flag_str(self):
        args = Args(args=['a','a1', '-b', 'c','1'])
        b = args.flag_str("b")
        expected = {
            'default':['a1']
        }
        self.assertDictEqual(args.unused_flags(),expected)

    def test_unused_with_nothing(self):
        args = Args(args=['a','a1', '-b', 'c','1'])
        expected = {
            'default':['a1'],
            'b':['c',1]
        }
        self.assertDictEqual(args.unused_flags(),expected)



class TestFlagContent(TestCase):

    def test_finded(self):
        args = Args(args=['a','a1', '-b', 'value of b'])
        b = args.flag_str('b')
        self.assertEqual(b, 'value of b')

    def test_finded_number(self):
        args = Args(args=['a','a1', '-b', 10])
        b = args.flag_str('b')
        self.assertEqual(b, 10)

    def test_none(self):
        args = Args(args=['a','a1', '-b', 10])
        b = args.flag_str('c')
        self.assertIsNone(b,None)


class TestUnusedFlagsNames(TestCase):

    def test_unused_flags_names(self):
        args = Args(args=['a','a1', '-b', '-c','1'])
        self.assertListEqual(args.unused_flags_names(),['b','c'])
        self.assertListEqual(args.unused_flags_names(
            include_default=True),
            ['default','b','c']
        )

        b = args.flags_content('b')
        self.assertListEqual(args.unused_flags_names(),['c'])
        self.assertListEqual(
            args.unused_flags_names(include_default=True),
        ['default','c']
        )



class TestTotalUnusedFlags(TestCase):

    def test_unused_flags_names(self):
        args = Args(args=['a','a1', '-b', '-c','1'])
        self.assertEqual(args.total_flags(),2)
        self.assertEqual(args.total_flags(include_default=True),3)
        b = args.flags_content('b')
        self.assertEqual(args.total_unused_flags(),1)   
        self.assertEqual(args.total_unused_flags(include_default=True),2)   
    