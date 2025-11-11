"""


I have three sets of data:
1. Data extracted from satellite images
2. Data from government sensors
3. data from citizen science projects.

I have generates a 100m by 100 grid oveer my study areas and creaed centroids for each grid cell.
from these grids. I have used the grids to extract data from satellite imagery.
I have spatially aligned all the data to the grid centroids and now want to combine all three datasets into a single dataset for analysis.

TASK: Write a Python script that merges these three datasets based on the grid centroids. 
The final dataset should contain columns for the grid cell ID, satellite data, government sensor data, and citizen science data.
You shopudl also add column for the fused data.
Lets assume the datasets are in CSV format with the following columns:- Satellite Data: 'grid_id', 'satellite_value'
- Government Sensor Data: 'grid_id', 'sensor_value'
- Citizen Science Data: 'grid_id', 'citizen_value'import pandas as pd
The data has been spatially aligned to the grids and temporaly alignbed as well.
It is availabel as a single CSV file with the following columns:
'grid_id', 'satellite_value', 'sensor_value', 'citizen_value'
"""

# Load the datasets
from src.load_data import load_dataset
import pandas as pd
import numpy as np

if __name__ == "__main__":
    file_path = 'dataset/dublin/final_merged_table_.csv'  # Path to the merged CSV file

    data_object = load_dataset(
        file_path, timestamp='timestamp', value_col='no2_values'
    )

print("Data Loaded Successfully")
print('y shape:',   data_object.y.shape)
print('Times:',     data_object.times[:5])
print('Grid IDs:',  data_object.grid_ids[:5])
