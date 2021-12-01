from unittest.loader import findTestCases
from cli_args_system import Args, FlagsContent
from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup

def exit_with_mensage(mensage:str):
    print(mensage)
    exit(1)


def get_html(args:Args)->str:
    """get html text, witch is bascly  the first argument of args
    it can be a file or a url 
    """
    try:
        html = args[0]
    except IndexError:
        #if doesnt find, kill the aplication
        exit_with_mensage(mensage='not html target')

    try: 
        #try to find the file
        with open(html,'r') as f:
            return  f.read()
        
    except FileNotFoundError:
        #if doesnt file, try to find the url 
        
        try:
            return urlopen(html).read().decode("utf8")
        except URLError:
            #if doenst find nothind, its impossible to proceed 
            #with the aplication
            exit_with_mensage(mensage='not a valid html')


def find_in_html(html:str,find:FlagsContent, args:Args)->str:

    find_dict = {}
    if not find.filled():
        exit_with_mensage(mensage='no tag')

    id = args.flags_content('id')
    if id.exist_and_empty():
        exit_with_mensage(mensage='empty id')
    if id.exist():
        find_dict['id'] = id[0]
    
    class_name = args.flags_content('class','classname')
    if class_name.exist_and_empty():
       exit_with_mensage(mensage='empty class')
    if class_name.exist():
        find_dict['class'] = class_name[0]
    
    
    return  BeautifulSoup(html,'lxml').find_all(find[0],find_dict)


args = Args()

html = get_html(args)

find = args.flags_content('filter','f')
if find.exist():
    text = find_in_html(html,find,args)
    print(text)

only_content  = args.flags_content('onlycontent','only')
