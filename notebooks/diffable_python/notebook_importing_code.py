# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# First import libraries 

import pandas as pd

# Then import local code. You require an empty \_\_init\_\_.py to be able to import the write functions. You can either path to the right file and import the functions: 

from code.custom_functions import multiplier

# or path to the folder and import the entire contents of a file.

from code import custom_functions


