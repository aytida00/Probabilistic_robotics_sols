import numpy as np
from numpy import random

# Transition function:
# rows are today and columns are tomorrow. 
# sunny = 0, cloudy = 1, rainy = 2
Tf = np.zeros((3, 3))
Tf[0][0] = 0.8
Tf[0][1] = 0.2
Tf[0][2] = 0.0
Tf[1][0] = 0.4
Tf[1][1] = 0.4
Tf[1][2] = 0.2
Tf[2][0] = 0.2
Tf[2][1] = 0.6
Tf[2][2] = 0.2

# b) write a simulator that can randomly generate sequences of "weathers" from the Tf.
# let's have 100x20 matrix that will store days simulated\
total_tests = 2000
total_sequenc_days = 200
weather_sequence = np.zeros((total_tests, total_sequenc_days))
number_of_days = np.zeros(3)
for i in range(0,total_tests):
    for j in range(0,(total_sequenc_days-1)):
        if j == 0:
            weather_sequence[i][j] = random.choice([0, 1, 2], p=[1/3, 1/3, 1/3])  # selecting random today
        match weather_sequence[i][j]:
            case 0:
                weather_sequence[i][j+1] = random.choice([0, 1, 2], p=[0.8, 0.2, 0.0])
                number_of_days[0] += 1
            case 1:
                weather_sequence[i][j+1] = random.choice([0, 1, 2], p=[0.4, 0.4, 0.2])
                number_of_days[1] += 1
            case 2:
                weather_sequence[i][j+1] = random.choice([0, 1, 2], p=[0.2, 0.6, 0.2])
                number_of_days[2] += 1
    match weather_sequence[i][total_sequenc_days-1]:
        case 0:
            number_of_days[0] += 1
        case 1:
            number_of_days[1] += 1
        case 2:
            number_of_days[2] += 1


# c) Stationary distribution of Markov Chain
print(f"Prob that random day is Sunny day: {float(number_of_days[0]/(total_sequenc_days*total_tests))}")
print(f"Prob that random day is Cloudy day: {float(number_of_days[1]/(total_sequenc_days*total_tests))}")
print(f"Prob that random day is Rainy day: {float(number_of_days[2]/(total_sequenc_days*total_tests))}")

