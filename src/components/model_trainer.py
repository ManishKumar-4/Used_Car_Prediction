"""
model_trainer.py

Purpose
-------
1. Train multiple regression models
2. Compare model performance
3. Select best model
4. Save best model
5. Return evaluation score
"""

# ==================================================
# Built-in Libraries
# ==================================================

import os
import sys

# ==================================================
# Third Party Libraries
# ==================================================

import numpy as np

from sklearn.linear_model import (
    LinearRegression,
    Ridge,
    Lasso,
    ElasticNet
)

from sklearn.tree import (
    DecisionTreeRegressor
)

from sklearn.ensemble import (

    RandomForestRegressor,

    ExtraTreesRegressor,

    GradientBoostingRegressor,

    AdaBoostRegressor
)

from sklearn.metrics import (
    r2_score
)

# ==================================================
# Project Imports
# ==================================================

from src.logger import logging

from src.exception import CustomException

from src.entity.config_entity import (
    ModelTrainerConfig
)

from src.utils.common import (
    save_object,
    evaluate_models
)


class ModelTrainer:
    """
    Model Training Component

    Responsibilities
    ----------------
    1. Train multiple models
    2. Evaluate all models
    3. Select best model
    4. Save best model
    """

    def __init__(
        self,
        config: ModelTrainerConfig
    ):

        self.config = config

    def initiate_model_trainer(
        self,
        train_array,
        test_array
    ):
        """
        Main training method

        Parameters
        ----------
        train_array : np.array

        test_array : np.array

        Returns
        -------
        r2_score
        """

        try:

            logging.info(
                "Starting Model Training"
            )

            # ======================================
            # Split Features and Target
            # ======================================

            X_train = train_array[:, :-1]

            y_train = train_array[:, -1]

            X_test = test_array[:, :-1]

            y_test = test_array[:, -1]

            logging.info(
                "Train-Test Split Completed"
            )

            # ======================================
            # Define Models
            # ======================================

            models = {

                "Linear Regression":
                LinearRegression(),

                "Ridge":
                Ridge(),

                "Lasso":
                Lasso(),

                "ElasticNet":
                ElasticNet(),

                "Decision Tree":
                DecisionTreeRegressor(),

                "Random Forest":
                RandomForestRegressor(),

                "Extra Trees":
                ExtraTreesRegressor(),

                "Gradient Boosting":
                GradientBoostingRegressor(),

                "AdaBoost":
                AdaBoostRegressor()
            }

            logging.info(
                "Models Initialized"
            )

            # ======================================
            # Evaluate Models
            # ======================================

            model_report = evaluate_models(

                X_train=X_train,

                y_train=y_train,

                X_test=X_test,

                y_test=y_test,

                models=models

            )

            logging.info(
                f"Model Report: {model_report}"
            )

            # ======================================
            # Best Model Selection based on  R2 Score
            # ======================================

            best_model_name= max(
                model_report,key=lambda model:model_report[model]["R2 Score"]
                )

            best_model_score =(
                model_report[best_model_name]["R2 Score"]
            )

            best_model = models[
                best_model_name
            ]

            logging.info(
                f"Best Model: {best_model_name}"
            )

            logging.info(
                f"Best Score: {best_model_score}"
            )

            # ======================================
            # Minimum Performance Check
            # ======================================

            if best_model_score < 0.60:

                raise Exception(
                    "No suitable model found"
                )

            # ======================================
            # Save Best Model
            # ======================================

            save_object(

                file_path=

                self.config
                .trained_model_file_path,

                obj=best_model

            )

            logging.info(
                "Best Model Saved"
            )

            # ======================================
            # Final Prediction
            # ======================================

            predicted = (

                best_model.predict(
                    X_test
                )

            )

            r2_square = r2_score(

                y_test,

                predicted

            )

            logging.info(
                f"Final R2 Score: {r2_square}"
            )

            return r2_square

        except Exception as e:

            raise CustomException(
                e,
                sys
            )