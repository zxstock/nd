import pandas as pd
import numpy as np
#import os
#cwd = os.getcwd()

df_nasdaq = pd.read_csv('nasdaq.csv')
symbols = df_nasdaq['Symbol'].tolist()


