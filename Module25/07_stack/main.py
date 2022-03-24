class Stack:

    def __init__(self):
        self.__task_list = []

    def __str__(self):
        return '; '.join(self.__task_list)

    def push(self, elem):
        self.__task_list.append(elem)

    def pop(self, string):
        if len(self.__task_list) == 0:
            return None
        else:
            return self.__task_list.pop(string)


class TaskManager:

    def __init__(self):
        self.task = dict()

    def __str__(self):
        console = []
        if self.task:
            for i_position in sorted(self.task.keys()):
                console.append('{} {}\n'.format(
                    str(i_position), self.task[i_position]
                ))
        return ''.join(console)

    def new_task(self, task, position):
        if position not in self.task:
            self.task[position] = Stack()
        self.task[position].push(task)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)