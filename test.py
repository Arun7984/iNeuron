import pandas as pd
from utils.all_utils import prepare_data

AND = {
    "x1": [0,0,1,1],
    "x2": [0,1,0,1],
    "y": [0,0,0,1],
}

df = pd.DataFrame(AND)
print(df)
print(df.drop("y",axis=1))



