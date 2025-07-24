import pandas as pd

df = pd.DataFrame({
    "src": ["key", "key", "key"],
    "snk": ["one", "two", "out"],
    "Δt": [1,4,7]
})

print(df.to_latex())