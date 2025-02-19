class Movie:
    def __init__(self, name, watched=False):
        self.name = name
        self.watched = watched

    def __str__(self):
        return self.name