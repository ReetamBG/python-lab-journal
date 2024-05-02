# Write a program to perform Chi square test

import numpy as np
import pandas as pd
import scipy.stats as st

population = pd.Series([100000, 60000, 50000, 15000, 35000], name='population')
sample = pd.Series([600, 300, 250, 75, 150], name='sample')

population_proportion = population.apply(lambda x : x/sum(population))

observed_values = sample
expected_values = sample.sum() * population_proportion

chi_squared = ((observed_values - expected_values)**2 / expected_values).sum()
crit = st.chi2.ppf(q = 0.95, df = 4)
p_value = 1 - st.chi2.cdf(x = chi_squared, df = 4)

print('Chi square value : {}\nCritical value : {}\nP value : {}'.format(chi_squared, crit, p_value))