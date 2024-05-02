import numpy as np
from scipy import stats
import doctest
import os

def numpy_example():
    arr = np.array([1, 2, 3, 4, 5])
    mean = np.mean(arr)
    median = np.median(arr)
    std_dev = np.std(arr)
    max = np.max(arr)
    min = np.min(arr)

    print("Max value:", max)
    print("Min value:", min)
    print("Mean:", mean)
    print("Median:", median)
    print("Standard Deviation:", std_dev)

def scipy_example():
    data = np.random.normal(0, 1, 1000)
    kurtosis = stats.kurtosis(data)
    skewness = stats.skew(data)
    rth_moment = stats.moment(data, 2)

    print("Kurtosis:", kurtosis)
    print("Skewness:", skewness)
    print("2nd Moment:", rth_moment)

def doctest_example():
    # function to add two numbers
    return lambda x, y: x + y

def os_example():
    cwd = os.getcwd()
    print("Current working directory:", cwd)

    files = os.listdir(cwd)
    print("Files and directories in current directory:", files)


numpy_example()
print()
scipy_example()
print()
os_example()
