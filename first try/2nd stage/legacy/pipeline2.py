from etl2 import *



file_path = "~/Documents/Pipelines/Expense Pipelines/Ver1/first try/end/Justin Expenses 2023 cleaned.csv"

save_path = "~/Documents/Pipelines/Expense Pipelines/Ver1/first try/end/Justin Expenses 2023 2ndStage.csv"



def run_pipeline(file_path:str, save_path:str):

    # TODO - extract
    df = extract(file_path=file_path)

    # TODO - transform
    df = transform(df=df)

    # TODO - load
    load(df = df, save_path=save_path)

    return

# print(__name__)

if __name__ == "__main__":

    run_pipeline(file_path=file_path, save_path=save_path)