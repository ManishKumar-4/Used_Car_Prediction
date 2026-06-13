"""
logger.py

Purpose
-------
This file configures project logging.

Why logging?

1. Track execution flow
2. Debug issues
3. Monitor pipeline
4. Store logs permanently

Instead of using print(),
we use logging.
"""

# ==========================================
# Built-in Libraries
# ==========================================

import os
import logging

from datetime import datetime

# ==========================================
# Create Unique Log File Name
# ==========================================

# Example:
#
# 06_09_2026_08_30_15.log
#

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# ==========================================
# Create Logs Directory
# ==========================================

logs_path = os.path.join(

    os.getcwd(),

    "logs"

)

os.makedirs(

    logs_path,

    exist_ok=True

)

# ==========================================
# Full Log File Path
# ==========================================

LOG_FILE_PATH = os.path.join(

    logs_path,

    LOG_FILE

)

# ==========================================
# Configure Logging
# ==========================================

logging.basicConfig(

    # Log file destination
    filename=LOG_FILE_PATH,

    # Log message format
    format=
    "[ %(asctime)s ] "
    "%(lineno)d "
    "%(name)s - "
    "%(levelname)s - "
    "%(message)s",

    # Capture INFO and above
    level=logging.INFO

)

# ==========================================
# Example
# ==========================================

logging.info(
    "Logger Initialized Successfully"
)