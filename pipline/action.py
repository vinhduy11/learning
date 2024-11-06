class Action:
    def __init__(self, do_func: callable, data: any) -> None:
        self.do_func = do_func   # Function to do the action
        self.data = data         # Data required for the action
    
    def execute(self)->any:
        return self.do_func(self.data)
    