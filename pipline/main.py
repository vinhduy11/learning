from action import Action
from action_1 import check_1
from action_2 import check_2
from action_3 import check_3
from manager import ActionManager

task_manager = ActionManager()
if __name__ == '__main__':
    task_manager.add_action(Action(check_1, True))
    task_manager.add_action(Action(check_2, False))
    task_manager.add_action(Action(check_3, False))
    task_manager.add_condition(True)
    task_manager.run()