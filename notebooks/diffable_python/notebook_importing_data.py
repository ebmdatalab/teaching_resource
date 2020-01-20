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

# ### Import libraries and local code
#
# See notebook_importing_code for more info.

import pandas as pd
import os

import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from code.custom_functions import calbmi

# ### Import data and process it 

# #### Path to the correct file 

filename = "weight-height.csv"

path = os.path.dirname(os.getcwd()) + "/data"

filepath = path + "/raw_data/" + filename

filepath

# #### Make dataframe from the csv

df = pd.read_csv(filepath)

df['height_m'] = df['Height'] / 39.37
df['weight_kg'] = df['Weight'] / 2.205

df.head()

df['bmi'] = calbmi(df['height_m'], df['weight_kg'])

df.head()

# #### Path to the output file 

export_filename = 'data.csv'
export_path = path + "/processed_data/" + export_filename

export_path

df.to_csv(export_path, index = None, header=True)


