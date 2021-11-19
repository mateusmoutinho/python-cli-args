from args import Args
from unittest import TestCase

class Args_Construction(TestCase):

    def test_all_true(self):
        args = Args(
            consider_first=True,
            case_sensitive=True,
            flag_identifier='-',
            convert_numbers=True,
            infinity_indentifier=True,
            args=['A','B','c','-A','1','2','3','--B','b1','B2','b3']
        )
        dict_espected = {
            'default':['A','B','c'],
            'A':[1,2,3],
            'B':['b1','B2','b3']
        }
        self.assertDictEqual(args.flags(),dict_espected)
        list_espected = ['A','B','c','-A',1,2,3,'--B','b1','B2','b3']
        self.assertListEqual(args.args(),list_espected)  

    def test_all_false(self):
        args = Args(
            consider_first=False,
            case_sensitive=False,
            flag_identifier='#',
            convert_numbers=False,
            infinity_indentifier=False,
            args=['A','B','c','#A','1','2','3','##B','b1','B2','b3']
        )
        dict_espected = {
            'default':['b','c'],
            'a':['1','2','3'],
            '#b':['b1','b2','b3']
        }
        self.assertDictEqual(args.flags(),dict_espected)
        list_espected = ['b','c','#a','1','2','3','##b','b1','b2','b3']
        self.assertListEqual(args.args(),list_espected)  


    def aaa_default(self):
        args = Args(
            consider_first=False,
            case_sensitive=False,
            flag_identifier='#',
            convert_numbers=False,
            infinity_indentifier=False,
            args=['A','B','c','#A','1','2','3','##B','b1','B2','b3']
        )
        dict_espected = {
            'default':['b','c'],
            'a':['1','2','3'],
            '#b':['b1','b2','b3']
        }
        self.assertDictEqual(args._flags,dict_espected)
        list_espected = ['b','c','#a','1','2','3','##b','b1','b2','b3']
        self.assertListEqual(args._args,list_espected)  
