# Reading the data from data sources
import os
import sys
# reson for importing these is because we will be suing our custom exception (exception.py)
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig


# any input that is required or anything that we will requrie will be given through this data ingestion class (similar reason for transformation as well)
@dataclass # this decorator makes you able to directly define your class varible inside a class, without needing to use __init__
class DataIngestionConfig:
    # defining inputs to the data ingestion components, to know where to save train, test and raw data
    train_data_path: str=os.path.join('artifacts', "train.csv")
    test_data_path: str=os.path.join('artifacts', "test.csv")
    raw_data_path: str=os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() # above paths will get saved in this "ingestion_config" variable as soon as the DataIngestion class is run

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv') # reading the dataset
            logging.info('Read the dataset as dataframe')

            # creating directories which are defined above
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            # saving raw data into the location defined above        
            df.to_csv(self.ingestion_config.raw_data_path,index=False, header=True)

            logging.info('Train Test split initiated')
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                # will requrie these for data transformation
            )
        
        except Exception as e:
            raise CustomException(e.sys)
        
# Running the above code
if __name__=="__main__":
    obj=DataIngestion()

    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    data_transformation.initiate_data_tranformation(train_data, test_data)