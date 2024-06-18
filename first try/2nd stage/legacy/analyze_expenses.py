import pandas as pd
import calendar
from pandas.core.frame import DataFrame
# import matplotlib.pyplot as plt
# import seaborn as sns

csv_file = "~/Documents/Pipelines/Expense Pipelines/Ver1/first try/end/expenses_2023.csv"
file_path = "~/Documents/Pipelines/Expense Pipelines/Ver1/first try/end/Justin Expenses 2023 cleaned.csv"

def analyze_expenses(df: DataFrame) -> DataFrame:
    # Step 1: Read the CSV file
    df = pd.read_csv(file_path)

    # Step 2: Convert the date column to a datetime object
    df['Date'] = pd.to_datetime(df['date'], format='mixed')
    # Step 3: Extract the month and year from the date column
    df['month'] = df['Date'].dt.month
    df['year'] = df['Date'].dt.year
    # Step 4: Summary statistics
    summary_stats = df.describe()
    summary_stats.to_csv('~/Documents/Pipelines/Expense Pipelines/Ver1/first try/end/summary_statistics.csv')







    
    # Step 5: Total expenses by category
    # Step 6: Monthly expenses
    # Step 7: Average expenses per category
    # Step 8: Identify outliers
    # Step 9: Cumulative expenses over time
    # Step 10: Pivot table for detailed analysis
    return{
        'summary_stats': summary_stats
    }
# results = analyze_expenses(csv_file)



