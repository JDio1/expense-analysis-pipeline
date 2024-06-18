import pandas as pd
import numpy as np
import datetime
import calendar
from pandas.core.frame import DataFrame

def extract(file_path: str) -> DataFrame:
    '''
    extracts csv data and converts to pandas Dataframe

    args:
        file_path (str): path to the csv file
    
    returns:
        df (DataFrame): pandas dataframe containing the csv data
    '''


    # TODO - # extracts the csv data as pandas dataframe and parse the date column as datetime
    df =  pd.read_csv(file_path)
    

    # TODO - # return the dataframe
    return   df 


def transform(df: DataFrame) -> DataFrame:
    '''
    cleans data

    args:
        df (DataFrame): pandas dataframe containing the raw data
    
    returns:
        df (DataFrame): pandas dataframe containing the clean data
    '''

    #convert date to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='mixed') 
    #extract the month in a new column
    df['Month2'] = df['Date'].dt.month
    #convert the month to text in a new column
    df['Month_name'] = df['Month2'].apply(lambda x: calendar.month_abbr[x])

    df= df.drop(['Month', 'Month2', 'Day'], axis=1)
    df= df[['Date', 'Month_name', 'Category', 'Amount']]
    df.info()


    # TODO - # drop null values
    df.dropna(inplace=True)

    #get month from date column
    # df['Month2'] = df['Date'].dt.month
    
    return df

def load(df: DataFrame, save_path: str):
    '''
    writes pandas Dataframe to csv file

    args:
        df (DataFrame): pandas dataframe containing the clean data
        save_path (str): path to save the csv file
    
    returns:
        None
    '''

    # TODO - # write dataframe to csv
    df.to_csv(save_path, index=False)

    return
