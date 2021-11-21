

from typing import Union


class FlagsContent(list):

    def __init__(self,content:Union[None,list]) -> None:
        
        self.exist = False 
        self.filled = False
        
        if content is not None:
            self.exist = True 
            if content != []:
                self.filled = True  
            self+=content
    
    

