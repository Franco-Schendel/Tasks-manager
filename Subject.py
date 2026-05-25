class Subject:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, id):
        for task in self.tasks:
            if task.id == id:
                self.tasks.remove(task)
    
    def get_tasks(self):
        return self.tasks

    def total_tasks(self):
        return len(self.tasks)
    
    def tasks_done(self):
        done = 0
        for i in self.tasks:
            if i.is_done() == True:
                done += 1
        return done

