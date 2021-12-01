from io import TextIOWrapper
from typing import IO, Text
from cli_args_system import Args
from cli_args_system import flags_content
from cli_args_system.flags_content import FlagsContent
from sys import exit

def exit_mensage(mensage:str):
    print(mensage)
    exit(1)

def get_file_text(args:Args) ->str:
    try:
        with open(args[0],'r') as f:
            return  f.read()
    except (FileNotFoundError,IndexError):
        exit_mensage(mensage='no file')


def get_out_wraper(args:Args,destroy_if_dont_find=True)->TextIOWrapper or None:
    out = args.flags_content('out','o','out-file','outfile','out_file')
    if out.filled:
        return open(out[0],'w')
    if destroy_if_dont_find:
        exit_mensage(mensage='not out file')


def join_files(join:FlagsContent,args:Args):
    if len(join) < 2:
        print('must bee at least 2 files')
        exit(1)
    full_text = ''  
    for file_path in join:
        try:
            with open(file_path,'r') as file:
                full_text+=file.read()
        except FileNotFoundError:
            print(f'file {file_path} not exist')
            exit(1)
    get_out_wraper(args).write(full_text)
    

def replace_elements(replace:flags_content,args:Args):
  
    if len(replace) != 2:
        exit_mensage(mensage='must bee two elements to replace')    
        
    replaced_text = get_file_text(args).replace(replace[0],replace[1])
    
    out = get_out_wraper(args,destroy_if_dont_find=False)
    if out is None:
        open(args[0],'w').write(replaced_text)
    else:
        out.write(replaced_text)
      

def remove_text(remove:FlagsContent,args:Args):
    
    if not remove.filled:
        exit_mensage('not text to remove')
    
    text_file = get_file_text(args)
    
    for text in remove:
       text_file = text_file.replace(text,'')

    out = get_out_wraper(args,destroy_if_dont_find=False)
    if out:
        out.write(text_file)
    else:
       open(args[0],'w').write(text_file) 

    
if __name__ == '__main__':
    args = Args(convert_numbers=False)
        

    join = args.flags_content('join','j')
    if join.exist:
        join_files(join,args)


    replace = args.flags_content('replace','substitute')
    if replace.exist:
        replace_elements(replace,args)

    remove = args.flags_content('r','remove','pop',)
    if remove.exist:
        remove_text(remove,args)




