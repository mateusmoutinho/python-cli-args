


from typing import Any,Union
from unittest import case




def format_flag(flag:str,case_sensitive:bool,identifier_char:str,infinity_identfier:bool)->str:
    if not case_sensitive:
        flag = flag.lower()
    for index in range(0,len(flag)):
        char = flag[index]
        if char == identifier_char and not infinity_identfier:
           return flag[index+1::]
        if char != identifier_char:
            return flag[index::]
    
    return flag

def is_a_flag(possible_flag:Union[str,int,float],case_sensitive:bool,identifier_char:str) ->bool:

    if possible_flag.__class__ in [int,float]:
         return False 
    
    if not case_sensitive:
        possible_flag = possible_flag.lower()

    if possible_flag[0] == identifier_char and len(possible_flag) > 1:
        return True 
    return False 


def get_flags(
    args:list,
    flag_identifier:str,
    case_sensitive:bool,
    infinity_identfier:bool)->dict:
    
    flags:dict = {'default':[]}
    current_flag = 'default'
    for arg in args:
   
        if is_a_flag(possible_flag=arg,case_sensitive=case_sensitive,identifier_char=flag_identifier):

            current_flag = format_flag(
                flag=arg,
                case_sensitive = case_sensitive,
                identifier_char=flag_identifier,
                infinity_identfier=infinity_identfier
                )
            if current_flag not in flags.keys():
                flags[current_flag] = []
            continue 
        
        flags[current_flag].append(arg)
    return flags 



def convert_number(possible_number:str)->Union[str,float,int]:
    '''convert the possible_number  in a number if its possible,
    case if were not possible to convert, will return the possible_number 
    (the same arg of function)
    '''

    try:
        #try to cast in an int 
        return int(possible_number)
    except ValueError:
        try: 
            #case cat a Value error, try to cast in a float
            return float(possible_number)
        except ValueError:
            #case if were not a int either a float, will cat here 
            #and return the same arg
            return possible_number 



def format_args(args:list,consider_first:bool,case_sensitive=bool,convert_numbers=bool):
    '''this function format args, based on args passed
    args: the list of "argv"
    consider_first: if the first element of args is to be considered
    case_sensitive: case if not, all will be lower
    convert_numbers: convert numbers in float or int if possible
    '''
    if not consider_first:
        #split the args
        args = args[1::]

    if not case_sensitive:
        #map the args to all be lower
        args = list(map(lambda arg: arg.lower(),args))
    
    if convert_numbers:
        #make a maping calling the convert number funcion
        args = list(map(convert_number,args))
    return args 


def cast_list(*elements)->list:
    '''elements: [tuple,list,str]
    this function cast everthing in a list, but every object, has 
    his especific way, ex:
    cast_list("a","b") returns: ["a","b"]
    cast_list([1,2]) returns: [1,2]
    '''
    #means just one element were passed as arg
    if  len(elements) == 1:
        #means nothing were passed as arg
        if elements[0] is None:
            return []
        
        if elements[0].__class__ in [list,tuple]:
            #if a tuple or list were passed, it will return a cast of it
            return list(elements[0])
            
        #else will make a list with elements 0 
        return [elements[0]]
    else:

        #if its a larger element, just cast with list
        return list(elements)
    


              
     
        
    