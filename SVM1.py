import pandas as pd
import os
from Quandl import Quandl
import time

auth_tok = "yourauthhere"

data = Quandl.get("WIKI/KO", trim_start = "2000-12-12", trim_end = "2014-12-30", authtoken=auth_tok)

print(data)
