from unittest import TestCase
from list_args import ListArgs



class Test_ListArgs(TestCase):
    
    def test_lists(self):
        list_object = ListArgs()
        list_object.args = ['a','b','c','d']
        self.assertTrue(list_object == ['a','b','c','d'] )
        self.assertFalse(list_object == [1,2])


    def test_size(self):
        list_object = ListArgs()
        list_object.args = ['a','b','c','d']
        self.assertTrue(list_object == 4)
        self.assertFalse(list_object == 3)
        self.assertTrue(list_object > 2)
        self.assertTrue(list_object >= 4)
        self.assertTrue(list_object < 10)
        self.assertTrue(list_object <= 4)

    def test_in(self):
        list_object = ListArgs()
        list_object.args = ['a','b','c','d']
        self.assertTrue('b' in list_object)
        self.assertFalse('x' in list_object)
        self.assertTrue('x' not in list_object)

    def test_index(self):
        list_object = ListArgs()
        list_object.args = ['a','b','c','d']
        b = list_object[1]
        self.assertEqual(b,'b')
        d = list_object[-1]
        self.assertEqual(d,'d')
        