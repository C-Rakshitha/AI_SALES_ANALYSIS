
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


# ==========================================
# 1. CREATE MACHINE LEARNING FEATURES
# ==========================================

def create_features(data):

    df = data.copy()

    # Extract month and year
    df["Month_Number"] = df["Date"].dt.month
    df["Year_Number"] = df["Date"].dt.year

    # Capture seasonal patterns
    df["Month_Sin"] = np.sin(
        2 * np.pi * df["Month_Number"] / 12
    )

    df["Month_Cos"] = np.cos(
        2 * np.pi * df["Month_Number"] / 12
    )

    # Previous sales values
    for lag in [1, 2, 3, 6, 12]:

        df[f"Lag_{lag}"] = df["Sales"].shift(lag)

    return df


# ==========================================
# 2. FIVE-YEAR SALES FORECASTING
# ==========================================

def forecast_sales(monthly_data):

    df = monthly_data.copy()

    # Convert year and month into date
    df["Date"] = pd.to_datetime(
        df["Year"].astype(str)
        + "-"
        + df["Month"].astype(str)
        + "-01",
        errors="coerce"
    )

    # Clean sales values
    df["Sales"] = pd.to_numeric(
        df["Sales"],
        errors="coerce"
    )

    df = df.dropna(
        subset=["Date", "Sales"]
    )

    # Combine duplicate months if present
    df = (
        df.groupby("Date", as_index=False)["Sales"]
        .sum()
        .sort_values("Date")
        .reset_index(drop=True)
    )

    # Check historical data
    if len(df) < 24:

        raise ValueError(
            "At least 24 months of historical sales "
            "are required for forecasting."
        )

    if (df["Sales"] < 0).any():

        raise ValueError(
            "Negative sales values must be checked "
            "before forecasting."
        )

    # Check monthly continuity
    expected_dates = pd.date_range(
        start=df["Date"].min(),
        end=df["Date"].max(),
        freq="MS"
    )

    if not df["Date"].equals(
        pd.Series(expected_dates, name="Date")
    ):

        raise ValueError(
            "Some months are missing from the historical data. "
            "Please check your monthly sales records."
        )

    # ======================================
    # 3. PREPARE TRAINING DATA
    # ======================================

    feature_df = create_features(df)

    feature_columns = [
        "Month_Number",
        "Year_Number",
        "Month_Sin",
        "Month_Cos",
        "Lag_1",
        "Lag_2",
        "Lag_3",
        "Lag_6",
        "Lag_12"
    ]

    training_data = feature_df.dropna().copy()

    X = training_data[feature_columns]

    y = training_data["Sales"]

    # ======================================
    # 4. VALIDATE MODEL USING LAST 12 MONTHS
    # ======================================

    split_index = len(training_data) - 12

    if split_index < 12:

        raise ValueError(
            "Not enough historical records for model validation."
        )

    X_train = X.iloc[:split_index]
    y_train = y.iloc[:split_index]

    X_test = X.iloc[split_index:]
    y_test = y.iloc[split_index:]

    validation_model = RandomForestRegressor(
        n_estimators=300,
        max_depth=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )

    validation_model.fit(
        X_train,
        y_train
    )

    test_predictions = validation_model.predict(
        X_test
    )

    mae = mean_absolute_error(
        y_test,
        test_predictions
    )

    # ======================================
    # 5. TRAIN FINAL MODEL ON ALL DATA
    # ======================================

    model = RandomForestRegressor(
        n_estimators=300,
        max_depth=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )

    model.fit(
        X,
        y
    )

    # ======================================
    # 6. PREDICT NEXT 60 MONTHS
    # ======================================

    history = list(df["Sales"].values)

    last_date = df["Date"].max()

    future_dates = pd.date_range(
        start=last_date + pd.offsets.MonthBegin(1),
        periods=60,
        freq="MS"
    )

    predictions = []

    for future_date in future_dates:

        # Previous monthly sales
        lag_1 = history[-1]
        lag_2 = history[-2]
        lag_3 = history[-3]
        lag_6 = history[-6]
        lag_12 = history[-12]

        month_number = future_date.month

        year_number = future_date.year

        month_sin = np.sin(
            2 * np.pi * month_number / 12
        )

        month_cos = np.cos(
            2 * np.pi * month_number / 12
        )

        input_data = pd.DataFrame([{
            "Month_Number": month_number,
            "Year_Number": year_number,
            "Month_Sin": month_sin,
            "Month_Cos": month_cos,
            "Lag_1": lag_1,
            "Lag_2": lag_2,
            "Lag_3": lag_3,
            "Lag_6": lag_6,
            "Lag_12": lag_12
        }])

        predicted_sales = model.predict(
            input_data[feature_columns]
        )[0]

        predicted_sales = max(
            0,
            float(predicted_sales)
        )

        predictions.append(predicted_sales)

        # Use prediction as input for next month
        history.append(predicted_sales)

    # ======================================
    # 7. CREATE MONTHLY FORECAST
    # ======================================

    forecast_df = pd.DataFrame({
        "Date": future_dates,
        "Predicted_Sales": predictions
    })

    forecast_df["Year"] = (
        forecast_df["Date"].dt.year
    )

    forecast_df["Month"] = (
        forecast_df["Date"].dt.month
    )

    forecast_df["Month_Name"] = (
        forecast_df["Date"].dt.strftime("%B")
    )

    # ======================================
    # 8. CREATE YEARLY FORECAST
    # ======================================

    yearly_forecast = (
        forecast_df.groupby("Year")["Predicted_Sales"]
        .sum()
        .reset_index()
    )

    yearly_forecast.columns = [
        "Year",
        "Predicted_Sales"
    ]

    # ======================================
    # 9. RETURN RESULTS
    # ======================================

    return forecast_df, yearly_forecast, mae
