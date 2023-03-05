import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data/final/fitlab_data.csv', index_col=0)

print(data.head())