"""
configuration.py

Purpose
-------
Central configuration manager.

Responsibilities
----------------
1. Create artifact folders
2. Manage file paths
3. Provide configs to components
"""

# ==========================================
# Built-in Libraries
# ==========================================

import os

# ==========================================
# Project Imports
# ==========================================

from src.entity.config_entity import (

    DataIngestionConfig,

    DataValidationConfig,

    DataTransformationConfig,

    ModelTrainerConfig

)


class ConfigurationManager:
    """
    Configuration Manager

    Provides configuration
    for all pipeline stages.
    """

    def __init__(self):

        # ==================================
        # Artifact Folder
        # ==================================

        self.artifacts_dir = (
            "artifacts"
        )

        os.makedirs(
            self.artifacts_dir,
            exist_ok=True
        )

    # ======================================
    # DATA INGESTION CONFIG
    # ======================================

    def get_data_ingestion_config(
        self
    ) -> DataIngestionConfig:

        """
        Create configuration
        for Data Ingestion.
        """

        train_data_path = os.path.join(

            self.artifacts_dir,

            "train.csv"

        )

        test_data_path = os.path.join(

            self.artifacts_dir,

            "test.csv"

        )

        raw_data_path = os.path.join(

            self.artifacts_dir,

            "raw.csv"

        )

        ingestion_config = (

            DataIngestionConfig(

                train_data_path=
                train_data_path,

                test_data_path=
                test_data_path,

                raw_data_path=
                raw_data_path

            )

        )

        return ingestion_config

    # ======================================
    # DATA VALIDATION CONFIG
    # ======================================

    def get_data_validation_config(
        self
    ) -> DataValidationConfig:

        """
        Create configuration
        for Data Validation.
        """

        validation_config = (

            DataValidationConfig(

                data_path=os.path.join(

                    self.artifacts_dir,

                    "raw.csv"

                ),

                status_file_path=
                os.path.join(

                    self.artifacts_dir,

                    "validation_status.txt"

                ),

                required_columns=['Car_Name','Year','Selling_Price','Present_Price','Kms_Driven','Fuel_Type',
                'Seller_Type','Transmission','Owner'
                ],

                target_column=
                "Selling_Price"

            )

        )

        return validation_config

    # ======================================
    # DATA TRANSFORMATION CONFIG
    # ======================================

    def get_data_transformation_config(
        self
    ) -> DataTransformationConfig:

        """
        Create configuration
        for Data Transformation.
        """

        preprocessor_path = os.path.join(

            self.artifacts_dir,

            "preprocessor.pkl"

        )

        transformation_config = (

            DataTransformationConfig(

                preprocessor_obj_file_path=
                preprocessor_path

            )

        )

        return transformation_config

    # ======================================
    # MODEL TRAINER CONFIG
    # ======================================

    def get_model_trainer_config(
        self
    ) -> ModelTrainerConfig:

        """
        Create configuration
        for Model Training.
        """

        model_path = os.path.join(

            self.artifacts_dir,

            "model.pkl"

        )

        trainer_config = (

            ModelTrainerConfig(

                trained_model_file_path=
                model_path

            )

        )

        return trainer_config