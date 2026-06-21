import pandas as pd

df = pd.read_csv("data/raw/Astram event data_anonymized.csv")

print("\nEVENT TYPES:")
print(df["event_type"].dropna().unique()[:20])

print("\nEVENT CAUSES:")
print(df["event_cause"].dropna().unique()[:20])

print("\nZONES:")
print(df["zone"].dropna().unique()[:20])

print("\nCORRIDORS:")
print(df["corridor"].dropna().unique()[:20])

print("\nPOLICE STATIONS:")
print(df["police_station"].dropna().unique()[:20])

print("\nJUNCTIONS:")
print(df["junction"].dropna().unique()[:20])