
"""
Data class module.

"""

import pandas as pd
import numpy as np
from dataclasses import dataclass
from typing import Optional

@dataclass

class DataLoader:
    """
    Class to load and manage datasets for analysis.
    """

    X:np.ndarray
    y:np.ndarray
    times:pd.DatetimeIndex
    grid_ids:np.ndarray
    coordinates:np.ndarray
    features_names:list

    # def __post_init__(self):
    #     assert self.y.shape[0] == self.X.shape[0], "Number of samples in y and X must be the same."
    #     (
    #         f"shape mismatch: y: {self.y.shape}, X: {self.X.shape}"
    #     )