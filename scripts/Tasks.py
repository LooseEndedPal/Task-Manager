class Tasks:
    def __init__(self, taskName, taskDescription):
        self.taskName = taskName
        self.taskDescription = taskDescription
    
    #Getters
    def getTaskName(self):
        return self.taskName
    
    def getTaskDescription(self):
        return self.taskDescription
    
    #Setters
    def setTaskName(self, taskName):
        self.taskName = taskName
    
    def setTaskDescription(self, taskDescription):
        self.taskDescription = taskDescription
    