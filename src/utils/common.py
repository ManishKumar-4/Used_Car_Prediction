"""
common.py

Purpose
-------
Utility functions used across the project.

Functions
---------
1. save_object()
2. load_object()
3. evaluate_models()

These functions are reused by multiple
pipeline components.
"""

# ==================================================
# Built-in Libraries
# ==================================================

import os
import sys
import pickle

# ==================================================
# Third Party Libraries
# ==================================================

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

# ==================================================
# Project Imports
# ==================================================

from src.exception import CustomException


# ==================================================
# SAVE OBJECT
# ==================================================

def save_object(
    file_path,
    obj
):
    """
    Save Python object as pickle file.

    Examples
    --------
    model.pkl

    preprocessor.pkl

    Parameters
    ----------
    file_path : str

    obj : object
    """

    try:

        # ==================================
        # Extract Folder Path
        # ==================================

        dir_path = os.path.dirname(
            file_path
        )

        # ==================================
        # Create Folder
        # ==================================

        os.makedirs(
            dir_path,
            exist_ok=True
        )

        # ==================================
        # Save Object
        # ==================================

        with open(
            file_path,
            "wb"
        ) as file_obj:

            pickle.dump(
                obj,
                file_obj
            )

    except Exception as e:

        raise CustomException(
            e,
            sys
        )


# ==================================================
# LOAD OBJECT
# ==================================================

def load_object(
    file_path
):
    """
    Load Pickle Object

    Examples
    --------
    model.pkl

    preprocessor.pkl

    Parameters
    ----------
    file_path : str

    Returns
    -------
    Loaded Object
    """

    try:

        with open(
            file_path,
            "rb"
        ) as file_obj:

            return pickle.load(
                file_obj
            )

    except Exception as e:

        raise CustomException(
            e,
            sys
        )


# ==================================================
# EVALUATE MODELS
# ==================================================

def evaluate_models(

    X_train,

    y_train,

    X_test,

    y_test,

    models

):
    """
    Train and evaluate multiple models.

    Parameters
    ----------
    X_train

    y_train

    X_test

    y_test

    models : dict

    Returns
    -------
    report : dict
    """

    try:

        report = {}

        # ==============================
        # Iterate Through Models
        # ==============================

        for model_name, model in models.items():

            # ==========================
            # Train Model
            # ==========================

            model.fit(
                X_train,
                y_train
            )

            # ==========================
            # Prediction
            # ==========================

            y_pred = model.predict(
                X_test
            )

            # ==========================
            # Evaluation Metrics
            # ==========================

            r2 = r2_score(
                y_test,
                y_pred
            )

            mae = mean_absolute_error(
                y_test,
                y_pred
            )

            mse = mean_squared_error(
                y_test,
                y_pred
            )

            rmse = mse ** 0.5

            # ==========================
            # Store Results
            # ==========================

            report[model_name] = {

                "R2 Score": r2,

                "MAE": mae,

                "MSE": mse,

                "RMSE": rmse

            }

        return report

    except Exception as e:

        raise CustomException(
            e,
            sys
        )