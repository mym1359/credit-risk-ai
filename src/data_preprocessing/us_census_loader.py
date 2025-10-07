# src/data_preprocessing/us_census_loader.py

import pandas as pd
import requests

CENSUS_URL = "https://api.census.gov/data/2021/acs/acs5/profile?get=NAME,DP03_0009E,DP03_0021E&for=state:*"

def fetch_us_census_data():
    response = requests.get(CENSUS_URL)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data[1:], columns=data[0])
        df.rename(columns={
            "NAME": "State",
            "DP03_0009E": "UnemploymentRate",
            "DP03_0021E": "PovertyRate"
        }, inplace=True)
        return df
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    df = fetch_us_census_data()
    df.to_csv("data/us_census_2021.csv", index=False)
    print("✅ US Census data saved to data/us_census_2021.csv")