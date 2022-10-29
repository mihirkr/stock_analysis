import sys

import numpy as np
import pandas as pd

pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)
sys.path.append("../")
from stock_analysis.query.data_query import parse_data

TICKER_LIST = [
    "RELIANCE",
    "SBIN",
]
df = pd.DataFrame()
for TICKER in TICKER_LIST:
    stockDict = parse_data(TICKER)
    # stockDict["stock"] = TICKER
    # print(stockDict)
    stock_df = (
        pd.DataFrame(data=stockDict, index=[TICKER])
        .replace("N/A", np.nan)
        .replace("N/A (N/A)", np.nan)
    )
    cols_to_keep = [
        "Previous Close",
        "Open",
        "Day's Range",
        "52 Week Range",
        "Volume",
        "Avg. Volume",
        "Market Cap",
        "Beta (5Y Monthly)",
        "PE Ratio (TTM)",
        "EPS (TTM)",
        "Forward Dividend & Yield",
        "1y Target Est",
    ]
    df = pd.concat([df, stock_df[cols_to_keep]], axis=0)

print(df)
## Todo -- 
# Fix data types
# Plot price - 1y
# identify events - Ex Dividend date, stock split/reverse split, holidays, etc. 
