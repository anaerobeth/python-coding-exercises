import math

def root_mean_squared_error(actual, predicted):
    """Returns the square root of the mean squared errors obtained by subtracting the squares predicted values from the actual values"""

    if len(actual) == len(predicted):
        squared_errors = 0
        for i in range(len(actual)):
            diff = actual[i] - predicted[i]
            squared_errors += diff * diff

        rmse = math.sqrt(squared_errors / len(actual))
        print(round(rmse, 2))

    else:
        print('Actual ratings and predicted ratings must have the same length')

actual = [1, 2, 3, 4, 5]
predicted = [1.3, 1.5, 2.6, 4.2, 4.8]

root_mean_squared_error(actual, predicted)
# 0.34
