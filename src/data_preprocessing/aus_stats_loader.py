# src/data_preprocessing/aus_stats_loader.py

import pandas as pd

def load_local_abs_data():
    try:
        df = pd.read_csv("data/aus_population_stats.csv")
        print("✅ Australian population data loaded successfully")
        print(df.head())
    except Exception as e:
        print(f"❌ Error loading local ABS data: {e}")

if __name__ == "__main__":
    load_local_abs_data()