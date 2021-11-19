from args import Args
from unittest import TestCase


class Args(TestCase):
    
    def test_numbers(self):
        args = Args(args=['a','b','-a','a1','a2'])
        self.assertEqual('c',args[0])
        self.assertEqual('-b',args[1])
        self.assertEqual('a2',args[-1])
       
    def test_slices(self):
        args = Args(args=['a','b','-a','a1','a2'])
        self.assertEqual(['c'],args[0:1])
   
