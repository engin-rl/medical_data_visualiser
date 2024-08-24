import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# IMPORTING DATA
df = pd.read_csv("medical_examination.csv")
# print(df.head())

# DETERMINING IF A PERSON IS OVERWEIGHT DEPENDING ON THEIR BMI (IF BMI > 25)
# CALCULATING BMI (WEIGHT IN KGS / SQUARE OF HEIGHT IN METER) AND ASIGNING TO A NEW COLUMN (overweight)
weight_kgs = df["weight"]
height_meter = df["height"] / 100
BMI = weight_kgs / (height_meter**2)
df["overweight"] = (BMI > 25).astype(int)

# NORMALIZING THE DATA AS, 0 IS ALWAYS GOOD AND 1 IS ALWAYS BAD
# FOR cholesterol AND gluc IF THE VALUE 1 THEN ITS 0
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)


def draw_cat_plot():
    # Created a DataFrame for the cat plot
    # with values from cholesterol, gluc, smoke, alco, active, and overweight
    df_cat_melted = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
    )

    df_cat_melted["total"] = df_cat_melted["value"]

    # Grouped and reformatted the data in df_cat_melted to split it by cardio.
    # Showed the counts of each feature.
    df_cat_grouped = (
        df_cat_melted.groupby(["cardio", "variable", "value"])
        .agg({"total": "count"})
        .reset_index()
    )

    chart = sns.catplot(
        df_cat_grouped,
        x="variable",
        y="total",
        hue="value",
        kind="bar",
        col="cardio",
        height=6,
        aspect=1,
    )

    fig = chart.fig
    fig.savefig("catplot.png")
    return fig


def draw_heat_map():
    # Cleaned the data.
    # Filtered out the following patient segments that represent incorrect data:
    # diastolic pressure is higher than systolic (Keept the correct data with (df['ap_lo'] <= df['ap_hi']))
    # height is less than the 2.5th percentile (Keept the correct data with (df['height'] >= df['height'].quantile(0.025)))
    # height is more than the 97.5th percentile
    # weight is less than the 2.5th percentile
    # weight is more than the 97.5th percentile
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # Calculated the correlation matrix and stored it
    corr = df_heat.corr()

    # Generated a mask for the upper triangle and stored it
    mask = np.triu(np.ones_like(corr, dtype=bool))
    fig, ax = plt.subplots(figsize=(16, 9))
    sns.heatmap(corr, mask=mask, square=True, linewidths=0.5, annot=True, fmt="0.1f")
    fig.savefig("heatmap.png")
    plt.show()

    return fig
