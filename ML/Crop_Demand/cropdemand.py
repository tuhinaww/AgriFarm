import pandas as pd
import numpy as np

commodity_counts = pd.read_csv("C:\\Users\\Anouska\\Downloads\\project\\AgriFarm\\ML\\Crop_Demand\\cropdemand.csv")

def make_predictions(market, season, crops):
    crop_percentages = {}
    for crop in crops:
        crop_percentages[crop] = 0

    total_count = 0
    for i, row in commodity_counts.iterrows():
        if row['Market'] == market and row['Season'] == season:
            total_count += row[crops].sum()
            for crop in crops:
                crop_percentages[crop] += row[crop]

    if total_count != 0:
        crop_percentages = {crop: (count / total_count) * 100 for crop, count in crop_percentages.items()}
    else:
        crop_percentages = {}

    # Calculate the recommended number of each crop to grow based on the user input
    crop_counts = {}
    for crop in crops:
        crop_counts[crop] = round(crop_percentages[crop], 2)

    return crop_counts
