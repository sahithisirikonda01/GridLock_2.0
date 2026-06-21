import pandas as pd

from utils.config import PROCESSED_DATA

def load_data():
    return pd.read_csv(PROCESSED_DATA)

def total_events(df):
    return len(df)

def planned_events(df):
    return len(df[df["event_type"] == 0])

def unplanned_events(df):
    return len(df[df["event_type"] == 1])

def high_priority_events(df):
    return len(df[df["priority"] == 0])