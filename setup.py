"""
setup.py

Purpose
-------
Convert project into an installable package.

Benefits
--------
1. Dependency management
2. Easier imports
3. Deployment support
4. CI/CD integration
"""

# =====================================================
# Import Required Libraries
# =====================================================
from setuptools import (setup,find_packages)

# =====================================================
# Function to Read Requirements
# =====================================================

def get_requirements(
    file_path: str
):
    """
    Read requirements.txt and
    return package list.

    Parameters
    ----------
    file_path : str

    Returns
    -------
    list
    """

    requirements = []

    with open(file_path) as file_obj:

        requirements = file_obj.readlines()

        # Remove newline character

        requirements = [

            req.replace(
                "\n",
                ""
            )

            for req in requirements

        ]

        # Remove editable install flag

        if "-e ." in requirements:

            requirements.remove(
                "-e ."
            )

    return requirements


# =====================================================
# Setup Configuration
# =====================================================

setup(

    # Package Name
    name="CarPricePrediction",

    # Package Version
    version="0.0.1",

    # Package Author
    author="Manish",

    # Author Email
    author_email=
    "manishkumar488@gmail.com",

    # Automatically Discover Packages
    packages=find_packages(),

    # Install Dependencies
    install_requires=
    get_requirements(
        "requirements.txt"
    )

)                                                                                                               