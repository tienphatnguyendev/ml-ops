import sys
import os
import pandas as pd
import sys
import os
import seaborn as sns

# Define your custom colors
navy = "#000080"  # Navy color hex
yellow = "#FFFF00"  # Yellow color hex

# Create a custom color palette
palette = [navy, yellow]

# Set the palette
sns.set_palette(palette)

sys.path.insert(0, "/Users/aaronnguyen/Documents/PersonalProjects/azure-mlops")
from src.visualization import NumericVisualizer, CategoricalVisualizer


df = pd.read_csv(
    "http://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data",
    header=None,
    names=[
        "StaAcc",
        "DuMon",
        "CredHis",
        "Purpose",
        "CredAmt",
        "SavAcc",
        "PreEmpl",
        "InsRt",
        "PerSta",
        "OthDebtor",
        "PreRe",
        "Property",
        "Age",
        "IntPla",
        "Housing",
        "ExstCredit",
        "Job",
        "NoMain",
        "Phone",
        "ForWorker",
        "Response",
    ],
    index_col=None,
    sep=" ",
)

numeric_cols = df.select_dtypes(include=["int", "float"]).columns
cat_cols = df.select_dtypes(include="O").columns
print(cat_cols)

# Create instances of the visualizers
numeric_visualizer = NumericVisualizer(df)
categorical_visualizer = CategoricalVisualizer(df)

# Plot distributions
# numeric_visualizer.plot_distribution(numeric_cols)
categorical_visualizer.plot_distribution(cat_cols)
