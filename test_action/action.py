class Action:
    def __init__(self, do_func, data):
        self.do_func = do_func   # Function to do the action
        self.data = data         # Data required for the action
    
    def execute(self):
        return self.do_func(self.data)
    