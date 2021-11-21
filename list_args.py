

from typing import Union

#abstract class 
class ListArgs:
    def __init__(self) -> None:
        self.args = []


    def __eq__(self, o: object) -> bool:

        if isinstance(o,int):
            return len(self) == o

        if isinstance(o,list):
            return o == self.args
        return False 

    def __ne__(self, o: object) -> bool:
        return False if self == o else True  


    def __getitem__(self,index:Union[slice,int]):
        return self.args[index]

    def __contains__(self, o:object):
        return o in self.args


    def __len__(self):
        return len(self.args)
    
    def __gt__(self,o:object):
        return len(self) > o

    def __ge__(self,o:object):
        return len(self) >= o
    
    def __lt__(self,o:object):
        return len(self) < o

    def __le__(self,o:object):
        return len(self) <= o