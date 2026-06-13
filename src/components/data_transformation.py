"""
data_transformation.py

Purpose
-------
This module is responsible for:

1. Reading train and test datasets
2. Creating preprocessing pipelines
3. Handling missing values
4. Scaling numerical features
5. Encoding categorical features
6. Saving preprocessing object
7. Returning transformed datasets


"""

# =====================================================
# Built-in Libraries
# =====================================================

import os
import sys

# =====================================================
# Third Party Libraries
# =====================================================

import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline

from sklearn.impute import SimpleImputer

from sklearn.preprocessing import (
    StandardScaler,
    OneHotEncoder
)

# =====================================================
# Project Imports
# =====================================================

from src.logger import logging

from src.exception import CustomException

from src.entity.config_entity import (
    DataTransformationConfig
)

from src.utils.common import (
    save_object
)


class DataTransformation:
    """
    Data Transformation Component

    Responsibilities:
    -----------------
    1. Create preprocessing pipeline
    2. Transform train data
    3. Transform test data
    4. Save preprocessor object
    """

    def __init__(
        self,
        config: DataTransformationConfig
    ):

        self.config = config

    def get_data_transformer_object(self):
        """
        Create preprocessing object

        Returns
        -------
        ColumnTransformer
        """

        try:

            logging.info(
                "Creating Data Transformation Pipeline"
            )

            # ==========================================
            # Numerical Features
            # ==========================================

            numerical_columns = [
                "Year",
                "Kms_Driven",
                "Present_Price",
                "Owner"
            ]

            # ==========================================
            # Categorical Features
            # ==========================================

            categorical_columns = [
                "Fuel_Type",
                "Transmission",
                "Seller_Type"
            ]

            # ==========================================
            # Numerical Pipeline
            # ==========================================

            numerical_pipeline = Pipeline(

                steps=[

                    (
                        "imputer",

                        SimpleImputer(
                            strategy="median"
                        )
                    ),

                    (
                        "scaler",

                        StandardScaler()
                    )
                ]
            )

            """
            Explanation:

            Step 1:
            Fill missing values using median

            Step 2:
            Standardize numerical values

            Formula:

            z = (x - mean)/std
            """

            # ==========================================
            # Categorical Pipeline
            # ==========================================

            categorical_pipeline = Pipeline(

                steps=[

                    (
                        "imputer",

                        SimpleImputer(
                            strategy="most_frequent"
                        )
                    ),

                    (
                        "onehot",

                        OneHotEncoder(
                            handle_unknown="ignore",
                            sparse_output=False
                        )
                    )
                ]
            )

            """
            Explanation:

            Step 1:
            Fill missing categorical values

            Step 2:
            Convert categories into numbers

            Example:

            Petrol → [1,0,0]
            Diesel → [0,1,0]
            """

            # ==========================================
            # Combine Both Pipelines
            # ==========================================

            preprocessor = ColumnTransformer(

                [

                    (
                        "numerical_pipeline",

                        numerical_pipeline,

                        numerical_columns
                    ),

                    (
                        "categorical_pipeline",

                        categorical_pipeline,

                        categorical_columns
                    )

                ]
            )

            logging.info(
                "Preprocessor Created Successfully"
            )

            return preprocessor

        except Exception as e:

            raise CustomException(
                e,
                sys
            )

    def initiate_data_transformation(
        self,
        train_path,
        test_path
    ):
        """
        Main Transformation Function

        Parameters
        ----------
        train_path : str

        test_path : str

        Returns
        -------
        train_array
        test_array
        preprocessor_path
        """

        try:

            logging.info(
                "Reading Train and Test Data"
            )

            # ==========================================
            # Read CSV Files
            # ==========================================

            train_df = pd.read_csv(
                train_path
            )

            test_df = pd.read_csv(
                test_path
            )

            logging.info(
                "Train and Test Data Loaded"
            )

            # ==========================================
            # Target Column
            # ==========================================

            target_column = (
                "Selling_Price"
            )

            # ==========================================
            # Separate Features and Target
            # ==========================================

            X_train = train_df.drop(
                columns=[target_column],
                axis=1
            )

            y_train = train_df[
                target_column
            ]

            X_test = test_df.drop(
                columns=[target_column],
                axis=1
            )

            y_test = test_df[
                target_column
            ]

            logging.info(
                "Feature Target Split Completed"
            )

            # ==========================================
            # Get Preprocessor
            # ==========================================

            preprocessing_obj = (
                self.get_data_transformer_object()
            )

            # ==========================================
            # Fit and Transform Train Data
            # ==========================================

            X_train_transformed = (

                preprocessing_obj.fit_transform(
                    X_train
                )

            )

            """
            fit_transform()

            Fit:
                Learn statistics

                Mean
                Std
                Categories

            Transform:
                Apply transformations
            """

            # ==========================================
            # Transform Test Data
            # ==========================================

            X_test_transformed = (

                preprocessing_obj.transform(
                    X_test
                )

            )

            """
            IMPORTANT

            We NEVER do:

            fit_transform(X_test)

            because it causes
            Data Leakage
            """

            logging.info(
                "Transformation Completed"
            )

            # ==========================================
            # Save Preprocessor Object
            # ==========================================

            save_object(

                file_path=

                self.config
                .preprocessor_obj_file_path,

                obj=preprocessing_obj
            )

            logging.info(
                "Preprocessor Saved Successfully"
            )

            # ==========================================
            # Combine Features and Target
            # ==========================================

            train_arr = np.c_[

                X_train_transformed,

                np.array(y_train)

            ]

            test_arr = np.c_[

                X_test_transformed,

                np.array(y_test)

            ]

            """
            np.c_

            Column-wise concatenation

            Features + Target
            """

            logging.info(
                "Transformation Pipeline Completed"
            )

            return (

                train_arr,

                test_arr,

                self.config
                .preprocessor_obj_file_path

            )

        except Exception as e:

            raise CustomException(
                e,
                sys
            )