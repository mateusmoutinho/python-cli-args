
from sys import argv
from copy import deepcopy
from json import dumps
from typing import Union
from extras import format_args, get_flags,cast_list


class Args:
   
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
        self._keys = list(self._flags.keys())
        self._size = len(self._args)

    
    def args(self,*flags)->list:
        
        flags_list = cast_list(*flags)
        filtered_args = []
        if flags_list == []:
            return self._args

        for flag in flags_list:
            if flag.__class__ != str:
                raise TypeError('only str are valid for flags')
                
            flag_content = cast_list(self[flag])
            filtered_args+=flag_content
        return filtered_args

    
    def flags(self,*flags)->dict:
        '''this funcion returns a dict,containing the flags passed by arguments,
        if nothing were passed,it will return the full dict flags\n
        flags: a list of the flags will want to filter\n
        exemple:\n
        argv: "teste" -a  "testa"  -b  "testeb"\n 
        code: args.flags("a","x")\n
        returns: {"a":["teste"],"x":None}
        '''
        #generated a standardized of flags_list
        flags_list = cast_list(*flags)
        if flags_list == []:
            return self._flags


        filtered_flags = {}
     
        for flag in flags_list:
            if flag.__class__ != str:
                raise TypeError('only str are valid for flags')
            
            try:
                 #try to refs the flag, with the _flags object
                 filtered_flags[flag] =  self._flags[flag]
            except KeyError:
                #case if doesnt find, it refs the key to None
                filtered_flags[flag] = None 

        return filtered_flags
    

    def flags_names(self)->list:
        '''returns the list of flags that were typed by the user ex:\n
        argv: "teste" -a  "testa"  -b  "testeb"\n 
        returns: ["default","a","b"]'''
        #returns the "private" atributes _keys
        return self._keys
    

    def __len__(self)->int:
        return self._size


    def __getitem__(self, index:Union[int,slice,str])->Union[list,str,int,None]:
        index_type = index.__class__
        try:
            if index_type in [slice,int]:
                return self._args[index]
            
            if index_type == str:
                return self._flags[index]

        except: 
                return None

        if index_type not in [slice,int,str]:
            raise TypeError('only int,slices and str are valid')


    def __contains__(self,arg: Union[str,int]):
        return arg in self._args 


    def __eq__(self, o: object) -> bool:
        
        
        if o == {} or o == []:
            return True if self._flags == {'default':[]} else False
        
        comparation_type = o.__class__
         
        if comparation_type == int:
            return o == self._size
         
        if comparation_type == tuple:
            return list(o) == self._args
            
        if comparation_type == list:
            return o == self._args
        
        if comparation_type == dict:
            return o == self._flags
        
        return False 

        
    def __ne__(self,o: object)-> bool:
        return True if self.__eq__(o) == False else True
    

    def __gt__(self,number: int)-> bool:
        return self._size > number
    
        
    def __ge__(self,number: int)-> bool:
        return  self._size  >= number
    

    def __le__(self,number: int)-> bool:
        return   self._size  <= number


    def __lt__(self,number: int)-> bool:
        return self._size < number

  
    def __repr__(self) -> str:
        return dumps(self._flags,indent=4)


args  = Args()

args.flags_names()
args.flags()

