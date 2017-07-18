"""
Inflight Entertainment
Choose two movies whose total runtimes will equal the exact flight length
"""

def choose_movies(flight_length, movie_lengths):
    match = False
    for movie_length in movie_lengths:
        for other_movie_length in movie_lengths:
            if movie_length + other_movie_length == flight_length:
                print(movie_length, other_movie_length)
                match = True
    return match

print(choose_movies(4, [1, 2, 3, 4]))
print(choose_movies(4, [1, 1, 2, 4]))
