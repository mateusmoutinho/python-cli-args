
from sys import argv
from copy import deepcopy
from json import dumps
from typing import Union
from extras import format_args, get_flags,cast_list


class Args:

    def __init__(self,consider_first=False,
                case_sensitive=False,
                convert_numbers=True,
                flag_identifier = '-',
                infinity_indentifier = True,
                args=deepcopy(argv)                
                ) -> None:

        self._args = format_args(
            args=args,
            consider_first=consider_first,
            case_sensitive=case_sensitive,
            convert_numbers=convert_numbers
        )

        self._flags = get_flags(
            args=self._args,
            flag_identifier=flag_identifier,
            infinity_identfier=infinity_indentifier
        )
        self.keys = list(self._flags.keys())
        self.size = len(self._args)

    
    def args(self,*flags)->list:
        flags_list = cast_list(*flags)
        filtered_args = []
        if flags_list == []:
            return self._args

        for flag in flags_list:
            flag_content = cast_list(self[flag])
            filtered_args+=flag_content
        return filtered_args


    def flags(self,*flags)->dict:
        flags_list = cast_list(*flags)
        if flags_list == []:
            return self.flags
        filtered_flags = {}
        for flag in flags_list:
            formated_flag = str(flag)
            filtered_flags[formated_flag] =  self[formated_flag]
        return filtered_flags
                
    
    def __len__(self)->int:
        return self.size


    def __getitem__(self, index:Union[int,slice,str])->Union[list,str,int,None]:
        try:
            index_type = index.__class__
            if index_type in [slice,int]:
                return self._args[index]
            
            if index_type == str:
                return self._flags[index]
           
        except KeyError or IndexError:pass 
        return None 
       

    def __contains__(self,arg: Union[str,int]):
        if arg in self._args or arg in self.keys:
            return True 
        return False 
        

    def __eq__(self, o: object) -> bool:
        if o == {} or o == []:
            return True if self._flags == {'default':[]} else False
        
        comparation_type = o.__class__
    
        if comparation_type == list:
            return o == self._args
        
        if comparation_type == dict:
            return o == self._flags
        return False 

        
    def __ne__(self,o: object)-> bool:
        return True if self.__eq__(o) == False else True
    

    def __gt__(self,number: int)-> bool:
        return self.size > number
    
        
    def __ge__(self,number: int)-> bool:
        return  self.size  >= number
    

    def __le__(self,number: int)-> bool:
        return   self.size  <= number


    def __lt__(self,number: int)-> bool:
        return self.size < number

 
    def __repr__(self) -> str:
        return dumps(self._flags,indent=4)


