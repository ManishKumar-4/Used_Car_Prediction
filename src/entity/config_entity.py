"""
config_entity.py

Purpose
-------
Store configuration objects
for each pipeline component.
"""

from dataclasses import dataclass


# ==========================================
# Data Ingestion Config
# ==========================================

@dataclass
class DataIngestionConfig:

    train_data_path: str

    test_data_path: str

    raw_data_path: str


# ==========================================
# Data Validation Config
# ==========================================

@dataclass
class DataValidationConfig:

    data_path: str

    status_file_path: str

    required_columns: list

    target_column: str


# ==========================================
# Data Transformation Config
# ==========================================

@dataclass
class DataTransformationConfig:

    preprocessor_obj_file_path: str


# ==========================================
# Model Trainer Config
# ==========================================

@dataclass
class ModelTrainerConfig:

    trained_model_file_path: str