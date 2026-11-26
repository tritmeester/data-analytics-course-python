import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    import math

    from sklearn.linear_model import LinearRegression, QuantileRegressor, LogisticRegression, LogisticRegressionCV
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

    sns.set_theme(style="darkgrid")
    return (
        LinearRegression,
        QuantileRegressor,
        RandomForestRegressor,
        np,
        pd,
        plt,
    )


@app.cell
def _(pd):
    uber_df_2025 = pd.read_csv('data/uber_2025.csv')
    return (uber_df_2025,)


@app.cell
def _(plt, uber_df_2025):
    def _():
        fig, ax = plt.subplots()


        ax.scatter(
            uber_df_2025['trip_miles'], 
            uber_df_2025['base_passenger_fare'], 
            alpha=0.3,           
            s=20         
        )


        ax.set_xlim(0, 15)
        ax.set_ylim(0,80)


        ax.set_xlabel('trip miles', fontsize=12)
        ax.set_ylabel('base passenger fare', fontsize=12)

        plt.show()

    _()
    return


@app.cell
def _(LinearRegression, plt, uber_df_2025):
    def _():

        model = LinearRegression()

        model.fit(uber_df_2025[['trip_miles']], uber_df_2025[['base_passenger_fare']])

        print(f"a={model.coef_}, b={model.intercept_}")

        uber_df_with_predictions = uber_df_2025.assign(model_prediction = lambda df: model.predict(df[['trip_miles']])).sort_values("trip_miles")


        fig, ax = plt.subplots()

        ax.scatter(
            uber_df_2025['trip_miles'], 
            uber_df_2025['base_passenger_fare'], 
            alpha=0.3,          
            s=20             
        )

        ax.plot(
            uber_df_with_predictions['trip_miles'],
            uber_df_with_predictions['model_prediction'],
            'r',
            alpha = 0.5
        )

        ax.set_xlim(0, 15)
        ax.set_ylim(0,80)

        ax.set_xlabel('trip miles', fontsize=12)
        ax.set_ylabel('base passenger fare', fontsize=12)

        plt.show()

    _()
    return


@app.cell
def _(QuantileRegressor, plt, uber_df_2025):
    def _():

        model =QuantileRegressor()
        model.fit(uber_df_2025[['trip_miles']], uber_df_2025[['base_passenger_fare']])

        print(f"a={model.coef_}, b={model.intercept_}")

        uber_df_with_predictions = uber_df_2025.assign(model_prediction = lambda df: model.predict(df[['trip_miles']])).sort_values("trip_miles")


        fig, ax = plt.subplots()

        ax.scatter(
            uber_df_2025['trip_miles'], 
            uber_df_2025['base_passenger_fare'], 
            alpha=0.3,          
            s=20             
        )

        ax.plot(
            uber_df_with_predictions['trip_miles'],
            uber_df_with_predictions['model_prediction'],
            'r',
            alpha = 0.5
        )

        ax.set_xlim(0, 15)
        ax.set_ylim(0,80)

        ax.set_xlabel('trip miles', fontsize=12)
        ax.set_ylabel('base passenger fare', fontsize=12)

        plt.show()

    _()
    return


@app.cell
def _(RandomForestRegressor, plt, uber_df_2025):
    def _():

        model =RandomForestRegressor()
        model.fit(uber_df_2025[['trip_miles']], uber_df_2025[['base_passenger_fare']])

        uber_df_with_predictions = uber_df_2025.assign(model_prediction = lambda df: model.predict(df[['trip_miles']])).sort_values("trip_miles")


        fig, ax = plt.subplots()

        ax.scatter(
            uber_df_2025['trip_miles'], 
            uber_df_2025['base_passenger_fare'], 
            alpha=0.3,          
            s=20             
        )

        ax.plot(
            uber_df_with_predictions['trip_miles'],
            uber_df_with_predictions['model_prediction'],
            'r',
            alpha = 0.5
        )

        ax.set_xlim(0, 15)
        ax.set_ylim(0,80)

        ax.set_xlabel('trip miles', fontsize=12)
        ax.set_ylabel('base passenger fare', fontsize=12)

        plt.show()

    _()
    return


@app.cell
def _(pd):
    uber_X_2026 = pd.read_csv('data/uber_X_2026.csv')
    uber_Y_2026 =  pd.read_csv('data/uber_Y_2026.csv')
    return uber_X_2026, uber_Y_2026


@app.cell
def _(uber_X_2026, uber_Y_2026):
    uber_df_2026 = uber_X_2026.merge(uber_Y_2026, on = 'ride_id')
    return (uber_df_2026,)


@app.cell
def _(LinearRegression, uber_df_2025, uber_df_2026):
    def _():

        model = LinearRegression()


        model.fit(uber_df_2025[['trip_miles']], uber_df_2025[['base_passenger_fare']])

        predictions = model.predict(uber_df_2026[['trip_miles']])

        print(predictions)


    _()
    return


@app.cell
def _():
    from sklearn.metrics import r2_score

    return (r2_score,)


@app.cell
def _(LinearRegression, r2_score, uber_df_2025, uber_df_2026):
    def _():

        model = LinearRegression()


        model.fit(uber_df_2025[['trip_miles']], uber_df_2025[['base_passenger_fare']])

        predictions = model.predict(uber_df_2026[['trip_miles']])

        outcome = uber_df_2026['base_passenger_fare']

        print(r2_score(outcome, predictions))

    _()
    return


@app.cell
def _():
    from sklearn.impute import SimpleImputer

    return (SimpleImputer,)


@app.cell
def _(np, pd):
    def _():
        train_X = pd.DataFrame(data = {
                                    'feature_1': [1, 2], 
                                    'feature_2': [np.nan, 3]
        })

        test_X =  pd.DataFrame(data = {
                                        'feature_1': [np.nan, 2], 
                                        'feature_2':  [6, np.nan],
            })
    
        print(f"Train_X: \n\n{train_X}\n")
    
        print(f"Test_X: \n\n{test_X}")

    _()
    return


@app.cell
def _(SimpleImputer, np, pd):
    def _():

        train_X = pd.DataFrame(data = {
                                    'feature_1': [1, 2], 
                                    'feature_2': [np.nan, 3]
        })

        test_X =  pd.DataFrame(data = {
                                        'feature_1': [np.nan, 2], 
                                        'feature_2':  [6, np.nan],
        })


        imputer = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value = 0).set_output(transform="pandas")

        imputer.fit(train_X)

        print(imputer.transform(test_X))

    _()
    return


@app.cell
def _():
    from sklearn.preprocessing import OneHotEncoder, TargetEncoder, OrdinalEncoder

    return OneHotEncoder, OrdinalEncoder, TargetEncoder


@app.cell
def _(OneHotEncoder, pd):
    def _():

        train_X = pd.DataFrame(data = {
                                    'feature_1': ['Blue', 'Blue', 'Green', 'Red'], 
        })

        test_X =  pd.DataFrame(data = {
                                        'feature_1': ['Blue', 'Green'], 
        })

        print(f"Train_X: \n\n{train_X}\n")
    
        print(f"Test_X: \n\n{test_X}\n\n")


        encoder = OneHotEncoder(sparse_output=False).set_output(transform="pandas")

        encoder.fit(train_X)

        print(encoder.transform(test_X))

    _()
    return


@app.cell
def _(OrdinalEncoder, pd):
    def _():

        train_X = pd.DataFrame(data = {
                                    'feature_1': ['Blue', 'Blue', 'Green', 'Red'], 
        })

        test_X =  pd.DataFrame(data = {
                                        'feature_1': ['Blue', 'Green'], 
        })

        print(f"Train_X: \n\n{train_X}\n")
    
        print(f"Test_X: \n\n{test_X}\n\n")


        encoder = OrdinalEncoder(
                                categories=[['Blue', 'Red', 'Green']]
                               ).set_output(transform="pandas")

        encoder.fit(train_X)

        print(encoder.transform(test_X))

    _()
    
    return


@app.cell
def _(TargetEncoder, pd):
    def _():

        train_X = pd.DataFrame(data = {
                                    'feature_1': ['Blue', 'Blue', 'Green', 'Red'], 
        })

        train_y = pd.DataFrame(data = {'y': [1.0, 2.0, 5.8, 0.3]})

        test_X =  pd.DataFrame(data = {
                                        'feature_1': ['Blue', 'Green'], 
        })

        print(f"Train_X: \n\n{train_X}\n")

        print(f"Train_y: \n\n{train_y}\n")
    
        print(f"Test_X: \n\n{test_X}\n\n")


        encoder = TargetEncoder(smooth = 0).set_output(transform="pandas")

        encoder.fit(train_X, train_y)

        print(encoder.transform(test_X))

    _()
    
    return


@app.cell
def _(TargetEncoder, pd):
    def _():

        train_X = pd.DataFrame(data = {
                                    'feature_1': ['Blue', 'Blue', 'Green', 'Red'], 
        })

        train_y = pd.DataFrame(data = {'y': [1.0, 2.0, 5.8, 0.3]})

        test_X =  pd.DataFrame(data = {
                                        'feature_1': ['Blue', 'Green'], 
        })

        print(f"Train_X: \n\n{train_X}\n")

        print(f"Train_y: \n\n{train_y}\n")
    
        print(f"Test_X: \n\n{test_X}\n\n")


        encoder = TargetEncoder(smooth = 0).set_output(transform="pandas")

        encoder.fit(train_X, train_y)

        print(encoder.transform(test_X))

    _()
    return


@app.cell
def _():
    from sklearn.preprocessing import StandardScaler, QuantileTransformer, FunctionTransformer

    return FunctionTransformer, QuantileTransformer, StandardScaler


@app.cell
def _(StandardScaler, pd):
    def _():

        train_X = pd.DataFrame(data = {
                                    'feature_1': [100, 200, 300], 
        })

        test_X =  pd.DataFrame(data = {
                                        'feature_1': [50,200, 350], 
        })

        print(f"Train_X: \n\n{train_X}\n")

    
        print(f"Test_X: \n\n{test_X}\n\n")

        scaler = StandardScaler().set_output(transform="pandas")

        scaler.fit(train_X)

        print(scaler.transform(test_X))

    _()
    return


@app.cell
def _(QuantileTransformer, pd):
    def _():

        train_X = pd.DataFrame(data = {
                                    'feature_1': [1, 3, 10], 
        })

        test_X =  pd.DataFrame(data = {
                                        'feature_1': [2, 3, 100_000], 
        })

        print(f"Train_X: \n\n{train_X}\n")

    
        print(f"Test_X: \n\n{test_X}\n\n")

        scaler = QuantileTransformer().set_output(transform="pandas")

        scaler.fit(train_X)

        print(scaler.transform(test_X))

    _()
    return


@app.cell
def _(FunctionTransformer, np, pd):
    def _():

        train_X = pd.DataFrame(data = {
                                    'feature_1': [1, 3, 10], 
        })

        test_X =  pd.DataFrame(data = {
                                        'feature_1': [2, 3, 100_000], 
        })
        print(f"Train_X: \n\n{train_X}\n")

    
        print(f"Test_X: \n\n{test_X}\n\n")

        transformer = FunctionTransformer(lambda x: np.clip(x, 0, 20)).set_output(transform="pandas")

        transformer.fit(train_X)

        print(transformer.transform(test_X))


    _()
    return


@app.cell
def _(FunctionTransformer, np, pd):
    def _():

        train_X = pd.DataFrame(data = {
                                    'feature_1': [0, 100, 10_000], 
        })

        test_X =  pd.DataFrame(data = {
                                        'feature_1': [10, 1_000, 100_000], 
        })

        print(f"Train_X: \n\n{train_X}\n")

    
        print(f"Test_X: \n\n{test_X}\n\n")

        transformer = FunctionTransformer(lambda x: np.log10(1 + x)).set_output(transform="pandas")

        transformer.fit(train_X)

        print(transformer.transform(test_X))

    _()
    return


if __name__ == "__main__":
    app.run()
