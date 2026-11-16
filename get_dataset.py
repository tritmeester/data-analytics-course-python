import pandas as pd
import kagglehub
import os
import ftfy
import numpy as np
import ast

def try_literal(val):
    try:
        return ast.literal_eval(val)
    except:
        return None

def clean_uber_dataset(year = 2025, frac = 0.1) -> None:


    raw_df = pd.read_parquet(f"data/fhvhv_tripdata_{year}-01.parquet")

    #{'HV0003': 'Uber','HV0005': 'Lyft' }
    cleaned_df = raw_df.sample(frac =frac, random_state = 42).loc[pd.col('hvfhs_license_num') == 'HV0003'].drop(columns = ['hvfhs_license_num', 'dispatching_base_num', 'originating_base_num','wav_request_flag', 'wav_match_flag', 'access_a_ride_flag', 'shared_request_flag', 'shared_match_flag', 'airport_fee', 'bcf', 'congestion_surcharge', 'cbd_congestion_fee'] ).rename(columns = {"PULocationID" : "pickup_zone_id", "DOLocationID": "dropoff_zone_id", "trip_time": "trip_seconds"}).reset_index(names = 'ride_id')
        
    cleaned_df.to_parquet(f"data/uber_dataset_{year}-01.parquet", index = False)


def get_movies_dataset() -> None:

    kaggle_folder = kagglehub.dataset_download("rounakbanik/the-movies-dataset")
    kaggle_file_path = os.path.join(kaggle_folder, "movies_metadata.csv")

    movies_df = pd.read_csv(kaggle_file_path, encoding='latin1') 

    movies_df = movies_df.drop(columns = ["belongs_to_collection", "imdb_id", "poster_path", "homepage", "video", "popularity", "adult", "status"]).assign(id = lambda df: pd.to_numeric(df['id'], errors='coerce'), budget = lambda df: pd.to_numeric(df['budget'], errors='coerce'), release_date = lambda df: pd.to_datetime(df['release_date'], errors='coerce')).dropna(subset = ['id']).astype({"id": int, "budget": 'Int64', "revenue": 'Int64', "runtime": 'Int64', "vote_count": 'Int64'}).replace({"revenue":0, "budget": 0}, np.nan)
    
    movies_df = movies_df.assign(spoken_languages=lambda df: df['spoken_languages'].apply(try_literal),
                                genres=lambda df: df['genres'].apply(try_literal),
                                production_companies=lambda df: df['production_companies'].apply(try_literal),
                                production_countries=lambda df: df['production_countries'].apply(try_literal))

    movies_df = movies_df.rename(columns = {"id": "movie_id"})

    # fix string column formatting
    movies_df = movies_df.assign(
        title=lambda df: df['title'].apply(lambda x: ftfy.fix_text(x) if isinstance(x, str) else x),
        overview=lambda df: df['overview'].apply(lambda x: ftfy.fix_text(x) if isinstance(x, str) else x),
        tagline=lambda df: df['tagline'].apply(lambda x: ftfy.fix_text(x) if isinstance(x, str) else x),
        original_title=lambda df: df['original_title'].apply(lambda x: ftfy.fix_text(x) if isinstance(x, str) else x)
    )

    movies_df = movies_df.dropna(subset = ['release_date', 'vote_count', 'vote_average'])

    movies_df = movies_df[movies_df['release_date'].dt.year <= 2017]

    movies_df = movies_df[['movie_id', 'title',  'release_date','overview', 'tagline', 'original_language', 'original_title',
        'budget','revenue', 'runtime',  'vote_average', 'vote_count',
            'genres', 'production_companies', 'production_countries', 'spoken_languages']]

    movies_df =  movies_df.assign(genres = pd.col('genres').apply(lambda genres: [genre['name'] for genre in genres]))

    spoken_languages_df = movies_df[["movie_id", "spoken_languages"]].explode("spoken_languages").dropna(subset = ["spoken_languages"]).rename(columns = {"spoken_languages": "language"})

    spoken_languages_df = spoken_languages_df.assign(language_id = lambda df: df['language'].apply(lambda x: x['iso_639_1'] if isinstance(x, dict) and 'iso_639_1' in x else None), language_name = lambda df: df['language'].apply(lambda x: ftfy.fix_text(x["name"]) )).drop(columns = ["language"])


    movies_df = movies_df.drop(columns = ["production_companies", "production_countries", "spoken_languages"])

    spoken_languages_df.to_csv("data/movies_spoken_languages.csv", index = False)
    movies_df.to_csv("data/movies.csv", index = False)


