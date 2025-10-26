import pandas as pd

def preprocess(df, region_df):
    #Filtering out the Summer Olympics data
    df=df[df['Season']=='Summer']
    #Merging the two dataframes on 'NOC' column
    df=df.merge(region_df, how='left', on='NOC')
    #Dropping duplicates to ensure each athlete's participation is counted only once per event
    df.drop_duplicates(inplace=True)
    #one-hot encoding the 'Medal' column to create separate columns for each medal type
    df=pd.concat([df, pd.get_dummies(df['Medal'], dtype=int)], axis=1)
    return df
