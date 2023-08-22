import pandas as pd
import numpy as np


df = pd.read_csv("squirrel.csv", usecols=["Primary Fur Color","Hectare Squirrel Number"], sep="," )

black_color = df["Primary Fur Color"].str.count("Black").sum()
gray_color = df["Primary Fur Color"].str.count("Gray").sum()
cinnamon_color = df["Primary Fur Color"].str.count("Cinnamon").sum()


df2 = pd.DataFrame(columns=['Fur Color', 'Count'])
df2.loc[:, "Fur Color"] = ["Black", "Gray", "Cinnamon"]
df2.loc[:, "Count"] = [black_color, gray_color, cinnamon_color]

print(df2)

# df2.to_csv("clear.csv")