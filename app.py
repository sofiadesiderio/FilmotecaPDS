import json
from flask import Flask, render_template, request
from models.Movie import Movie
from models.User import User
from models.Strategy import Context, SuggestionWatchedMoviesStrategy, SuggestionUnwatchedMoviesStrategy

app = Flask(__name__)

with open("data/movies.json", "r", encoding="utf-8") as file:
    dataMovie = json.load(file)

# criando todos os objetos Movie a partir de um arquivo .json
allMovies = [Movie(movie["name"], movie["watched"]) for movie in dataMovie]

# criando um único usuário e adicionando todos os filmes assistidos por ele
singleUser = User("Fernanda Torres")

for movie in allMovies:
    singleUser.addMovie(movie)

@app.route("/", methods=["GET", "POST"])

def index():
    context = Context()
    result = None

    if request.method == "POST":
        suggestionType = request.form.get("suggestion_type")

        if suggestionType == "watched":
            movies = singleUser.getWatchedMovies()
            context.setStrategy(SuggestionWatchedMoviesStrategy())
        else:
            movies = singleUser.getUnwatchedMovies()
            context.setStrategy(SuggestionUnwatchedMoviesStrategy())

        suggestionMovie = context.executeStrategy(movies)

        if suggestionMovie:
            result = f"Veja: {suggestionMovie}"
        else:
            result = "Nenhum filme encontrado para recomendação."
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)