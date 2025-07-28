import os  # import os module
import pandas as pd
import json

directory = 'sparse'  # set directory path

graph = pd.read_pickle("reduced/graph.pickle")
paths = {}

def kids(src, rest):
    if not rest or type(rest[0]) == type(""):
        return [sink for sink in rest if graph[src][sink]]
    return {sink:kids(sink, rest[i+1:]) for i in range(len(rest)) for sink in rest[i] if graph[src][sink] == 1 } 

for entry in os.scandir(directory):  
    if entry.is_file():  
        # get times of flow 
        tt = pd.read_pickle(entry)
        name = entry.path.split(".")[0].split("/")[1]
        # series into dag
        dag = [list(item.index) for key, item in tt.groupby(tt)]
        # into a tree (n-dim dict)
        if len(dag):
            tree = kids(name,dag)
            if tree:
                paths[name] = tree

open("reduced/paths.json","w").write(json.dumps(paths))
