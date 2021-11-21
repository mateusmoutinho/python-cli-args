from typing import Union
from cli_args.list_args import ListArgs


# The Flags Content Extends ListArgs, witch is a "only-read" list
class FlagsContent(ListArgs):
    
    def __init__(self, content: Union[None, list]) -> None:
        """content:the group of args that were found \n"""

        # set the exist and filled to false
        super().__init__()
        self.exist = False
        self.filled = False
        # if content is not None, means the flag exist
        if content is not None:
            self.exist = True
            # if content is not [], means its filled
            if content:
                self.filled = True
                # set the args to content, for to be
            # used with the super(ListArgs)
            self.args = content
