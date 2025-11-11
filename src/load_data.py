
"""
load_data.py
Loads data from disk.
"""


import pandas as pd
import numpy as np
import json
from .data_class import DataLoader

def load_dataset(file_path: str, 
                 timestamp: str, 
                 value_col: str, 
                 grid_id_col='grid_id', 
                 coord_cols=['latitude', 'longitude']) -> DataLoader:
    """
    Load spatio-temporal data from a single CSV containing:
        - grid_id
        - coordinates
        - spatial features
        - time series measurements (value_col)
    """
    # Load the data from CSV
    df = pd.read_csv(file_path)
    df[timestamp] = pd.to_datetime(df[timestamp])

    # Unique times and locations
    times = pd.DatetimeIndex(sorted(df[timestamp].unique()))
    grid_ids = df[grid_id_col].unique()
    L = len(grid_ids)
    T = len(times)

    # Extract spatial features ( coordinates and others if present)

    X = df.drop(columns=[timestamp, value_col]).drop_duplicates(subset=[grid_id_col]).sort_values(by=grid_id_col)
    feature_names = list(X.columns.drop(grid_id_col))
    coordinates = X[coord_cols].to_numpy()
    X = X[feature_names].to_numpy()


    # Build measurement matrix y
    y=np.full((T, L), np.nan)
    grid_id_to_idx = {grid_id: idx for idx, grid_id in enumerate(grid_ids)}
    time_to_idx = {time: idx for idx, time in enumerate(times)}

    for _, row in df.iterrows():
        t = time_to_idx[row[timestamp]]
        g = grid_id_to_idx[row[grid_id_col]]
        y[t, g] = row[value_col]

   

    return DataLoader(
        X=X,
        y=y,
        times=times,
        grid_ids=grid_ids,
        coordinates=coordinates,
        features_names=feature_names
    )
