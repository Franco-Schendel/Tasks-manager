import matplotlib.pyplot as plt

class Graphs_creator:
    def __init__(self, mn):
        self.subject_manager = mn

    def draw_graph(self):
        # Data
        subjects = self.subject_manager.get_subjects()
        def get_name(subject):
            return subject.name
        subjects_names = map(get_name, subjects)
        def get_percentage(subject):
            if(subject.total_tasks() == 0): return 100
            return int((subject.tasks_done() / subject.total_tasks()) * 100)
        
        for i in subjects:
            get_percentage(i)
        subjects_percentages = map(get_percentage, subjects)

        subjects_names = list(subjects_names)
        subjects_percentages = list(subjects_percentages)

        # Bar plot
        fig, ax = plt.subplots()
        ax.bar(x = subjects_names, height = subjects_percentages)
        ax.set_ylim(0, 100)
        plt.show()