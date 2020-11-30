import pandas as pd
import numpy as np


matches = pd.read_csv("./data/match.csv")

players = pd.read_csv("./data/player.csv")

#print(matches.groupby("league_id")["id"].count())


for i, sum in enumerate(matches.isna().sum()):
    print(matches.columns[i]+"\t"*4,sum)



