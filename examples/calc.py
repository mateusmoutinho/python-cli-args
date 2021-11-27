from cli_args_system import Args
from cli_args_system.flags_content import FlagsContent
from sys import exit
#this is a basic calculator to demonstrate args_system usage
#with numbers 


def execute_calc(flags_content:FlagsContent,calc:str)->int:
   
   #for seeing if will be possible to execute the calculation
   if len(flags_content) < 2:
      print('two numbers is required')
      exit(1)
   
   #creates a dict with the results, its not nessesary to cast elements
   #with int objects because the lib does it by itself
   operation = {
      '+':flags_content[0] + flags_content[1],
      '-':flags_content[0] - flags_content[1],
      '*':flags_content[0] * flags_content[1],
      '/':flags_content[0] / flags_content[1]
   }
   return operation[calc]


#creates the args object
args = Args()


#its one because "default" flag is unconsidered in this method
if args.total_flags() != 1:
   print(f'only one calc is permitted not {args.total_flags()}')
   exit(1) 


result:int = None 

#get the flagsContent of add flags and its sinoniumous
add = args.flags_content('add','a')
#verify if add flag  or its synonimous is present 
if add.exist:
   result = execute_calc(add,'+')

#make the same for the others 
sub = args.flags_content('sub','pop','remove','s')
if sub.exist:
   result = execute_calc(sub,'-')


multi = args.flags_content('multi','m','*')
if multi.exist:
   result = execute_calc(multi,'*')


div = args.flags_content('div','d','/')
if div.exist:
   result = execute_calc(div,'/')


if result is not None:
   print(result)
else:
   print(f'invalid flag: {args.unused_flags_names()[0]}')