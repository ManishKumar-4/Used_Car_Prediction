"""
exception.py

Purpose
-------
Custom exception handling for the project.

Why?

Instead of showing only:

    division by zero

we can show:

    File Name
    Line Number
    Error Details

This makes debugging easier.
"""

# ==========================================
# Built-in Libraries
# ==========================================

import sys

# sys module provides information
# about exceptions currently being handled.


def error_message_detail(
    error,
    error_detail: sys
):
    """
    Generate detailed error message.

    Parameters
    ----------
    error : Exception

    error_detail : sys

    Returns
    -------
    Detailed Error String
    """

    # ======================================
    # Extract Exception Information
    # ======================================

    _, _, exc_tb = error_detail.exc_info()

    # exc_tb
    #
    # traceback object
    #
    # contains:
    #
    # file name
    # line number
    #

    file_name = exc_tb.tb_frame.f_code.co_filename

    # Example:
    #
    # data_transformation.py

    line_number = exc_tb.tb_lineno

    # Example:
    #
    # 125

    # ======================================
    # Create Error Message
    # ======================================

    error_message = (

        f"Error occurred in python script "
        f"[{file_name}] "

        f"line number [{line_number}] "

        f"error message [{str(error)}]"

    )

    return error_message


class CustomException(Exception):
    """
    Custom Exception Class

    Inherits from Python's
    built-in Exception class.
    """

    def __init__(
        self,
        error_message,
        error_detail: sys
    ):
        """
        Constructor
        """

        super().__init__(
            error_message
        )

        self.error_message = (
            error_message_detail(

                error_message,

                error_detail

            )
        )

    def __str__(self):
        """
        Return formatted error.
        """

        return self.error_message