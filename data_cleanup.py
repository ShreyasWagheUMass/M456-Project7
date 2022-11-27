import numpy as np
import pandas as pd
import os

locations = pd.read_csv(os.path.abspath('./data/FBWMLocationsDemands.csv'))
print(locations)