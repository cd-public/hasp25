import os  # import os module
import pandas as pd

directory = 'sparse'  # set directory path

# We'll track all signal names, the atomic flows, and other flows

signal = []
atomic = {}
others = {}

# Transpose the series into dictionary entries

for entry in os.scandir(directory):  
    if entry.is_file():  
        # get name of root source signal from filename
        name = entry.path.split(".")[0].split("/")[1]
        signal.append(name)
        # retrive times-of-flow tuples
        tt = pd.read_pickle(entry)
        # remove shadow_ prefix
        tt.index = tt.index.str.replace('shadow_','')
        # pop the root source signal
        # ... which somehow isn't always present?
        if name in tt.index:
            tt.pop(name)
        if not tt.empty:
            # differentiate atomics from others
            # ... wish I had operator in base language!
            atomic[name] = tt[tt == min(tt)].index.tolist()
            others[name] = tt[tt != min(tt)].index.tolist()

# Actually just gonna build the graph in df to avoid learning how pickle works.
# We'll use a NumPy array then add labels
import numpy as np

# "Signed integer type, compatible with C char"
# ... 0 = no edge
# ... 1 = yes edge
# ... -1 = maybe edge?

graph = np.zeros((len(signal),len(signal)),dtype=np.byte)

# Add atomics
for rss in atomic:
    x = signal.index(rss)
    sinks = atomic[rss]
    for sink in sinks:
        graph[signal.index(sink)][x] = 1

# Add candidates
for rss in others:
    x = signal.index(rss)
    sinks = others[rss]
    for sink in sinks:
        graph[signal.index(sink)][x] = -1

# Candidate promotion
for sink in graph:
    # no known edges...
    if np.count_nonzero(sink == 1) == 0:
        # at most one candidate
        if np.count_nonzero(sink == -1) == 1:
            sink[np.where(sink == -1)] = 1

df = pd.DataFrame(graph)
df.columns = signal
df.index = signal
df.to_pickle("reduced/path.pickle")