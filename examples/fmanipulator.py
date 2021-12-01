from io import TextIOWrapper
from typing import IO, Text
from cli_args_system import Args

from cli_args_system import Args, FlagsContent
from sys import exit

HELP = """this is a basic file manipulator to demonstrate
args_system usage with file flags

-------------------flags----------------------------
-join: join the files passed and save in the --out flag

-replace: replace the text on file and save in the --out flag 
if there is no out flag, it will save in the same file 

-remove: remove the given text in the file 

-------------------usage----------------------------
$ python3 fmanipulator.py -join a.txt b.txt -out c.txt
will join the content on a.txt and b.txt, and save in c.txt 


$ python3 fmanipulator.py a.txt  -replace a b 
will replace the char a for char b in the a.txt file 

$ python3 fmanipulator.py a.txt  -replace a b -out b.txt 
will replace the char a for char b and save in b.txt 

$ python3 fmanipulator.py a.txt -r test 
will remove the text: test in the file a.txt 

$ python3 fmanipulator.py a.txt -r test -out b.txt
will remove the text: test in the file a.txt  and save in b.txt"""


def exit_with_mensage(mensage:str):
    """kills the aplcation after printing the mensage \n
    mensage: the mensage to print"""
    print(mensage)
    exit(1)


def get_file_text(args:Args) ->str:
    """returns the file text of args[0] (argv[0]) \n
    args:The  args Object"""
    try:
        with open(args[0],'r') as f:
            return  f.read()
    except (FileNotFoundError,IndexError):
        #if doenst find the file text,kilss the aplcation
        exit_with_mensage(mensage='no file')


def get_out_wraper(args:Args,destroy_if_dont_find=True)->TextIOWrapper or None:
    """returns the out wraper of out[0] flag\n
    args: The  args Object \n
    destroy_if_dont_find: if True it will destroy the aplication
    if doesnt find out[0] flag"""

    out = args.flags_content('out','o','out-file','outfile','out_file')
    if out.filled():
        return open(out[0],'w')
    else:
        #check if is to destroy
        if destroy_if_dont_find:
            exit_with_mensage(mensage='not out file')


def write_text_in_out_file_or_same_file(text:str,args:Args):
    """write text in out flag if exist,
    otherwhise write on same file args(0)\n
    text: the text to write \n
    args: The  args Object \n
    """
    out = get_out_wraper(args,destroy_if_dont_find=False)
        
    #if out is not passed it replace in the same file
    if out is None:
        open(args[0],'w').write(text)
    else:
        #otherwise write in the out file
        out.write(text)
      

def join_files(join:FlagsContent,args:Args):
    """join the files of join flag, in the out flag content
    join: the join FlagsContent \n
    args: The args Object"""
    if len(join) < 2:
        print('must bee at least 2 files')
        exit(1)
    full_text = ''  

    #make a iteration on join flag
    for file_path in join:
        try:
            #try to open and add in the full text, the content of 
            #file path
            with open(file_path,'r') as file:
                full_text+=file.read()
        except FileNotFoundError:
            print(f'file {file_path} not exist')
            exit(1)
    #write the changes in the out file
    get_out_wraper(args).write(full_text)
    

def replace_elements(replace:FlagsContent,args:Args):
    """replace in file (args[0) with  replace[0] to replace[1]
    replace: the replace FlagsContent
    args: The  args Object
    """

    if len(replace) != 2:
        exit_with_mensage(mensage='must bee two elements to replace')    
        
    #get the file of args[0]
    file = get_file_text(args)
    #make the replace
    replaced_text = file.replace(replace[0],replace[1])
    write_text_in_out_file_or_same_file(text=replaced_text,args=args)


def remove_text(remove:FlagsContent,args:Args):
    """this function remove the text in passed in the remove flags \n
    remove: the remove FlagsContent \n
    args: The args Object """
    

    if not remove.filled():
        exit_with_mensage('not text to remove')
    
    text_file = get_file_text(args)
    #goes in a iteration in remove flags
    for text in remove:
       text_file = text_file.replace(text,'')

    write_text_in_out_file_or_same_file(text=text_file,args=args)

if __name__ == '__main__':
    #construct the args
    args = Args(convert_numbers=False)
    
       
   #for help flag
    help = args.flags_content('h','help')
    if help.exist():
        print(HELP);exit(0)
    

    join = args.flags_content('join','j')
    #if join flag exist, call the join_files
    if join.exist():
        join_files(join,args)
    
    replace = args.flags_content('replace','substitute')
    #if replace flag exist call the replace_elements function
    if replace.exist():
        replace_elements(replace,args)

    remove = args.flags_content('r','remove','pop')
    #if remove flag exist call the remove_text
    if remove.exist():
        remove_text(remove,args)




