class Subject_manager:
    def __init__(self, subjects=[]):
        self.subjects = subjects

    def add_subject(self, subject):
        self.subjects.append(subject)

    def delete_subject(self, name):
        for subject in self.subjects:
            if subject.name == name:
                self.subjects.remove(subject)

    def get_subjects(self):
        return self.subjects