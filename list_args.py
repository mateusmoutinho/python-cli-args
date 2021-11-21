

from typing import Union

#abstract class 
class ListArgs:
    
    def __getitem__(self,index:Union[slice,int]):
        return self._args[index]

    def __contains__(self, o:object):
        return o in self._args

    def __len__(self):
        return len(self._args)
    
    def __gt__(self,o:object):
        return len(self) > o

    def __ge__(self,o:object):
        return len(self) >= o
    
    def __lt__(self,o:object):
        return len(self) < o

    def __le__(self,o:object):
        return len(self) <= o