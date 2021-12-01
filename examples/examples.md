
 
In this folder you will see 3 programs containing examples of how the library works:

#### calc.py
>basic calculator based on flags system

##### usage:

``` bash
$python3 calc.py -add 10 20
result: 30 

$python3 calc.py -sub 10 3 
result: 7

$python3 calc.py -mult 10 20 
result: 200

$python3 calc.py -div 10 2 
result: 5.0
```
##### dealing with errors: 
``` bash
$python3 calc.py -x 10 2 
result: invalid flag x 

$python3 calc.py -add -subb 10 2 
result:only one calc is permitted not 2

$python3 calc.py -add 10  
result: two numbers is required
```