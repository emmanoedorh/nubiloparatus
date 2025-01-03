import os
from typing import TypedDict

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(os.getcwd()), '.env'))

class KeyValueDict(TypedDict):
    """
    A dictionary with key-value pairs.
    """
    key: str
    value: str