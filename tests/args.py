from args import Args
from unittest import TestCase


class Test_args(TestCase):

    def test_all(self):
        args = Args(args=['a','b','-a','a1','a2','--c','c1','c2'])
        expected = ['b','-a','a1','a2','--c','c1','c2']
        self.assertEqual(args.args(),expected)


    def test_one_flag(self):
        args = Args(args=['a','b','-a','a1','a2','--c','c1','c2'])
        self.assertEqual(args.args('a'),['a1','a2'])


    def test_double_flag(self):
        args = Args(args=['a','b','-a','a1','a2','--c','c1','c2'])
        self.assertEqual(args.args('a','c'),['a1','a2','c1','c2'])

    def test_Inesiscente_flag(self):
        args = Args(args=['a','b','-a','a1','a2','--c','c1','c2'])
        self.assertEqual(args.args('#'),[])

    def test_list(self):
        args = Args(args=['a','b','-a','a1','a2','--c','c1','c2'])
        self.assertEqual(args.args(['a']),['a1','a2'])


    def test_tuple(self):
        args = Args(args=['a','b','-a','a1','a2','--c','c1','c2'])
        self.assertEqual(args.args(('a')),['a1','a2'])
  
    def test_invalid_args(self):
        args = Args(args=['a','b','-a','a1','a2','--c','c1','c2'])
        self.assertRaises(TypeError,lambda:args.args(1,2,3))

  


