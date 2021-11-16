
from sys import argv
from copy import deepcopy
from json import dumps
from typing import Union


from extras import format_args, get_flags, get_size


class Args:

    def __init__(self,consider_first=False,
                case_sensitive=False,
                convert_numbers=True,
                flag_identifier = '-',
                infinity_indentifier = True 
                ) -> None:

        self.args = format_args(
            args=deepcopy(argv),
            consider_first=consider_first,
            case_sensitive=case_sensitive,
            convert_numbers=convert_numbers
        )

        self.flags = get_flags(
            args=self.args,
            flag_identifier=flag_identifier,
            infinity_identfier=infinity_indentifier
        )
        self.keys = self.flags.keys()
        self.size = len(self.args)


    def __len__(self)->int:
        return self.size

    def __getitem__(self, index:object)->Union[list,str,int]:
        index_type = index.__class__
       
        if index_type == str:
            try:
                 return self.flags[index]
            except KeyError:
                return None 


        if index_type in [tuple,list]:
            group = []
            for key in index:
                if key in self.keys:
                     group.append(*self.flags[key])
              
            return group        
            

        if index_type in [slice,int]:
            try:
                return self.args[index]
            except IndexError:
                return None
      
     
    def __eq__(self, o: object) -> bool:
       
        if o == {} or o == []:
            return True if self.flags == {'default':[]} else False
        
        comparation_type = o.__class__
    
        if comparation_type == list:
            return o == self.args
        
        if comparation_type == dict:
            return o == self.flags
        
        
    def __ne__(self,o:object):
        return True if self.__eq__(o) == False else True
    

    def __gt__(self,o:object):
        return get_size(o) > self.size
    
        
    def __ge__(self,o:object):
        return get_size(o) >= self.size
    
    def __le__(self,o:object):
        return get_size(o)  <=  self.size
    
        
    def __lt__(self,o:object):
        return get_size(o)  <  self.size

 
    def __repr__(self) -> str:
        return dumps(self.flags,indent=4)


x  = Args()


if x != ['aaa','vvv']:
    print('aaa')