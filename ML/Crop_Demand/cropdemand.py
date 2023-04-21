import pandas as pd
import numpy as np

commodity_counts = pd.read_csv("Crop_Demand\cropdemand.csv")

def make_predictions(market, season, crops):
    # Initialize the dictionary to store the recommended percentages
    crop_percentages = {}
    for crop in crops:
        crop_percentages[crop] = 0

    for i, row in commodity_counts.iterrows():
        if row['Market'] == market and row['Season'] == season:
            for crop in crops:
                crop_percentages[crop] = row[crop]/ row.sum()

    # Calculate the recommended number of each crop to grow based on the user input
    crop_counts = {}
    for crop in crops:
        crop_counts[crop] = round(crop_percentages[crop] * 100)

    return crop_counts

market = 'Parsoniya Mandi, Mahua block'
season = 'Rabi'
crops = ['Cabbage', 'Green Chilli', 'Tomato']

predictions = make_predictions(market, season, crops)
print(predictions)