"""
data_validation.py

Purpose
-------
This module validates incoming data before
it reaches preprocessing and model training.

Validation Checks:
------------------
1. File existence
2. Empty dataset check
3. Required column validation
4. Column count validation
5. Duplicate check
6. Null column check
7. Target column validation
"""

# ==================================================
# Built-in Libraries
# ==================================================

import os
import sys

# ==================================================
# Third Party Libraries
# ==================================================

import pandas as pd

# ==================================================
# Project Imports
# ==================================================

from src.logger import logging

from src.exception import CustomException

from src.entity.config_entity import (
    DataValidationConfig
)


class DataValidation:
    """
    Data Validation Component

    Responsibilities
    ----------------
    Validate dataset quality before
    transformation begins.
    """

    def __init__(self,config: DataValidationConfig):

        self.config = config

    def validate_dataset_schema(
        self
    ) -> bool:
        """
        Main validation method

        Returns
        -------
        bool

        True  -> Validation Passed
        False -> Validation Failed
        """

        try:

            validation_status = True

            logging.info(
                "Starting Data Validation"
            )

            # =====================================
            # Read Dataset
            # =====================================

            df = pd.read_csv(
                self.config.data_path
            )

            logging.info(
                f"Dataset Loaded. Shape: {df.shape}"
            )

            # =====================================
            # Check 1:
            # Dataset Empty?
            # =====================================

            if df.shape[0] == 0:

                logging.warning(
                    "Dataset is Empty"
                )

                validation_status = False

            # =====================================
            # Check 2:
            # Required Columns
            # =====================================

            expected_columns = (

                self.config
                .required_columns

            )

            for column in expected_columns:

                if column not in df.columns:

                    logging.warning(
                        f"Missing Column: {column}"
                    )

                    validation_status = False

            # =====================================
            # Check 3:
            # Column Count
            # =====================================

            if len(df.columns) != len(
                expected_columns
            ):

                logging.warning(
                    "Column Count Mismatch"
                )

                validation_status = False

            # =====================================
            # Check 4:
            # Target Column Exists
            # =====================================

            if (

                self.config.target_column

                not in df.columns

            ):

                logging.warning(
                    "Target Column Missing"
                )

                validation_status = False

            # =====================================
            # Check 5:
            # Duplicate Records
            # =====================================

            duplicate_count = (

                df.duplicated()
                .sum()

            )

            if duplicate_count > 0:

                logging.warning(

                    f"{duplicate_count} "
                    "Duplicate Rows Found"

                )

            # =====================================
            # Check 6:
            # Entire Null Columns
            # =====================================

            null_columns = []

            for column in df.columns:

                if (

                    df[column]
                    .isnull()
                    .all()

                ):

                    null_columns.append(
                        column
                    )

            if len(null_columns) > 0:

                logging.warning(

                    f"Fully Null Columns: "
                    f"{null_columns}"

                )

                validation_status = False

            # =====================================
            # Save Validation Result
            # =====================================

            with open(

                self.config
                .status_file_path,

                "w"

            ) as file:

                file.write(

                    f"Validation Status: "
                    f"{validation_status}"

                )

            logging.info(
                "Validation Completed"
            )

            return validation_status

        except Exception as e:

            raise CustomException(
                e,
                sys
            )