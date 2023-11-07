from TaskOrganizer import TaskOrganizer
from Tasks import Tasks

taskManager = TaskOrganizer()

def addTask():
    global taskManager
    task = Tasks(input("\nEnter task title: \n"), input("\nEnter task description: \n"))
    taskManager.addTask(task)
    print(f"\nTask successfully added!")

def removeTask():
    global taskManager
    taskManager.printTask()
    try:
        index = int(input("\nSelect based on number the task you wish to remove: ")) - 1
        taskManager.removeTask(index)
        print(f"\nTask successfully removed!")
    except:
        print(f"\nERROR! Please enter a number instead or the correct number based on the task")

def editTask():
    global taskManager
    taskManager.printTaskWhole()
    try:
        index = int(input("\nSelect based on the number the task you wish to edit: ")) - 1
        choice = input("\nWould you like to edit the \"Name\" or the \"Description\" of the task?\n")
        if choice.lower() == "name":
            taskManager.editTask(input("\nPlease enter a new task name:\n"), index, 1)
            print(f"\nTask name successfully edited!")
        elif choice.lower() == "description":
            taskManager.editTask(input("\nPlease enter a new task description:\n"), index, 2)
            print(f"\nDescription successfully edited!")
        else:
            print(f"\nPlease enter one of the two options\n")
    except:
        print(f"\nERROR! Please enter the correct value for the question or the correct number based on the task")


print("---------------------------------------------------")
print(f"\nWelcome to the task manager creator.\nPlease make sure to add a task before doing other options.\n")
print("---------------------------------------------------\n")

while True:

    try:
        choice = int(input("""Please select based on number, one of the following options.
---------------------------------------------------
\t1. Add a task
\t2. Remove a task
\t3. Edit a task
\t4. Display all tasks
\t5. Save all tasks into file(Note: this will end the program)
\t6. End program
---------------------------------------------------
Answer: """))
        print("\n---------------------------------------------------")
        if choice == 1:
            addTask()
        elif choice == 2 and len(taskManager.getTasks()) != 0:
            removeTask()
        elif choice == 3 and len(taskManager.getTasks()) != 0:
            editTask()
        elif choice == 4 and len(taskManager.getTasks()) != 0:
            taskManager.printTaskWhole()
        elif choice == 5 and len(taskManager.getTasks()) != 0:
            taskManager.saveTasks()
            print(f"\n All tasks successfully saved under tasks.txt!")
        elif choice == 6:
            print(f"\nThanks for using this program")
            print("\n---------------------------------------------------")
            break
        else:
            print("\nNote: choice 2 - 5 will not work unless you have at least one task otherwise please select a valid option")
        print("\n---------------------------------------------------")
        
    except:
        print("\nPlease enter a number value\n")

