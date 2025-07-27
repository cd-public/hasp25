import os  # import os module
import pandas as pd

directory = 'dfs'  # set directory path

for entry in os.scandir(directory):  
    if entry.is_file():  
        # retrive df
        df = pd.read_pickle(entry)
        name = entry.path.split(".")[0].split("/")[1]
        # extract IFT
        df = df.loc[df.index.str.startswith("shadow_")]
        # drop unreached regs
        df = df.loc[(df!=0).any(axis=1)]
        # get and order the time-of-flow tuples
        tt = df.idxmax(axis=1)
        tt = tt.apply(lambda s : int(s[1:]))
        # format
        tt.index = tt.index.str.replace('shadow_','')
        tt = tt.sort_values()
        # pop the root source signal
        tt = tt[tt!=0]
        # save
        tt.to_pickle("sparse/" + name + ".pickle")
