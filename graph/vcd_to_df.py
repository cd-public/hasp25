from vcd2df import vcd2df
import os  # import os module
import pandas as pd


directory = 'vcds'  # set directory path

for entry in os.scandir(directory):  
    if entry.is_file():  # check if it's a file
        vcd2df(entry).to_pickle("dfs/" + entry.path.split(".")[0].split("/")[1] + ".pickle")
