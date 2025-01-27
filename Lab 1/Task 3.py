import random

class BackupTask:
    def __init__(self, task_id):
        self.task_id = task_id
        self.status = random.choice(["completed", "failed"])  
    
    def __str__(self):
        return f"Task{self.task_id} has status {self.status}"

class BackupManagementAgent:
    def __init__(self, tasks):
        self.tasks = tasks  
    
    def retry(self):
        print("\nScanning tasks:")
        for task in self.tasks:
            if task.status == "failed":
                print(f"Retrying {task}")
                task.status = "completed"  
                print(f"Task{task.task_id} retried and completed")
    
    def display_task_statuses(self):
        print("\nUpdated Backup Task Statuses:")
        for task in self.tasks:
            print(task)

def create_backup_tasks(num_tasks):
    tasks = []
    for i in range(1, num_tasks + 1):
        tasks.append(BackupTask(i))
    return tasks

def run_code():
    tasks = create_backup_tasks(4)
    
    print("Initial Backup Task Statuses:")
    for task in tasks:
        print(task)
    
    agent = BackupManagementAgent(tasks)
    
    agent.retry()
    
    # Display the final task statuses after retrying
    agent.display_task_statuses()

#Run the simulation
run_code()
