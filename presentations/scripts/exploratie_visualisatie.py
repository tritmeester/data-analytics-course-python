import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from great_tables import GT, html
    from great_tables.data import sza
    import polars as pl
    import polars.selectors as cs
    import matplotlib.colors as mcolors
    import pandas as pd
    import numpy as np

    from matplotlib.ticker import ScalarFormatter

    from scipy.stats import truncnorm, norm

    from matplotlib.collections import PatchCollection



    return GT, html, mo, np, pd, pl, sza, truncnorm


@app.cell
def _():
    import matplotlib.pyplot as plt

    return (plt,)


@app.cell
def _():
    import seaborn as sns
    sns.set_theme(style="darkgrid") 
    return (sns,)


@app.cell
def _(GT, html, pl, sza):


    sza_pivot = (
        pl.from_pandas(sza)
        .filter((pl.col("latitude") == "20") & (pl.col("tst") <= "1200"))
        .select(pl.col("*").exclude("latitude"))
        .drop_nulls()
        .pivot(values="sza", index="month", on="tst", sort_columns=True)
    )

    (
        GT(sza_pivot, rowname_col="month")
        .data_color(
            domain=[90, 0],
            palette=["rebeccapurple", "white", "orange"],
            na_color="white",
        )
        .tab_header(
            title="Solar Zenith Angles from 05:30 to 12:00",
            subtitle=html("Average monthly values at latitude of 20&deg;N."),
        )
        .sub_missing(missing_text="")
    )
    return (sza_pivot,)


@app.cell
def _(GT, html, sza_pivot):
    (
        GT(sza_pivot, rowname_col="month")
        .tab_header(
            title="Solar Zenith Angles from 05:30 to 12:00",
            subtitle=html("Average monthly values at latitude of 20&deg;N."),
        )
        .sub_missing(missing_text="")
    )
    return


@app.cell
def _(np, pd, truncnorm):
    # Generate some 'random' data to illustrate plotting

    random_state =  np.random.RandomState(seed = 42)

    revenue = np.array(list(30 + 15*truncnorm.rvs(-1.4, 100, size = 700, random_state = random_state)) + list(70 + 5*truncnorm.rvs(-1.5, 100, size = 200, random_state =random_state)))

    population = revenue*(1 + 0.8*truncnorm.rvs(-1,1, size = len(revenue), random_state = random_state))

    revenue_competitor = 0.5*population*(population/revenue - 0.2) + 5*truncnorm.rvs(-1, 1, size = len(revenue), random_state = random_state)

    revenue_competitor = 3*np.round((1/3)*revenue_competitor, decimals = 0)

    revenue_data = pd.DataFrame({'revenue': revenue, 'population': population, 'revenue_competitor': revenue_competitor})
    return (revenue_data,)


@app.cell
def _(revenue_data):
    revenue_data
    return


@app.cell
def _(revenue_data):
    print(revenue_data['revenue'].describe())
    return


@app.cell
def _(plt, revenue_data):
    fig, ax = plt.subplots()

    ax.hist(revenue_data['revenue'], bins=30, range=(0, 90))

    # 4. Opmaak
    ax.set_title('Verdeling van omzet', fontsize=14)
    ax.set_xlabel('Omzet (in miljoenen €)', fontsize=12)
    ax.set_ylabel('Aantal bedrijven', fontsize=12)

    # Optioneel: Integer ticks forceren op de x-as
    from matplotlib.ticker import MaxNLocator
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    plt.show()
    return


@app.cell
def _(pd):
    import json

    movies_df_raw = pd.read_csv('./data/movies.csv')
    movies_df = movies_df_raw.assign(
                                        release_date = pd.col('release_date').astype('datetime64[ns]'),
                                         genres = pd.col('genres').map(lambda s: json.loads(s.replace("'", '"')))
    )
    return (movies_df,)


@app.cell
def _(movies_df, pd):
    filtered_df = movies_df[
        (movies_df['release_date'] >= '2000-01-01') & 
        (movies_df['release_date'] <= '2016-12-31')
    ]

    yearly_avg = filtered_df.groupby(pd.Grouper(key='release_date', freq='YE'))['runtime'].mean().reset_index()

    filtered_movies_df = movies_df.explode("genres").loc[pd.col('genres').isin(['Action', 'Comedy', 'Drama'])]
    return (filtered_movies_df,)


@app.cell
def _(filtered_movies_df):
    filtered_movies_df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    Matplotlib basics
    """)
    return


@app.cell(hide_code=True)
def _():
    # import matplotlib.pyplot as plt
    return


@app.cell
def _(plt):
    def _():
        fig, ax = plt.subplots()
        ax.scatter([1,2,3], [15.0, 20.0, 5.0])
        plt.show()
    _()
    return


@app.cell
def _(plt):
    def _():
        fig, ax = plt.subplots()
        ax.plot([1,2,3], [15.0, 20.0, 5.0])
        plt.show()
    _()
    return


@app.cell
def _(plt):
    def _():
        fig, ax = plt.subplots()
        ax.plot([1,2,3], [15.0, 20.0, 5.0])
        ax.scatter([1,2,3], [15.0, 20.0, 5.0])
        plt.show()
    _()
    return


@app.cell
def _(plt):
    def _():
        fig, ax = plt.subplots()

        ax.plot([1,2,3], [15.0, 20.0, 5.0])
        ax.scatter([1,2,3], [15.0, 20.0, 5.0])

        ax.set_ylim(bottom = 0)
        ax.set_xlabel('Input (V)')
        ax.set_ylabel('Output (Hz)')
        ax.set_title('Input voltage vs output frequency')
        plt.show()
    _()
    return


@app.cell
def _(plt):
    def _():
        fig, ax = plt.subplots()

        ax.plot([1,2,3], [15.0, 20.0, 5.0])
        ax.scatter([1,2,3], [15.0, 20.0, 5.0])

        ax.plot([1,2,3], [13.0, 18.0, 7.0])
        ax.scatter([1,2,3], [13.0, 18.0, 7.0])

        ax.set_xlabel('Input (V)')
        ax.set_ylabel('Output (Hz)')
        ax.set_title('Input voltage vs output frequency')
        plt.show()
    _()
    return


@app.cell
def _(plt):
    def _():
        fig, ax = plt.subplots()

        ax.plot([1,2,3], [15.0, 20.0, 5.0] , label = "Experiment 1")
        ax.scatter([1,2,3], [15.0, 20.0, 5.0]
                   )

        ax.plot([1,2,3], [13.0, 18.0, 7.0])
        ax.scatter([1,2,3], [13.0, 18.0, 7.0]
                   , label = "Experiment 2")

        ax.set_ylim(bottom = 0)
        ax.set_xlabel('Input (V)')
        ax.set_ylabel('Output (Hz)')
        ax.set_title('Input voltage vs output frequency')
        ax.legend()
        plt.show()
    _()
    return


@app.cell
def _(plt):
    def _():
        fig, ax = plt.subplots()

        ax.plot([1,2,3], [15.0, 20.0, 5.0], linestyle = '--')
        ax.scatter([1,2,3], [15.0, 20.0, 5.0], marker = 'x'
                   , label = "Experiment 1")

        ax.plot([1,2,3], [13.0, 18.0, 7.0], color = 'red')
        ax.scatter([1,2,3], [13.0, 18.0, 7.0], color = 'red'
                   , label = "Experiment 2")

        ax.set_ylim(bottom = 0)
        ax.set_xlabel('Input (V)')
        ax.set_ylabel('Output (Hz)')
        ax.set_title('Input voltage vs output frequency')
        ax.legend()
        plt.show()
    _()
    return


@app.cell
def _(plt):
    def _():
        from matplotlib.ticker import ScalarFormatter
        fig, ax = plt.subplots()

        ax.plot([1,2,3], [15.0, 20.0, 5.0], linestyle = '--')
        ax.scatter([1,2,3], [15.0, 20.0, 5.0], marker = 'x'
                   , label = "Experiment 1")

        ax.plot([1,2,3], [13.0, 18.0, 7.0], color = 'red')
        ax.scatter([1,2,3], [13.0, 18.0, 7.0], color = 'red'
                   , label = "Experiment 2")

        ax.set_ylim(bottom = 0)
        ax.set_xlabel('Input (V)')
        ax.set_ylabel('Output (Hz)')
        ax.set_title('Input voltage vs output frequency')

        tick_formatter = ScalarFormatter(useMathText=True)
        tick_formatter.set_scientific(True)
        tick_formatter.set_powerlimits((0, 0)) 

        ax.yaxis.set_major_formatter(tick_formatter)

        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

        ax.legend()
        plt.show()
    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Seaborn basics
    """)
    return


@app.cell
def _(sns):
    penguin_df = sns.load_dataset("penguins")

    penguin_df
    return (penguin_df,)


@app.cell
def _(penguin_df, plt, sns):
    def _():

        sns.scatterplot(
        data=penguin_df, 
            x="flipper_length_mm", 
            y="bill_length_mm", 
            hue="species", 
        )
        plt.show()
    _()
    return


@app.cell
def _(penguin_df, plt, sns):
    def _():

        ax = sns.scatterplot(
        data=penguin_df, 
            x="flipper_length_mm", 
            y="bill_length_mm", 
            hue="species", 
        )

        ax.set_xlabel('Flipper lengte (mm)')
        ax.set_ylabel('Snavel lengte lengte (mm)')

        plt.show()
    _()
    return


@app.cell
def _(penguin_df, plt, sns):
    def _():

        fig, ax = plt.subplots()

        sns.scatterplot(
        data=penguin_df, 
            x="flipper_length_mm", 
            y="bill_length_mm", 
            hue="species", 
            ax = ax
        )

        ax.set_xlabel('Flipper lengte (mm)')
        ax.set_ylabel('Snavel lengte lengte (mm)')

        plt.show()
    _()
    return


@app.cell
def _(penguin_df, plt, sns):
    def _():

        graph = sns.relplot(
        data=penguin_df, 
            x="flipper_length_mm", 
            y="bill_length_mm", 
            hue="species", 
        )

        graph.ax.set_xlabel('Flipper lengte (mm)')
        graph.ax.set_ylabel('Snavel lengte lengte (mm)')

        plt.show()
    _()
    return


@app.cell
def _(penguin_df, sns):
    sns.heatmap(penguin_df.corr(numeric_only = True), annot=True,  cmap="flare_r")
    return


@app.cell
def _(penguin_df, sns):
    sns.jointplot(data=penguin_df, x="flipper_length_mm", y="bill_length_mm", hue="species")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Altair
    """)
    return


@app.cell
def _():
    import altair as alt

    return (alt,)


@app.cell
def _(alt, filtered_movies_df, np, pd):
    def _():
        movies_in_timeframe = filtered_movies_df.loc[(pd.col('release_date') >= pd.Timestamp('2015-01-02')) &  (pd.col('release_date') <= pd.Timestamp('2015-12-30'))].assign(gaussian_jitter = lambda df: np.random.normal(0, 0.1, size=len(df)))

        chart = (
        alt.Chart(movies_in_timeframe)
        .mark_circle(size=8, clip = True)
        .encode(
            y=alt.Y("genres"),
            x=alt.X("runtime", scale=alt.Scale(domain=[0, 210])),
            yOffset="gaussian_jitter",
        )
        )

        chart.save('altair_chart.svg')

    _()
    return


@app.cell
def _(alt, filtered_movies_df, np, pd):
    def _():
        movies_in_timeframe = filtered_movies_df.loc[(pd.col('release_date') >= pd.Timestamp('2015-01-02')) &  (pd.col('release_date') <= pd.Timestamp('2015-12-30'))].assign(gaussian_jitter = lambda df: np.random.normal(0, 0.1, size=len(df)))

        chart = (
        alt.Chart(movies_in_timeframe)
        .mark_circle(size=8, clip = True)
        .encode(
            y=alt.Y("genres"),
            x=alt.X("runtime", scale=alt.Scale(domain=[0, 210])),
            yOffset="gaussian_jitter",
            color=alt.Color("vote_average", scale=alt.Scale(scheme="viridis")),
        )
        )

        chart.save('altair_chart.svg')

    _()
    return


@app.cell
def _(alt, filtered_movies_df, np, pd):
    def _():
        movies_in_timeframe = filtered_movies_df.loc[(pd.col('release_date') >= pd.Timestamp('2015-01-02')) &  (pd.col('release_date') <= pd.Timestamp('2015-12-30'))].assign(gaussian_jitter = lambda df: np.random.normal(0, 0.1, size=len(df)))

        chart = (
        alt.Chart(movies_in_timeframe)
        .mark_circle(size=20)
        .encode(
            y=alt.Y("genres"),
            x=alt.X("runtime", aggregate = 'mean', scale=alt.Scale(domain=[0, 210])),
        )
        )




        chart.save('altair_chart_agg.svg')

    _()
    return


@app.cell
def _(alt, filtered_movies_df, np, pd):
    def _():
        movies_in_timeframe = filtered_movies_df.loc[(pd.col('release_date') >= pd.Timestamp('2015-01-02')) &  (pd.col('release_date') <= pd.Timestamp('2015-12-30'))].assign(gaussian_jitter = lambda df: np.random.normal(0, 0.1, size=len(df)))

        chart = (
        alt.Chart(movies_in_timeframe)
        .mark_bar()
        .encode(
            y=alt.Y("genres"),
            x=alt.X("runtime", aggregate = 'mean', scale=alt.Scale(domain=[0, 210])),
        )
        )



        chart.save('altair_chart_agg_bar.svg')

    _()
    return


if __name__ == "__main__":
    app.run()
