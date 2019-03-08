import pandas as pd
import numpy as np
from itertools import groupby
import matplotlib.pyplot as plt

STEP_SIZE = 120 # so for each hour
PADDING = 20 # PADDING to the begging and end of the search view
df = pd.read_csv('data.csv', sep=',', header=None)
dfPrice = df[2]

tops = []
bottoms = []


def delete_smaller_than(dictionary, min_size=2):
    temp_dict = dictionary.copy()
    for key in dictionary.keys():
        if temp_dict[key] <= min_size:
            del temp_dict[key]
    return temp_dict


for i in range(0, len(dfPrice)):

    curr_prices = dfPrice[i: i + STEP_SIZE]
    maximum = curr_prices.idxmax()
    minimum = curr_prices.idxmin()

    if maximum not in list(range(i, i + PADDING)) and maximum not in list(range(i + STEP_SIZE - PADDING, i + STEP_SIZE)):
        tops.append(maximum)
    if minimum not in list(range(i, i + PADDING)) and minimum not in list(range(i + STEP_SIZE - PADDING, i + STEP_SIZE)):
        bottoms.append(minimum)

# count frequency for each entry
count_for_entry_max = {key: len(list(group)) for key, group in groupby(tops)}
count_for_entry_min = {key: len(list(group)) for key, group in groupby(bottoms)}

# only get high confidence values
count_for_entry_max = delete_smaller_than(count_for_entry_max)
count_for_entry_min = delete_smaller_than(count_for_entry_min)

# Prepare for matplotlib make empty fields none
highs = np.array([None] * len(dfPrice)) #.astype(np.double)
for item in count_for_entry_max:
    highs[item] = dfPrice[item]

lows = np.array([None] * len(dfPrice))
for item in count_for_entry_min:
    lows[item] = dfPrice[item]

highs = highs.astype(np.double)
lows = lows.astype(np.double)

# plotting
dfPrice.plot()
plt.plot(highs, marker='o', linestyle='-', color="r")
plt.plot(lows, marker='o', linestyle='-', color="g")

plt.show()
print("hello world")