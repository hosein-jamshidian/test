import pandas as pd 
import numpy as np 
import os

api_key = os.getenv('TEST_KEY')

print(api_key)
data= pd.DataFrame({"A":[1,2,3], "B": [10,11,12], "C": [20,21,22]})

print("Done!")
