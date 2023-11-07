class TaskOrganizer:
    
    def __init__(self):
        self.tasks = []
    

    def addTask(self, task):
        self.tasks.append(task)
    
    def removeTask(self, index):
        self.tasks.pop(int(index))
    
    def editTask(self, edit, index, setting):
        if(int(setting) == 1):
            self.tasks[int(index)].setTaskName(edit)
        elif(int(setting) == 2):
            self.tasks[int(index)].setTaskDescription(edit)

    def getTasks(self):
        return self.tasks
    
    def saveTasks(self):
        with open("tasks.txt", "w+") as file:
            for count in range(0, len(self.tasks)):
                file.write(f"{count + 1}. {self.tasks[count].getTaskName()}\n{self.tasks[count].getTaskDescription()}\n")       

    def printTask(self):
        for count in range(0, len(self.tasks)):
            print(f"{count + 1}. {self.tasks[count].getTaskName()}\n")
    
    def printTaskWhole(self):
        for count in range(0, len(self.tasks)):
            print(f"{count + 1}. {self.tasks[count].getTaskName()}\n\t{self.tasks[count].getTaskDescription()}\n")