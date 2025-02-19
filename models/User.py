class User:
    def __init__(self, name):
        self.name = name
        self.watchedMovies = []
        self.unwatchedMovies = []

    def addMovie(self, movie):
        if movie.watched:
            self.watchedMovies.append(movie)
        else:
            self.unwatchedMovies.append(movie)
    
    def getWatchedMovies(self):
        return self.watchedMovies
    
    def getUnwatchedMovies(self):
        return self.unwatchedMovies