"""
prediction_pipeline.py

Purpose
-------
1. Accept user input
2. Convert input into DataFrame
3. Load preprocessor
4. Transform input data
5. Load trained model
6. Predict car price
"""

# ==========================================
# Built-in Libraries
# ==========================================

import os
import sys

# ==========================================
# Third Party Libraries
# ==========================================

import pandas as pd

# ==========================================
# Project Imports
# ==========================================

from src.exception import CustomException

from src.utils.common import load_object


class PredictPipeline:
    """
    Prediction Pipeline

    Responsibilities
    ----------------
    1. Load model
    2. Load preprocessor
    3. Transform incoming data
    4. Generate predictions
    """

    def __init__(self):
        pass

    def predict(self, features):
        """
        Predict car price

        Parameters
        ----------
        features : DataFrame

        Returns
        -------
        prediction
        """

        try:

            # ==================================
            # Model Path
            # ==================================

            model_path = os.path.join(
                "artifacts",
                "model.pkl"
            )

            # ==================================
            # Preprocessor Path
            # ==================================

            preprocessor_path = os.path.join(
                "artifacts",
                "preprocessor.pkl"
            )

            # ==================================
            # Load Model
            # ==================================

            model = load_object(
                model_path
            )

            # ==================================
            # Load Preprocessor
            # ==================================

            preprocessor = load_object(
                preprocessor_path
            )

            # ==================================
            # Transform Input Data
            # ==================================

            data_scaled = (

                preprocessor.transform(
                    features
                )

            )

            # ==================================
            # Prediction
            # ==================================

            prediction = model.predict(
                data_scaled
            )

            return prediction

        except Exception as e:

            raise CustomException(
                e,
                sys
            )
        
# ==========================================
# Custom Data Class
# ==========================================

class CustomData:
    """
    Collect user input and
    convert it into DataFrame
    """

    def __init__(

        self,

        Year,
        Present_Price,
        Kms_Driven,
        Fuel_Type,
        Seller_Type,
        Transmission,
        Owner

    ):

        self.Year = Year

        self.Present_Price = Present_Price

        self.Kms_Driven = Kms_Driven

        self.Fuel_Type = Fuel_Type

        self.Seller_Type = Seller_Type

        self.Transmission = Transmission

        self.Owner = Owner

    def get_data_as_dataframe(self):
        """
        Convert user input
        into pandas DataFrame
        """

        try:

            custom_data_input_dict = {

                "Year": [self.Year],

                "Present_Price": [
                    self.Present_Price
                ],

                "Kms_Driven": [
                    self.Kms_Driven
                ],

                "Fuel_Type": [
                    self.Fuel_Type
                ],

                "Seller_Type": [
                    self.Seller_Type
                ],

                "Transmission": [
                    self.Transmission
                ],

                "Owner": [
                    self.Owner
                ]

            }

            data_frame = pd.DataFrame(
                custom_data_input_dict
            )

            return data_frame

        except Exception as e:

            raise CustomException(
                e,
                sys
            )