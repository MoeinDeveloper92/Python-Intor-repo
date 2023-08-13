import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


sales = pd.read_csv('data\sales_data.csv', parse_dates=["Date"])
print(sales.head())
