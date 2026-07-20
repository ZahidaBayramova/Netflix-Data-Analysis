import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
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
    df_cleaned=df.dropna(subset=['date_added','rating','duration']).copy()
    return df_cleaned
df_cleaned=remove_missing_values(df)
def changing_datetime_format(df_cleaned):
    df_cleaned['date_added']=df_cleaned['date_added'].str.strip()
    df_cleaned['date_added']=pd.to_datetime(df_cleaned['date_added'])
    return df_cleaned
    
df_cleaned=changing_datetime_format(df_cleaned)
def general_statistics(df_cleaned):
    type_statistic=df_cleaned['type'].value_counts()
    print(type_statistic)
    row_count=len(df_cleaned)
    print(row_count)
    num_columns=len(df_cleaned.columns)
    print(num_columns)
def content_type_analysis_barchart(df_cleaned):
    cat=df_cleaned['type'].value_counts()
    plt.bar(cat.index,cat.values)
    plt.title("Content Type Distribution")
    plt.xlabel("Films and TV Shows")
    plt.ylabel("Numbers")
    plt.show()
def content_type_analysis_piechart(df_cleaned):
        
    cat=df_cleaned['type'].value_counts()
    plt.figure(figsize=(10,10))
    plt.pie(cat,
            labels=cat.index,
            autopct="%1.1f%%",
            shadow=True)
    plt.title("Content Type Distribution")
    plt.show()
def top_countries(df_cleaned):
    df_cleaned['country']=df_cleaned['country'].str.split(',')
    df_cleaned=df_cleaned.explode('country',ignore_index=True)
    df_cleaned['country']=df_cleaned['country'].str.strip()
    top_country=df_cleaned["country"].value_counts().head(10)
    plt.barh(top_country.index,top_country.values,color='red')
    plt.title("Country Analysis")
    plt.xlabel('Number of Titles')
    plt.ylabel('Countries')
    plt.show()
def release_year_analysis(df_cleaned):
    tvshows=df_cleaned[df_cleaned['type']=='TV Show']
    tvshows_byyear=tvshows['release_year'].value_counts().sort_index()
    movs=df_cleaned[df_cleaned['type']=='Movie']
    movs_byyear=movs['release_year'].value_counts().sort_index()
    plt.plot(tvshows_byyear.index,tvshows_byyear.values,label='TV Shows')
    plt.plot(movs_byyear.index,movs_byyear.values,label='Movies')
    plt.xlabel("Release Year")
    plt.ylabel("Number of Titles")
    plt.title("Movies vs TV Shows by Release Year")
    plt.legend()
    plt.show()
def genre_analysis(df_cleaned):
    df_cleaned['listed_in']=df_cleaned['listed_in'].str.split(',')
    df_cleaned=df_cleaned.explode('listed_in',ignore_index=True)
    df_cleaned['listed_in']=df_cleaned['listed_in'].str.strip()
    genre_counts=df_cleaned['listed_in'].value_counts()
    print(genre_counts.idxmax())
    max_10=genre_counts.head(10)
    plt.barh(max_10.index,max_10.values)
    plt.xlabel('Values')
    plt.ylabel('Genres')
    plt.title('Top 10 genres')
    plt.show()
def dateadded_analysis(df_cleaned):
    df_cleaned['year']=df_cleaned['date_added'].dt.year
    tvshows=df_cleaned[df_cleaned['type']=='TV Show']
    tvshows_byyear=tvshows['year'].value_counts().sort_index()
    movs=df_cleaned[df_cleaned['type']=='Movie']
    movs_byyear=movs['year'].value_counts().sort_index()
    plt.plot(tvshows_byyear.index,tvshows_byyear.values,label='TV Shows')
    plt.plot(movs_byyear.index,movs_byyear.values,label='Movies')
    plt.legend()
    plt.xlabel('Added Year')
    plt.ylabel('Number of Titles')
    plt.title('TV Shows and Movies by Added date')
    plt.show()
def duration_analysis(df_cleaned):
    movies=df_cleaned[df_cleaned['type']=='Movie'].copy()
    movies['duration']=movies['duration'].str.replace(' min','').astype(int)
    print("Maximum duration:", movies['duration'].max())
    print("Minimum duration:", movies['duration'].min())
    print("Average duration:", movies['duration'].mean())
    print("Median duration:", movies['duration'].median())
    plt.hist(movies['duration'],color='red')
    plt.xlabel('Values')
    plt.ylabel('Duration')
    plt.show()
def rating_analysis(df_cleaned):
    ratings=df_cleaned['rating'].value_counts()
    best5=ratings.head(5)
    plt.bar(best5.index,best5.values)
    plt.title('Rating Distribution')
    plt.xlabel('Movies and TV Shows')
    plt.ylabel('Rating')
    plt.show()
def director_analysis(df_cleaned):
    df_cleaned['director']=df_cleaned['director'].str.split(',')
    df_cleaned=df_cleaned.explode('director',ignore_index=True)
    df_cleaned['director']=df_cleaned['director'].str.strip()
    director_count=df_cleaned['director'].value_counts().head(10)
    plt.barh(director_count.index,director_count.values)
    plt.title('Director Analysis')
    plt.xlabel('Counts')
    plt.ylabel('Name of Directors')
    plt.show()
def actor_analysis(df_cleaned):
    df_cleaned['cast']=df_cleaned['cast'].str.split(',')
    df_cleaned=df_cleaned.explode('cast',ignore_index=True)
    df_cleaned['cast']=df_cleaned['cast'].str.strip()
    actor_count=df_cleaned['cast'].value_counts().head(10)
    plt.barh(actor_count.index,actor_count.values)
    plt.title('Actor Analysis')
    plt.xlabel('Counts')
    plt.ylabel('Name of Actors')
    plt.show()
def monthly_trend_analysis(df_cleaned):
    df_cleaned['month_name']=df_cleaned['date_added'].dt.month_name()
    month_count=df_cleaned['month_name'].value_counts().head(10)
    plt.bar(month_count.index,month_count.values)
    plt.title('Monthly Analysis')
    plt.xlabel('Months')
    plt.ylabel('Counts')
    plt.show()

if __name__ == "__main__":
    dataset_overview(df)
    missing_values_analysis(df)
    duplicate_analysis(df)
    general_statistics(df_cleaned)
    content_type_analysis_barchart(df_cleaned)
    content_type_analysis_piechart(df_cleaned)
    top_countries(df_cleaned)
    release_year_analysis(df_cleaned)
    genre_analysis(df_cleaned)
    dateadded_analysis(df_cleaned)
    duration_analysis(df_cleaned)
    rating_analysis(df_cleaned)
    director_analysis(df_cleaned)
    actor_analysis(df_cleaned)
    monthly_trend_analysis