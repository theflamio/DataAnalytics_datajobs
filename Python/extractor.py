# python/extractor.py
import pandas as pd
from kaggle_api_handler import KaggleAPIHandler

def extract_data():
    """
    Function to extract data from a source.
    """
    config_dir = r'C:\Dev\DataAnalytics_datajobs\TestScripts\kaggle'
    dataset_name = 'lukebarousse/data-analyst-job-postings-google-search'
    save_dir = './datasets'

    # Create an instance of KaggleAPIHandler
    kaggle_handler = KaggleAPIHandler(config_dir)

    # Call the download_dataset method
    kaggle_handler.download_dataset(dataset_name, save_dir)

    data = pd.read_csv('./datasets/gsearch_jobs.csv', sep="\t",) #TODO must remove hardcoded folder structure
    return data
