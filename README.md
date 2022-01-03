
#### Install from scratch

# 
~~~ shel 
$ sudo python3 setup.py install
~~~
###### windows
# 
~~~ shel 
$ python setup.py install
~~~
#
#


#### What is cli_args_system ?
in an general way its a library to manipulate argv args its content and its flags 
#
#


#### Basic Usage 
###### the most basic aplication:
#
~~~~ python
from cli_args_system import Args

args = Args()
print(args)
~~~~
###### running:
~~~~ shel 
$ python3  test.py  -a "value of a" -b "value of b"
~~~~
###### results:
#
~~~ json
{
    "default": [],
    "a": [
        "value of a "
    ],
    "b": [
        "value of b"
    ]
}
~~~
#
#

##### Args:
###### retriving the args: 
#
~~~~python
from cli_args_system import Args

args = Args()

list_of_args = args.args()
print(list_of_args)
~~~~


###### making iterations:
#
~~~~python
from cli_args_system import Args

args = Args()

for a in args:
    print(a)
~~~~
##### Flags:

###### retriving all flags dict:
#
~~~ python
from cli_args_system import Args

args = Args()

flags = args.flags()
print(flags)
~~~


##### install from scratch
* Windows: $python setup.py install 
* Linux: $sudo python3 setup.py install 



##### install from pip

* Windows: $pip install cli_args_system
* Linux: $pip3 install cli_args_system

#### Basic Usage


##### The most Basic Aplication
~~~python
from cli_args_system import Args,FlagsContent


args = Args()

print(args)
~~~
