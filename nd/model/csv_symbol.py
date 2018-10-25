import pandas as pd
import numpy as np
#import os
#cwd = os.getcwd()

def return_symbols(csvfile):
    df_nasdaq = pd.read_csv(csvfile)
    df_nasdaq_filter = df_nasdaq[df_nasdaq['IPOyear']<=2014]
    symbols = df_nasdaq_filter['Symbol'].tolist()

    return symbols




