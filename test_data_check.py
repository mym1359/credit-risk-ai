import pandas as pd

us = pd.read_csv("data/us_census_2021.csv")
aus = pd.read_csv("data/aus_population_stats.csv")

print("US shape:", us.shape)
print("AUS shape:", aus.shape)
print("US columns:", us.columns)
print("AUS columns:", aus.columns)