import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from scipy import stats
    from matplotlib.ticker import MaxNLocator

    return MaxNLocator, np, pd, plt, sns


@app.cell
def _(sns):
    sns.set_theme(style="darkgrid") 
    return


@app.cell
def _(MaxNLocator, np, pd, plt):
    def _():

        uber_df = pd.read_parquet("./data/uber_dataset_2025-01.parquet")
        rng = np.random.default_rng(seed = 42)
        df_sample = uber_df.sample(1000, random_state = rng) 

        fig, ax = plt.subplots()

        ax.hist(df_sample['trip_miles'], bins=60, range=(0, 20))

        ax.set_title('Verdeling van lengte rit', fontsize=14)
        ax.set_xlabel('Lengte rit (in miles)', fontsize=12)
        ax.set_ylabel('Aantal ritten', fontsize=12)

        # Force integer ticks on the x-axis
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        plt.show()

    _()
    return


if __name__ == "__main__":
    app.run()
