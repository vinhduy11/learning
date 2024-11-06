class ActionManager:
    def __init__(self):
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    def run(self):
        result = False
        for action in self.actions:
            result = action.execute()
            if not result:
                break