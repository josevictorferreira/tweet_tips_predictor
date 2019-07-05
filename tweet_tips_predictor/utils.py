""" Helper module with some helper functions to use across the project. """

import os
from dotenv import load_dotenv

load_dotenv()

def get_env(value):
    """ Return a environment variable value defined in the .env file
    or the system env.
    """
    return os.getenv(value)

def dataset_path(filename):
    """ Returns the full path for the dataset file. """
    basepath = os.path.dirname(__file__)
    filepath = os.path.abspath(
        os.path.join(basepath, "..", "datasets", filename))
    return filepath
