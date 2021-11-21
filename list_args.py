

from typing import Union

#abstract class 
#the ListArgs is a "only read" list, that implements the 
#"magic" methods of lists 
class ListArgs:
    
    def __init__(self) -> None:
        #creates the empty args 
        self.args = []


    def __eq__(self, o: object) -> bool:
        '''this function is called when == is called
        o: the object comparation, ex args == 20, 20 its "o" 
        '''
        #if comparation is a int, it will be compared with size 
        if isinstance(o,int):
            return len(self) == o
        #if its a list it will be compared with the args propety
        if isinstance(o,list):
            return o == self.args
        return False 

    def __ne__(self, o: object) -> bool:
        '''this function is called when != is called''' 
        #its "flip" the __eq__ methods
        return False if self == o else True  


    def __getitem__(self,index:Union[slice,int]):
        '''this function its called when != is used '''
        #its just return the index element
        return self.args[index]

    def __contains__(self, o:object):
        '''this function is called when "in" is useed'''
        #its just return the in comparation with args 
        return o in self.args


    def __len__(self):
        '''this function is called when len(x) is called'''
        return len(self.args)
    
    #all above methods is for >, >=, <. <= methods 
    #and all make the comparation with the self len 
    def __gt__(self,o:object):
        return len(self) > o

    def __ge__(self,o:object):
        return len(self) >= o
    
    def __lt__(self,o:object):
        return len(self) < o

    def __le__(self,o:object):
        return len(self) <= o