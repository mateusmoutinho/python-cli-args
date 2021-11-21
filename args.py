
from sys import argv
from copy import deepcopy
from json import dumps
from typing import Union
from extras import format_args, get_flags,cast_list
from flags_content import FlagsContent
from list_args import ListArgs


class Args(ListArgs):
   
    def __init__(self,consider_first=False,
                flags_case_sensitive=False,
                args_case_sensitive=True,
                convert_numbers=True,
                flag_identifier = '-',
                infinity_indentifier = True,
                args=deepcopy(argv)                
                ) -> None:
        
        self._args = format_args(
            args=args,
            consider_first=consider_first,
            case_sensitive=args_case_sensitive,
            convert_numbers=convert_numbers
        )

        self._flags = get_flags(
            args=self._args,
            flag_identifier=flag_identifier,
            case_sensitive=flags_case_sensitive,
            infinity_identfier=infinity_indentifier
        )
        self.flags_names = list(self._flags.keys())



    def flags_content(self,*flags)->FlagsContent:
        flags_list = cast_list(*flags)
        filtered_args = []
        at_least_one_flag_exist = False
        for flag in flags_list:
            if flag.__class__ != str:
                raise TypeError('only str are valid for flags')
            try:
                filtered_args+=self._flags[flag]
                at_least_one_flag_exist = True 
            except KeyError:pass 

        if at_least_one_flag_exist:
            return FlagsContent(content=filtered_args)
        else:
            return FlagsContent(content=None)


    def __eq__(self, o: object) -> bool:
        
        if o == {} or o == []:
            return True if self._args == [] else False
        
        comparation_type = o.__class__
         
        if comparation_type == int:
            return o == len(self)
         
        if comparation_type == tuple:
            return list(o) == self._args
            
        if comparation_type == list:
            return o == self._args
        
        if comparation_type == dict:
            return o == self._flags
        
        return False 

       
    def __ne__(self,o: object)-> bool:
        return True if self.__eq__(o) == False else True
    
  
    def __repr__(self) -> str:
        return dumps(self._flags,indent=4)


