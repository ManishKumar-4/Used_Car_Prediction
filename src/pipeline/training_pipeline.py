"""
training_pipeline.py

Purpose
-------
This file orchestrates the complete
training workflow.

Pipeline Flow
-------------

1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Training

This is the entry point of model training.
"""

# ==========================================
# Built-in Libraries
# ==========================================

import sys

# ==========================================
# Project Imports
# ==========================================

from src.logger import logging

from src.exception import CustomException

# Configuration Manager

from src.config.configuration import (
    ConfigurationManager
)

# Components

from src.components.data_ingestion import (
    DataIngestion
)

from src.components.data_validation import (
    DataValidation
)

from src.components.data_transformation import (
    DataTransformation
)

from src.components.model_trainer import (
    ModelTrainer
)


class TrainingPipeline:
    """
    Complete Training Pipeline

    Responsibilities
    ----------------
    1. Run Data Ingestion
    2. Run Validation
    3. Run Transformation
    4. Run Model Training
    """

    def __init__(self):
        """
        Constructor

        Currently no initialization
        required.
        """
        pass

    def initiate_training_pipeline(self):
        """
        Execute complete ML workflow.

        Flow
        ----
        Data Ingestion
            ↓
        Data Validation
              ↓
        Data Transformation
              ↓
        Model Training
        """

        try:

            logging.info(
                "Training Pipeline Started"
            )

            # ==================================
            # Configuration Manager
            # ==================================

            config = (
                ConfigurationManager()
            )

            logging.info(
                "Configuration Manager Created"
            )

            # ==================================
            # DATA INGESTION
            # ==================================

            logging.info(
                "Starting Data Ingestion"
            )

            ingestion_config = (

                config
                .get_data_ingestion_config()

            )

            data_ingestion = (

                DataIngestion(
                    ingestion_config
                )

            )

            train_path, test_path = (

                data_ingestion
                .initiate_data_ingestion()

            )

            logging.info(
                f"Train File : {train_path}"
            )

            logging.info(
                f"Test File : {test_path}"
            )

            logging.info(
                "Data Ingestion Completed"
            )

            # ==================================
            # DATA VALIDATION
            # ==================================

            logging.info(
                "Starting Data Validation"
            )

            validation_config = (

                config
                .get_data_validation_config()

            )

            data_validation = (

                DataValidation(
                    validation_config
                )

            )

            validation_status = (

                data_validation
                .validate_dataset_schema()

            )

            logging.info(
                f"Validation Status : "
                f"{validation_status}"
            )

            # ==================================
            # VALIDATION CHECK
            # ==================================

            if not validation_status:

                logging.error(
                    "Data Validation Failed"
                )

                raise Exception(
                    "Data Validation Failed"
                )

            # ==================================
            # DATA TRANSFORMATION
            # ==================================

            logging.info(
                "Starting Data Transformation"
            )

            transformation_config = (

                config
                .get_data_transformation_config()

            )

            data_transformation = (

                DataTransformation(
                    transformation_config
                )

            )

            train_arr, test_arr, preprocessor_path = (

                data_transformation
                .initiate_data_transformation(

                    train_path,

                    test_path

                )

            )

            logging.info(
                f"Preprocessor Saved At : "
                f"{preprocessor_path}"
            )

            logging.info(
                "Data Transformation Completed"
            )

            # ==================================
            # MODEL TRAINING
            # ==================================

            logging.info(
                "Starting Model Training"
            )

            trainer_config = (

                config
                .get_model_trainer_config()

            )

            model_trainer = (

                ModelTrainer(
                    trainer_config
                )

            )

            r2_score_value = (

                model_trainer
                .initiate_model_trainer(

                    train_arr,

                    test_arr

                )

            )

            logging.info(
                "Model Training Completed"
            )

            logging.info(
                f"Final R2 Score : "
                f"{r2_score_value}"
            )

            logging.info(
                "Training Pipeline Finished Successfully"
            )

            return r2_score_value

        except Exception as e:

            logging.error(
                f"Training Pipeline Failed : {str(e)}"
            )

            raise CustomException(
                e,
                sys
            )


# ==================================================
# MAIN ENTRY POINT
# ==================================================
#
# This block executes only when this file
# is run directly.
#
# Example:
#
# python src/pipeline/training_pipeline.py
#
# Without this block:
# Nothing happens.
#
# ==================================================

if __name__ == "__main__":

    try:

        logging.info(
            "Application Started"
        )

        print(
            "\nTraining Pipeline Started...\n"
        )

        pipeline = TrainingPipeline()

        result = (

            pipeline
            .initiate_training_pipeline()

        )

        print(
            f"\nTraining Completed Successfully"
        )

        print(
            f"Final R2 Score : {result}\n"
        )

        logging.info(
            "Application Finished Successfully"
        )

    except Exception as e:

        print(
            f"\nTraining Failed : {e}\n"
        )

        logging.error(
            f"Application Failed : {str(e)}"
        )

        raise