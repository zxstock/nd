import pandas as pd
import numpy as np
#import os
#cwd = os.getcwd()

def return_symbols(csvfile):
    df_nasdaq = pd.read_csv(csvfile)
    #df_nasdaq_filter = df_nasdaq[df_nasdaq['IPOyear']<=2014] into nd.nd2 table
    #df_nasdaq_filter = df_nasdaq[df_nasdaq['IPOyear'] <= 2018] #into nd.ndall table
    df_nasdaq_filter = df_nasdaq #include all symbols
    symbols = df_nasdaq_filter['Symbol'].tolist()

    return symbols




