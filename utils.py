import pandas as pd
import numpy as np
import re, warnings
warnings.filterwarnings("ignore")

def erro_df_vazio(df):
    if df.empty == True:
        raise ValueError('Dataframe está vazio!')
        
def tratar_colunas(df) -> pd.DataFrame:
    erro_df_vazio(df)
    cols = list(df.columns)
    cols = [col.upper() for col in cols]
    cols = [col.replace(" ","_") for col in cols]
    df.columns = cols
    return df

def tratar_duration(df) -> pd.DataFrame:
    erro_df_vazio(df)
    hour_pattern = r'(\d+)\s*hr'
    minute_pattern = r'(\d+)\s*min'
    duration = list(df["DURATION"])
    hour_match = [re.search(hour_pattern, d) for d in duration]
    minute_match = [re.search(minute_pattern, d) for d in duration]
    df["DURATION_HR"] = [int(d.group(1)) if d else np.nan for d in hour_match]
    df["DURATION_MIN"] = [int(d.group(1)) if d else np.nan for d in minute_match]
    df[["DURATION_HR","DURATION_MIN"]] = df[["DURATION_HR","DURATION_MIN"]].fillna(0)
    df["DURATION_HR"] = df["DURATION_HR"]*60
    df["DURATION_FINAL"] = df["DURATION_HR"] + df["DURATION_MIN"]
    df.drop(["DURATION","DURATION_HR","DURATION_MIN"], axis = 1, inplace = True)
    return df

def tratar_UNKNOWN(df) -> pd.DataFrame:
    erro_df_vazio(df)
    df["SCORE"] = df["SCORE"].str.replace("UNKNOWN","0")
    df["RANK"] = df["RANK"].str.replace("UNKNOWN","0")
    df["SCORED_BY"] = df["SCORED_BY"].str.replace("UNKNOWN","0")
    
    """
    Not yet aired and Currently airing will not have number of episodes
    """
    df["EPISODES"] = df["EPISODES"].str.replace("UNKNOWN","-1")
    return df

def tratar_premiered(df) -> pd.DataFrame:
    erro_df_vazio(df)
    df[['PREMIERED_SEASON','PREMIERED_YEAR']] = df['PREMIERED'].str.split(n=1, expand=True)
    df.drop(["PREMIERED"], axis = 1, inplace = True)
    return df

def tratar_tipo(df) -> pd.DataFrame:
    erro_df_vazio(df)
    df[["SCORE","RANK","EPISODES","SCORED_BY"]] = df[["SCORE","RANK","EPISODES","SCORED_BY"]].astype(float)
    df["PREMIERED_YEAR"] = pd.to_numeric(df['PREMIERED_YEAR'], errors='coerce')
    return df

def tratar_genre(df) -> pd.DataFrame:
    erro_df_vazio(df)
    df["GENRES"] = df["GENRES"].str.replace(" ","")
    genres_dummies = df['GENRES'].str.get_dummies(',')
    df = pd.concat([df, genres_dummies], axis=1)
    df.drop(["GENRES","UNKNOWN"], axis = 1, inplace = True)
    return df