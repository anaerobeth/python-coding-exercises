import math

def adjusted_score(average_rating, max_rating, number_of_ratings):
    """Returns a score after applying a correction for averages
    based on fewer rating events resulting in a conservative estimate"""

    constant = max_rating / 2.0
    score = average_rating - constant / math.sqrt(number_of_ratings)

    return score

average_rating = 4.5
max_rating = 5
number_of_ratings = 16

print(adjusted_score(average_rating, max_rating, number_of_ratings))
