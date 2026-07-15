# check the dataset
# balanced or imbalanced

import pandas as pd

data = pd.read_csv("heart.csv")
print(data)

print(data["output"].value_counts())