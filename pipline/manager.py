class ActionManager:
    def __init__(self)-> None:
        self.actions = []
        self.condition = False
    
    def add_condition(self, condition) -> None:
        self.condition = condition

    def add_action(self, action) -> None:
        self.actions.append(action)

    def run(self) -> None:
        result = False
        for action in self.actions:
            result = action.execute()
            if result == self.condition:
                break