from args import Args
from unittest import TestCase

class Test_Construction(TestCase):

    def test_all_true(self):
        args = Args(
            consider_first=True,
            args_case_sensitive=True,
            flags_case_sensitive=True,
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
        self.assertDictEqual(args.flags,dict_espected)
        list_espected = ['A','B','c','-A',1,2,3,'--B','b1','B2','b3']
        #testing args 
        self.assertListEqual(args.args,list_espected)  
        #testing keys
        self.assertListEqual(args.flags_names,['default','A','B'])


    def test_all_false(self):
        args = Args(
            consider_first=False,
            args_case_sensitive=False,
            flags_case_sensitive=False,
            flag_identifier='#',
            convert_numbers=False,
            infinity_indentifier=False,
            args=['A','B','c','#A','1','2','3','###B','b1','B2','b3']
        )
        dict_espected = {
            'default':['b','c'],
            'a':['1','2','3'],
            '##b':['b1','b2','b3']
        }
        self.assertDictEqual(args.flags,dict_espected)
        list_espected = ['b','c','#a','1','2','3','###b','b1','b2','b3']
        #testing args
        self.assertListEqual(args.args,list_espected)  
        #testing keys
        self.assertListEqual(args.flags_names,['default','a','##b'])
    

    def test_default(self):
        args = Args(args=['A','B','c','-A','1','2.3','3','--B','b1','B2','b3'])
        dict_espected = {
            'default':['B','c'],
            'a':[1,2.3,3],
            'b':['b1','B2','b3']
        }
        self.assertDictEqual(args.flags,dict_espected)
        list_espected = ['B','c','-A',1,2.3,3,'--B','b1','B2','b3']
        self.assertListEqual(args.args,list_espected)  
        self.assertListEqual(args.flags_names,['default','a','b'])
    

    def test_size(self):
        args = Args(args=['A','B'],consider_first=True)
        self.assertEqual(len(args),2)
        args = Args(args=['A','B'],consider_first=False)
        self.assertEqual(len(args),1)


