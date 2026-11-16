import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import pandas as pd
    import numpy as np

    pd.set_option('display.width', None)
    return np, pd


@app.cell
def _(pd):
    revenue_data = pd.DataFrame({
        'country' : pd.Series(['Netherlands', 'Belgium', 'Netherlands', 'Belgium'], dtype = str), 
        'city': pd.Series(['Amsterdam', 'Brussels', 'Utrecht', 'Leuven'], dtype = str), 
        'revenue': pd.Series([12.1, 9.2, 13.1, 8.5], dtype = float)})

    print(revenue_data)
    return (revenue_data,)


@app.cell
def _(revenue_data):
    revenue_data.to_csv('data/revenue_data.csv', index=False)
    return


@app.cell
def _(revenue_data):
    revenue_data.to_parquet('data/revenue_data.parquet', index = False)
    return


@app.cell
def _(pd):
    print(
        pd.read_csv('data/revenue_data.csv', dtype={"country": str, "city": str, "revenue": float})
    )
    return


@app.cell
def _(revenue_data):
    print(
        revenue_data.groupby('country').agg({'revenue': 'sum'}).sort_values(by='revenue', ascending=False).head(10)
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Dataframe anatomy
    """)
    return


@app.cell
def _(revenue_data):
    revenue_data.columns
    return


@app.cell
def _(revenue_data):
    revenue_data.index
    return


@app.cell
def _(revenue_data):
    print(revenue_data['country'])
    return


@app.cell
def _(revenue_data):
    type(revenue_data['country'])
    return


@app.cell
def _(revenue_data):
    print(revenue_data.dtypes)
    return


@app.cell
def _(pd):
    pd.col('country')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Example dtypes
    """)
    return


@app.cell
def _(revenue_data):
    (revenue_data['revenue'] == 0).dtype
    return


@app.cell
def _(pd):
    t = pd.CategoricalDtype(categories=["b", "a"], ordered=True)
    pd.Series(["a", "b", "a", None], dtype=t)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Dataframe operaties
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Transformatie
    """)
    return


@app.cell
def _(pd, revenue_data):
    print(
        revenue_data.assign(revenue_dollars = pd.col('revenue') * 1.1)
    )
    return


@app.cell
def _(pd):
    type(pd.col('country'))
    return


@app.cell
def _(pd, revenue_data):
    print(
        revenue_data.assign(
            country = pd.col('country').replace({'Netherlands': 'NL'}),
            city_is_capital = pd.col('city').map(lambda city: city == 'Amsterdam' or city == 'Brussels'),
            important_branch = (pd.col('revenue') > 10) | pd.col('city_is_capital'),
            revenue_rank = pd.col('revenue').rank(),
        )
    )
    return


@app.cell
def _(pd, revenue_data):
    print(
        revenue_data.assign(
            country = pd.col('country').replace({'Netherlands': 'NL'}),
            city_is_capital = pd.col('city').isin(['Amsterdam', 'Brussels']),
            important_branch = (pd.col('revenue') > 10) | pd.col('city_is_capital'),
            revenue_rank = pd.col('revenue').rank(),
        )
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Selectie
    """)
    return


@app.cell
def _(revenue_data):
    print(
        revenue_data.drop(columns = ['country'])
    )
    return


@app.cell
def _(revenue_data):
    print(
        revenue_data[['city', 'revenue']]
    )
    return


@app.cell
def _(pd, revenue_data):
    print(
        revenue_data.loc[(pd.col('revenue') > 10)]
    )
    return


@app.cell
def _(revenue_data):
    print(
        revenue_data.sample(2, random_state = 42)
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Sorteren
    """)
    return


@app.cell
def _(revenue_data):
    print(
        revenue_data.sort_values(by='revenue', ascending=False)
    )
    return


@app.cell
def _(revenue_data):
    print(
        revenue_data.sort_values(by='revenue', ascending=False).head(2)
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Know your dtypes
    """)
    return


@app.cell
def _(pd):
    print(
        pd.Series(['Netherlands', 'Belgium']).str.contains('i')
    )
    return


@app.cell
def _(pd):
    print(
        pd.Series(['2018-01-01', '2019-01-01'], dtype='datetime64[ns]') 
        - pd.Series(['2018-06-01', '2019-08-01'], dtype='datetime64[ns]')
    )
    return


@app.cell
def _(pd):
    print(
        pd.Series(['2018-01-01', '2019-01-01'], dtype='datetime64[ns]').dt.day_name()
    )
    return


@app.cell
def _(pd):
    print(
        pd.Series(['5','3']) + pd.Series(['2','1'])
    )
    return


@app.cell
def _(pd):
    print(
        pd.Series(['5','3']).astype(int) + pd.Series(['2','1']).astype(int)
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Casting
    """)
    return


@app.cell
def _(pd):
    pd.Series([1,2])
    return


@app.cell
def _(pd):
    pd.Series([1, 2.0])
    return


@app.cell
def _(pd):
    print(pd.Series(['a', 'b']))
    return


@app.cell
def _(pd):
    print(
        pd.Series([1, 'a'])
    )
    return


@app.cell
def _(pd):
    print(
        pd.Series([1,'a'], dtype = str)
    )
    return


@app.cell
def _(pd):
    print(
        pd.Series([1,'a'], dtype = int)
    )
    return


@app.cell
def _(pd):
    pd.Series(['2018-09-31', '2019-01-01'], dtype='datetime64[ns]')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Aggregatie
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell
def _(revenue_data):
    print(revenue_data)
    return


@app.cell
def _(revenue_data):
    revenue_data['revenue'].sum()
    return


@app.cell
def _(revenue_data):
    revenue_data['revenue'].min()
    return


@app.cell
def _(pd, revenue_data):
    revenue_data.loc[pd.col('country') == 'Belgium']['revenue'].sum()
    return


@app.cell
def _(revenue_data):
    print(
        revenue_data['revenue'].describe()
    )
    return


@app.cell
def _(pd):
    print(
        pd.DataFrame(
            {'revenue_year_1': [11.7, 8.3, 13.2, 8.8], 'revenue_year_2': [12.1, 9.2, 13.1, 8.5]}
        ).assign(total_revenue = lambda df: df.sum(axis=1))
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Groupby
    """)
    return


@app.cell
def _(revenue_data):
    print(
        revenue_data
                .groupby('country', as_index = False)
                .agg(   total_revenue=('revenue', 'sum'),
                        max_revenue=('revenue', 'max'), 
                        revenue_spread = ('revenue', lambda revenue: revenue.max() - revenue.min()))
    )
    return


@app.cell
def _(revenue_data):
    print(
        revenue_data
            [['country']]
            .value_counts()
            .reset_index()
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Windowing
    """)
    return


@app.cell
def _(revenue_data):
    print(revenue_data)
    return


@app.cell
def _(revenue_data):
    print(
        revenue_data
            .assign(total_revenue_in_country = lambda df: df.groupby('country')['revenue']
                                                            .transform('sum')
                   )
    )
    return


@app.cell
def _(revenue_data):
    print(
        revenue_data
            .assign(rank_in_country = lambda df: df.groupby('country')['revenue']
            .transform('rank'))
    )
    return


@app.cell
def _(pd, revenue_data):
    print(
        revenue_data
            [['revenue']]
            .sort_values(by = "revenue", ascending = False)
            .assign(cumulative_revenue = pd.col('revenue').cumsum())
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Koppeling
    """)
    return


@app.cell
def _(pd):
    revenue_city_data = pd.DataFrame({'city': ['Amsterdam', 'Brussels', 'Utrecht', 'Leuven'], 'revenue': [12.1, 9.2, 13.1, 8.5]})
    city_data = pd.DataFrame({'country' : ['Netherlands', 'Belgium', 'Netherlands', 'Belgium'], 'city': ['Amsterdam', 'Brussels', 'Utrecht', 'Leuven']})

    print(revenue_city_data, '\n\n', city_data)
    return city_data, revenue_city_data


@app.cell
def _(city_data, pd, revenue_city_data):
    print(
        pd.merge(city_data, revenue_city_data, on='city', how='inner')
    )
    return


@app.cell
def _(revenue_data):
    netherlands_data = revenue_data[revenue_data['country'] == 'Netherlands'].reset_index(drop = True)
    belgium_data = revenue_data[revenue_data['country'] == 'Belgium'].reset_index(drop = True)
    print(netherlands_data, '\n\n', belgium_data)
    return belgium_data, netherlands_data


@app.cell
def _(belgium_data, netherlands_data, pd):
    print(
        pd.concat([netherlands_data, belgium_data])
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Reshaping
    """)
    return


@app.cell
def _(pd):
    yearly_data = pd.DataFrame({'country' : ['Netherlands', 'Belgium'], 'year': [['2024', '2025'], ['2024', '2025']], 'revenue': [[12.1, 13.1], [9.2, 8.5]]})
    print(yearly_data)
    return (yearly_data,)


@app.cell
def _(yearly_data):
    print(
        yearly_data.explode(['year', 'revenue'])
    )
    return


@app.cell
def _(yearly_data):
    pivoted_data = (yearly_data.explode(['year', 'revenue'])
                    .pivot(index = ['country'], columns=['year'], values='revenue')
                    .reset_index()
                    #.rename_axis(None, axis=1)
                   )

    pivoted_data
    return (pivoted_data,)


@app.cell
def _(pivoted_data):
    print(
        pivoted_data.melt(id_vars='country', var_name='year', value_name='revenue')
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Know your dtypes III: Nulls en NaNs
    """)
    return


@app.cell
def _(np, pd):
    s = pd.Series([1., 2., np.nan], dtype= np.float64) 
    print(s)
    return (s,)


@app.cell
def _(np, pd):
    (pd.NA == pd.NA,
    None == None,
    np.nan == np.nan)
    return


@app.cell
def _(s):
    print(
        s.isna()
    )
    return


@app.cell
def _(s):
    print(
        s.fillna(0.0)
    )
    return


@app.cell
def _(pd):
    pd.Series([True, False, None], dtype=bool)
    return


@app.cell
def _(pd):
    pd.Series([True, False, None], dtype=pd.BooleanDtype())
    return


@app.cell
def _(pd):
    revenue_data_na = pd.DataFrame({
        'country' : pd.Series(['Netherlands', pd.NA, 'Netherlands', 'Belgium'], dtype = pd.StringDtype()), 
        'city': pd.Series(['Amsterdam', 'Brussels', pd.NA, 'Leuven'], dtype = str ), 
        'revenue': pd.Series([12.1, 9.2, 13.1, 8.5], dtype = float)
    })

    print(revenue_data_na)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    yay or nay
    """)
    return


@app.cell
def _(revenue_data):
    df = revenue_data
    return (df,)


@app.cell
def _(df):
    total_revenue_nl = 0
    for row in df.itertuples():
        if row.country == 'NL':
            total_revenue += row['revenue']
    return


@app.cell
def _(df, pd):
    df.loc[
    pd.col('country') == 'NL', 'revenue'
    ].sum()
    return


@app.cell
def _(df, pd):
    df.assign(country_has_i 
    = pd.col('country').map(lambda country: 'i' in country))
    return


@app.cell
def _(df, pd):
    df.assign(country_has_i = pd.col('country').str.contains('i'))
    return


@app.cell
def _(df):
    df['large_revenue'] = df['revenue'] > 10
    df['city_is_important'] = df['large_revenue'] | (df['city'] == 'Amsterdam')
    df.groupby('country', as_index = False).agg(frac_important_cities = ('city_is_important', 'mean'))
    return


@app.cell
def _(revenue_data):
    # n.b.: Make sure to also run this cell after the above or it will mess up the marimo dependency logic ...

    revenue_data.drop(columns = ['large_revenue','city_is_important'], inplace=True)
    return


@app.cell
def _(df, pd):
    (df
        .assign(
            large_revenue= pd.col('revenue') > 10,
            city_is_important = pd.col('large_revenue') | (pd.col('city') == 'Amsterdam')
        )
        .groupby('country', as_index = False)
        .agg(frac_important_cities = ('city_is_important', 'mean'))
    )
    return


@app.cell
def _(df):
    df.assign(large_revenue= df['revenue'] > 10)
    return


@app.cell
def _(df, pd):
    df.assign(large_revenue= pd.col('revenue') > 10)
    return


@app.cell
def _(df, revenue_data):
    df_1 = df.drop(columns = ['revenue'])
    df_2 = revenue_data
    return df_1, df_2


@app.cell
def _(df_1, df_2):
    df_1.assign(
        large_revenue = df_2['revenue'] > 10
    )
    return


@app.cell
def _(df_1, df_2, pd):
    pd.merge(df_1, df_2, on = 'city').assign(large_revenue= pd.col('revenue') > 10)
    return


@app.cell
def _(pd):
    pd.DataFrame({
        'country' : ['Netherlands', 'MISSING'], 
        'date' : ['2026-01-01', '2018-02-29']
    })
    return


@app.cell
def _(pd):
    pd.DataFrame({
        'country': pd.Series(['Netherlands', pd.NA], dtype = str), 
        'date': pd.Series(['2026-01-01', '2018-02-28'], dtype = 'datetime64[ns]')
    })
    return


if __name__ == "__main__":
    app.run()
