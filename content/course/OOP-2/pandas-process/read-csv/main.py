import pandas as pd
import numpy as np


df = pd.read_csv("weather_data.csv", usecols=["day", "temp", "condition"], sep=",")

# data_dict = df.to_dict()
# data_list = df["temp"].to_list()
# df_avg = df["temp"].max()
# print(df_avg)
# print(df[df.day == "Monday"])


# print(df[df.temp == df.temp.max()])

# monday = df[df.day == "Monday"]
# fah_deg = monday.temp * 33.8
# print(fah_deg)

df["temp"] = df["temp"] * 9/5 + 32
print(df)