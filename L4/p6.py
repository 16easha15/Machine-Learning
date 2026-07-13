#pip install seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("student.csv")
sns.histplot(data["English_Marks"],kde = True)
plt.show()

data = pd.read_csv("student.csv")
sns.histplot(data["Attendance"],kde=True)
plt.show()

data=pd.read_csv("student.csv")
sns.histplot(data["Math_Marks"],kde=True)
plt.show()