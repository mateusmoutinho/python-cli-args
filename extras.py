


from typing import Any,Union




def format_flag(flag:str,identifier_char:str,infinity_identfier:bool)->str:
    for index in range(0,len(flag)):
        char = flag[index]
        if char == identifier_char and not infinity_identfier:
           return flag[index+1::]
        if char != identifier_char:
            return flag[index::]
    return flag

def is_a_flag(possible_flag:str,identifier_char:str) ->bool:

    if possible_flag.__class__ == int:
         return False 

    if possible_flag[0] == identifier_char and len(possible_flag) > 1:
        return True 
    return False 


def get_flags(args:list,flag_identifier:str,infinity_identfier:bool)->dict:
    
    flags:dict = {'default':[]}
    current_flag = 'default'
    for arg in args:
        if is_a_flag(possible_flag=str(arg),identifier_char=flag_identifier):

            current_flag = format_flag(
                flag=arg,
                identifier_char=flag_identifier,
                infinity_identfier=infinity_identfier
                )
            flags[current_flag] = []
            continue 
        
        flags[current_flag].append(arg)
    return flags 



def convert_number(possible_number:str)->Union[str,float,int]:
    try:
        return int(possible_number)
    except ValueError:
        try: 
            return float(possible_number)
        except ValueError:
            return possible_number 



def format_args(args:list,consider_first:bool,case_sensitive=bool,convert_numbers=bool):
     
     if not consider_first:
        args = args[1::]

     if not case_sensitive:
        args = list(map(lambda arg: arg.lower(),args))
    
     if convert_numbers:
        args = list(map(convert_number,args))
     return args 


def cast_list(*elements)->list:

    if  len(elements) == 1:
        if elements[0] is None:
            return []
            
        if elements[0].__class__ == list:
            return elements[0]

        return [elements[0]]
    else:
        return list(elements)
    


              
     
        
    