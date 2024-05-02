# Write a program for finding moment, skewness and kurtosis
# using formulas from scipy.stats

import numpy as np

def mean(data):
    return sum(data)/len(data)

# nth moment
def moment(data, r):
    data = np.array(data)
    return sum((data-mean(data))**r) / len(data)

# second moment -> variance
def variance(data):
    return moment(data, 2)

# third moment -> skewness
def skewness(data):
    return moment(data, 3) / (moment(data, 2)**(3/2))

def kurtosis(data):
    # scipy.stats(fisher=False)
    return moment(data, 4)/ (moment(data, 2)**2)


data = [1, 2, 3, 4, 5, 5, 5, 2, 3, 10]
print('2nd moment : ', moment(data, 2))
print('Mean : ', mean(data))
print('Variance : ', variance(data))
print('Skewness : ', skewness(data))
print('Kurtosis : ', kurtosis(data))



