# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#Imports
import numpy as np
import pandas as pd


# %%
#Read data in

matches = pd.read_csv("./data/match.csv")
players = pd.read_csv("./data/player.csv")
player_attributes = pd.read_csv("./data/player_attributes.csv")
len(matches)


# %%


mat=matches.drop(columns=matches.columns[11:55])
ma = mat.drop(columns=mat.columns[33:])
ma=ma.drop(columns=ma.columns[1:9])
ma["result"]=ma["home_team_goal"] - ma["away_team_goal"]
ma.loc[ma["result"]>0,"result"] = 1
ma.loc[ma["result"]<0,"result"] = -1
ma.loc[ma["result"]==0,"result"] = 0
ma=ma.dropna()

pa = player_attributes.dropna()
print(len(ma))

for i, sum in enumerate(ma.isna().sum()):
    print(ma.columns[i]+"\t"*4,sum)


# %%
ma.groupby("result")["id"].count()


# %%
#Find average values for each column in pa

averages=dict()
pa = pa.select_dtypes(exclude=['object'])
pa=pa.drop(columns=["player_fifa_api_id","player_api_id"])
for col in pa.columns:
    averages[col]=((pa[col].mean()*100).round())/100

for key in averages.keys():
    print(key + "    ",averages[key])


# %%



# %%


new_df=pd.merge(ma,pa,left_on="home_player_1",right_on="id",how="left").drop(columns=["id_y"])
new_df["id"]=new_df["id_x"]
new_df=new_df.drop(columns=["id_x"])
for col in pa.columns[1:]:
    new_df["home_player_1 "+col]=new_df[col]
    new_df=new_df.drop(columns=[col])

for j in range(2,23):
    s= "home_player_" if j<12 else "away_player_"
    k = j if j<12 else j-11
    new_df=pd.merge(new_df,pa,left_on=(s+str(k)),right_on="id",how="left").drop(columns=["id_y"])
    new_df["id"]=new_df["id_x"]
    new_df=new_df.drop(columns=["id_x"])
    for col in pa.columns[1:]:
        new_df[s+str(k)+" "+col]=new_df[col]
        new_df=new_df.drop(columns=[col])




for i, sum in enumerate(new_df.isna().sum()):
    print(new_df.columns[i]+"\t"*4,sum)


# %%

for col in new_df.columns:
    splitter=col.split(' ')
    if(len(splitter)>1):
        original_name=splitter[1]
        print(averages[original_name])
        new_df[col]=new_df[col].fillna(averages[original_name])


# %%
for i, sum in enumerate(new_df.isna().sum()):
    print(new_df.columns[i]+"\t"*4,sum)


# %%
new_df.to_csv("./data.csv")


# %%



