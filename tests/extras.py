from unittest import TestCase
from extras import cast_list, format_args, format_flag,is_a_flag,get_flags

class Format_Flag(TestCase):
     
     def test_infinity_identifier(self):
         formated_flag = format_flag(flag='--a',
         case_sensitive=False,
         identifier_char='-',
         infinity_identfier=True
         )
         self.assertEqual(formated_flag,'a')
         
     def test_not_inifynity_identifier(self):
         formated_flag = format_flag(flag='---a',
         case_sensitive=False,
         identifier_char='-',
         infinity_identfier=False
         )
         self.assertEqual(formated_flag,'--a')

     def test_case_sensitive(self):
         formated_flag = format_flag(flag='--A',
         case_sensitive=True,
         identifier_char='-',
         infinity_identfier=True
         )
         self.assertEqual(formated_flag,'A')


class Is_a_Flag(TestCase):
    
    def test_is_a_flag(self):
        flag = is_a_flag('--a',case_sensitive=False,identifier_char='-')
        self.assertTrue(flag)

    def test_case_sensitive(self):
        flag = is_a_flag('BA',case_sensitive=True,identifier_char='b')
        self.assertFalse(flag)


    def test_case_sensitive(self):
        flag = is_a_flag('BA',case_sensitive=True,identifier_char='B')
        self.assertTrue(flag)



    def test_is_not_a_flag(self):
        flag = is_a_flag('--a',case_sensitive=False,identifier_char='#')
        self.assertFalse(flag)


class Get_Flags(TestCase):
    
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        
    def test_with_flags(self):
        args = ['a','b','c','-a','a1','a2','a3','--b','b1','b2','b3']
        flags = get_flags(args=args,case_sensitive=False, flag_identifier='-',infinity_identfier=True)
        espected = {
            'default':['a','b','c'],
            'a':['a1','a2','a3'],
            'b':['b1','b2','b3']
        }
        self.assertDictEqual(flags,espected)

    def test_without_flags(self):
        args = ['a','b','c','a1','a2','a3','b1','b2','b3']
        flags = get_flags(args=args,case_sensitive=False,flag_identifier='-',infinity_identfier=True)
        espected = {
            'default':['a','b','c','a1','a2','a3','b1','b2','b3']
        }
        self.assertDictEqual(flags,espected)

    def test_with_diferent_identifier(self):
        args = ['a','b','c','#a','a1','a2','a3','##b','b1','b2','b3']
        flags = get_flags(args=args,case_sensitive=False,flag_identifier='#',infinity_identfier=True)
        espected = {
            'default':['a','b','c'],
            'a':['a1','a2','a3'],
            'b':['b1','b2','b3']
        }
        self.assertDictEqual(flags,espected)


    def test_with_flags_case_sensitive(self):
        args = ['a','b','c','-A','a1','a2','a3','--B','b1','b2','b3']
        flags = get_flags(args=args,case_sensitive=True, flag_identifier='-',infinity_identfier=True)
        espected = {
            'default':['a','b','c'],
            'A':['a1','a2','a3'],
            'B':['b1','b2','b3']
        }
        self.assertDictEqual(flags,espected)




class Format_args(TestCase):

    def test_al_true(self):
        entry = ['A','B','C','D','1','2','3','4']
        args = format_args(
            args=entry,
            consider_first=True,
            case_sensitive=True,
            convert_numbers=True
            )
        expected = ['A','B','C','D',1,2,3,4]
        self.assertListEqual(args,expected)

    def test_al_false(self):
        entry = ['A','B','C','D','1','2','3','4']
        args = format_args(
            args=entry,
            consider_first=False,
            case_sensitive=False,
            convert_numbers=False
            )
        expected = ['b','c','d','1','2','3','4']
        self.assertListEqual(args,expected)


class Cast_List(TestCase):

    def test_empty(self):
        self.assertListEqual(cast_list(),[])
        self.assertListEqual(cast_list(None),[])
        self.assertListEqual(cast_list([]),[])

    def test_tuple(self):
        value = cast_list('1',2,3)
        self.assertListEqual(value,['1',2,3])

    def test_list(self):
        value = cast_list(['1',2,3])
        self.assertListEqual(value,['1',2,3])


    
    def test_string(self):
        value = cast_list('a')
        self.assertListEqual(value,['a'])
                                                  
