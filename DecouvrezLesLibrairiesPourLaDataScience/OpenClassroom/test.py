import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

mpg = sns.load_dataset('mpg')

sns.set_theme()

origin_count = mpg['origin'].value_counts().reset_index()

plt.pie(labels=origin_count['index'], x=origin_count['origin'], autopct='%.1f%%')
