import argparse
import logging
logging.basicConfig(level=logging.INFO)
import pandas as pd
import os
import time

logger = logging.getLogger(__name__)

def main(filename):
    logger.info('Starting cleaning process')
    
    df=_read_data(filename) #read fiel
    date_id = _extract_date(filename) #extract date of data
    df = _add_date_id_col(df,date_id) #add date as a column
    df = _generate_energy(df) #calculate a energy percentage
    #df = _saving_file(df) arreglar
    return df
    
def _read_data(filename):
    logger.info('Reading file {}'.format(filename))
    
    return pd.read_csv(filename)

def _extract_date(filename):
    logger.info('Extracting date when data are obtained')
    getting_date = time.strptime(time.ctime(os.path.getmtime(filename)))
    date_id = time.strftime("%Y-%m-%d",getting_date)
    
    logger.info('Data was obtained: {}'.format(date_id))
    return date_id

def _add_date_id_col(df,data):
    logger.info('Filling data_id column with {}'.format(data))
    df['data_id'] = data
    
    return df

def _generate_energy(df):
    logger.info('Calculating energy percentage from {}'.format(df))
    df['Energy (%)'] = df['energy'].apply(lambda x:x*100)
    
    return df

def _saving_file(df):
    logger.info('Saving file {}'.format(df))
    file= df.to_pickle('Result.csv')
    return file
    
if __name__ == '__main__':
    parser =argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='The path to the dirty data',
                        type=str)
    
    arg = parser.parse_args()
    df = main(arg.filename)
    print(df)
    