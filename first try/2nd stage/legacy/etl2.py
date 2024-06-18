import pandas as pd
import numpy as np
import datetime
import calendar
from pandas.core.frame import DataFrame

path_prefix = "~/Documents/Pipelines/Expense Pipelines/Ver1/first try/end/"

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

    df['Date'] =pd.to_datetime(df['Date'], format='ISO8601')

    # Extract the month and year from the date column
    df['month'] = df['Date'].dt.month
    df['year'] = df['Date'].dt.year

    # Step 4: Summary statistics
    summary_stats = df.describe()
    summary_stats.to_csv('~/Documents/Pipelines/Expense Pipelines/Ver1/first try/end/summary_statistics.csv')

    # Step 5: Total expenses by category
    total_by_category =df.groupby('Category')['Amount'].sum()
    total_by_category.to_csv(path_prefix + 'total_by_category.csv', header=['Total Amount'])


    # Step 6: Monthly expenses
    monthly_expenses= df.groupby(['year', 'month'])['Amount'].sum().reset_index()
    monthly_expenses.to_csv(path_prefix +'monthly_expenses.csv', index=False)

    # Step 7: Average expenses per category
    average_by_category = df.groupby('Category')['Amount'].mean()
    average_by_category.to_csv(path_prefix + 'average_by_category.csv', header=['Average Amount'])

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
