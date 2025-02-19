import random
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, movies):
        pass

class SuggestionWatchedMoviesStrategy(Strategy):
    def execute(self, movies):
        if movies: return random.choice(movies)

        return None

class SuggestionUnwatchedMoviesStrategy(Strategy):
    def execute(self, movies):
        if movies: return random.choice(movies)
        
        return None

class Context:
    def __init__(self):
        self.strategy = None

    def setStrategy(self, strategy):
        self.strategy = strategy
    
    def executeStrategy(self, movies):
        return self.strategy.execute(movies)