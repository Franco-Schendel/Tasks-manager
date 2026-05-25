class Task:
    def __init__(self, id, title, description, due_date, priority):
        self.id = id
        self.title = title
        self.description = description
        self.done = False
        self.due_date = due_date
        self.priority = priority

    def mark_done(self):
        self.done = True
    
    def mark_undone(self):
        self.done = False

    def is_done(self):
        return self.done