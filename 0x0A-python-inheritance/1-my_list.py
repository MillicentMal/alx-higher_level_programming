class MyList(list):
    """
    inherits from list object
    """
    def __init__(self):
        self.obj = list()
    
    def print_sorted(self):
        return self.sort()
    
    def __repr__(self) -> str:
        return super().__repr__()
