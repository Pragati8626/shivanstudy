import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

df = pd.read_csv("ShivamStudySchedule.csv")
#print(df)
qsn = df["NoOfQuestions"]
#print(qsn)
topic = df["MathsTopic"]
#print(topic)
date = df["Date"]
#print(date)
sns.set_theme(style="whitegrid")
rcParams["figure.figsize"]= 10,10
sns.barplot(x='Date', y='NoOfQuestions', hue='MathsTopic', data=df)

x_range = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
plt.yticks(x_range)

plt.xlabel("Dates", fontsize = 16)
plt.ylabel("Number of questions", fontsize = 16)

plt.show()


