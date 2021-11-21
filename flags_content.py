

from typing import Union

from list_args import ListArgs


class FlagsContent(ListArgs):

    def __init__(self,content:Union[None,list]) -> None:
        
        self.exist = False 
        self.filled = False
        
        if content is not None:
            self.exist = True 
            if content != []:
                self.filled = True  
            self.args = content
    
    


