import pandas as pd
from pathlib import Path
def load_data():
    script_dir=Path(__file__).resolve().parent
    data_folder=script_dir/"data"
    data=data_folder/"netflix_titles.csv"
    df=pd.read_csv(data)
    return df
df=load_data()
def dataset_overview(df):
    df.info()
    print(df.describe(include='all'))
    print(df.columns)
    print(df.head())
    print(df.shape)
def missing_values_analysis(df):
    print(df.isna().sum())
    print(df.isna().mean()*100)
def duplicate_analysis(df):
    print(df.duplicated().sum())
def remove_missing_values(df):
    df_cleaned=df.dropna(subset=['date_added','rating','duration'])
    return df_cleaned
df_cleaned=remove_missing_values(df)
def changing_datetime_format(df_cleaned):
    df_cleaned['date_added']=pd.to_datetime(df_cleaned['date_added'])
    return df_cleaned
    
