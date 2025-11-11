
"""
data_setup.py
Loads data from a csv. The file has all the necessary columns already merged.
"""

import pandas as pd
import numpy as np
from loguru import logger


try:
    import pandas as pd