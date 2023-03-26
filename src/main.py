""".DS_Store"""
import os
import pandas as pd

print(os.environ["PATH"])
df = pd.read_csv("abc.csv")
print(df.head())
