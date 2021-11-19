from args import Args
from unittest import TestCase

class Test_Flags(TestCase):

    def test_all(self):
        args = Args(args=['a','b','-a','a1','a2'])
        expected = {
            'default':['b'],
            'a':['a1','a2']
        }
        self.assertEqual(args.flags(),expected)


    def test_especific(self):
        args = Args(args=['a','b','-a','a1','a2','--c','c1','c2'])
        expected = {
            'c':['c1','c2']
        }
        self.assertEqual(args.flags('c'),expected)


    def test_double(self):
        args = Args(args=['a','b','-a','a1','a2','--c','c1','c2'])
        expected = {
            'a':['a1','a2'],
            'c':['c1','c2']
        }
        self.assertEqual(args.flags('c','a'),expected)


    def test_with_not_exist(self):
        args = Args(args=['a','b','-a','a1','a2','-2.5','-3','c1','c2'])
        expected = {
            'a':['a1','a2',-2.5,-3,'c1','c2'],
            '#':None
        }
        self.assertEqual(args.flags('#','a'),expected)


    def test_with_list(self):
        args = Args(args=['a','b','-a','a1','a2','--c','c1','c2'])
        expected = {
            'a':['a1','a2'],
            'c':['c1','c2']
        }
        self.assertEqual(args.flags(['c','a']),expected)


    def test_with_tuple(self):
        args = Args(args=['a','b','-a','a1','a2','--c','c1','c2'])
        expected = {
            'a':['a1','a2'],
            'c':['c1','c2']
        }
        self.assertEqual(args.flags(('c','a')),expected)


    def test_with_invalid_type(self):
        args = Args(args=['a','b','-a','a1','a2','--2','c1','c2'])
        self.assertRaises(TypeError,lambda: args.flags(2,[1,2,3]))
        