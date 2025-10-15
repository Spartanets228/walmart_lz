from imdb import IMDb

ia = IMDb()
top = ia.get_top250_movies()

for i, movie in enumerate(top[:10], start=1):
    print(f"{i}. {movie['title']} - {movie['rating']}")
