"""
data_ingestion.py

Purpose:
--------
This module is responsible for:

1. Reading raw dataset
2. Splitting data into train and test sets
3. Saving train and test datasets
4. Returning file paths for downstream pipeline

This is the first step of the ML pipeline.
"""

# Built-in libraries
import os
import sys

# Third-party libraries
import pandas as pd

from sklearn.model_selection import train_test_split

# Project-specific imports
from src.logger import logging
from src.exception import CustomException

from src.entity.config_entity import DataIngestionConfig


class DataIngestion:
    """
    DataIngestion Class

    Responsibilities:
    ----------------
    1. Read raw data
    2. Create artifact directory
    3. Split train-test data
    4. Save train/test datasets
    """

    def __init__(self, config: DataIngestionConfig):
        """
        Constructor

        Parameters
        ----------
        config : DataIngestionConfig

        Contains:
        - train_data_path
        - test_data_path
        - raw_data_path
        """

        self.config = config

    def initiate_data_ingestion(self):
        """
        Main method for data ingestion.

        Steps:
        ------
        1. Read CSV
        2. Create artifacts folder
        3. Save raw data
        4. Split train-test
        5. Save train data
        6. Save test data
        7. Return file paths

        Returns
        -------
        tuple
            (
                train_data_path,
                test_data_path
            )
        """

        logging.info(
            "Entered Data Ingestion Component"
        )

        try:

            #################################################
            # Step 1: Read Dataset
            #################################################

            logging.info(
                "Reading dataset from source"
            )

            df = pd.read_csv(
                "data/raw/car_data_test.csv"
            )

            logging.info(
                f"Dataset Loaded Successfully. Shape: {df.shape}"
            )

            #################################################
            # Step 2: Create Artifact Directory
            #################################################

            os.makedirs(
                os.path.dirname(
                    self.config.train_data_path
                ),
                exist_ok=True
            )

            logging.info(
                "Artifact Directory Created"
            )

            #################################################
            # Step 3: Save Raw Dataset
            #################################################

            df.to_csv(
                self.config.raw_data_path,
                index=False,
                header=True
            )

            logging.info(
                "Raw Dataset Saved"
            )

            #################################################
            # Step 4: Train Test Split
            #################################################

            logging.info(
                "Splitting Dataset into Train and Test"
            )

            train_set, test_set = train_test_split(

                df,

                test_size=0.2,

                random_state=42

            )

            logging.info(
                "Train-Test Split Completed"
            )

            #################################################
            # Step 5: Save Train Dataset
            #################################################

            train_set.to_csv(

                self.config.train_data_path,

                index=False,

                header=True

            )

            logging.info(
                "Train Dataset Saved"
            )

            #################################################
            # Step 6: Save Test Dataset
            #################################################

            test_set.to_csv(

                self.config.test_data_path,

                index=False,

                header=True

            )

            logging.info(
                "Test Dataset Saved"
            )

            #################################################
            # Step 7: Return Paths
            #################################################

            logging.info(
                "Data Ingestion Completed Successfully"
            )

            return (

                self.config.train_data_path,

                self.config.test_data_path

            )

        except Exception as e:

            raise CustomException(
                e,
                sys
            )
        
if __name__ == "__main__":

    print("File Executed")