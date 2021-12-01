from cli_args_system import Args
from cli_args_system.flags_content import FlagsContent
from sys import exit


HELP = """this is a basic calculator to demonstrate
args_system usage with numbers

-------------------flags----------------------------
-add: add the first number with the next number 
-sub: subtract the first number with the next number 
-multi: multiply the first number with the next number
-div: divide first number with the next number  

-------------------usage----------------------------
$ python3 calc.py -add 10 20 -> 30 
$ python3 calc.py -sub 10 3 -> 7
$ python3 calc.py -mult 10 20 -> 200
$ python3 calc.py -div 10 2 -> 5.0"""

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


if __name__ == '__main__':
   #creates the args object
   args = Args()
   
   #for help flag
   help = args.flags_content('h','help')
   if help.exist:
      print(HELP);exit(0)


          
   #its one because "default" flag goona be unconsidered
   if args.total_flags() != 1:
      print(f'only one calc is permitted not {args.total_flags()}')
      exit(1) 

   #--------------------threating flags---------------------------

   #get the flagsContent of add flags and its sinoniumous
   add = args.flags_content('add','a')
   #verify if add flag  or its synonimous is present 
   if add.exist:
      print(execute_calc(add,'+'))

   #make the same for the others 
   sub = args.flags_content('sub','pop','remove','s')
   if sub.exist:
      print(execute_calc(sub,'-'))


   multi = args.flags_content('multi','mult','m','*')
   if multi.exist:
      print(execute_calc(multi,'*'))


   div = args.flags_content('div','d','/')
   if div.exist:
      print(execute_calc(div,'/'))


   if args.total_unused_flags() > 0:
      print(f'invalid flag: {args.unused_flags_names()[0]}')