import json

# Get a list of paths

tree = json.load(open("reduced/paths.json"))

def flatten(tree):
    flat = []
    for t in tree:
        if tree[t] and type(tree[t]) == type({}):
            flat += [[t] + kid for kid in flatten(tree[t])]
        else:
            flat += [[t]] 
    return flat


