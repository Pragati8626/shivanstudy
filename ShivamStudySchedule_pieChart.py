import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ShivamStudySchedule.csv")
print(df)
qsn = df["NoOfQuestions"]
topic = (df["MathsTopic"])+ " " +(df["Date"].map(str))
date = df["Date"]
plt.pie(qsn, labels = topic, radius = 1.2, autopct = "%0.01f%%")

plt.show()

