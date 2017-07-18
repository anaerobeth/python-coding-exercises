"""
Inflight Entertainment
Choose two movies whose total runtimes will equal the exact flight length
"""

def choose_movies(flight_length, movie_lengths):
    match = False
    seen_movies = set()
    for movie_length in movie_lengths:
        other_movie_length = flight_length - movie_length
        if other_movie_length in seen_movies:
            match = True
        seen_movies.add(movie_length)
    return match

print(choose_movies(4, [1, 2, 3, 4]))
print(choose_movies(4, [1, 1, 2, 4]))
