import streamlit as st
import pandas as pd
import plotly.express as px


def show_anomaly_detection(df):

    st.header("Automatic Sales Anomaly Detection")

    monthly_sales = (
        df.groupby(
            pd.Grouper(key="Order Date", freq="MS")
        )["Sales"]
        .sum()
        .reset_index()
    )

    monthly_sales = monthly_sales.sort_values("Order Date")

    monthly_sales["Change %"] = (
        monthly_sales["Sales"].pct_change() * 100
    )

    threshold = st.slider(
        "Anomaly Threshold (%)",
        min_value=10,
        max_value=80,
        value=40
    )

    monthly_sales["Anomaly"] = monthly_sales["Change %"].apply(
        lambda x:
        "Sudden Increase" if x >= threshold
        else "Sudden Decrease" if x <= -threshold
        else "Normal"
    )

    anomalies = monthly_sales[
        monthly_sales["Anomaly"] != "Normal"
    ]

    if anomalies.empty:
        st.success("No unusual monthly sales changes detected.")
    else:
        st.warning(
            f"{len(anomalies)} unusual sales changes detected."
        )

        st.dataframe(
            anomalies,
            use_container_width=True
        )

    fig = px.line(
        monthly_sales,
        x="Order Date",
        y="Sales",
        markers=True,
        title="Monthly Sales Anomaly Detection"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Anomaly Details")

    if not anomalies.empty:

        for _, row in anomalies.iterrows():

            st.write(
                f"**{row['Order Date'].strftime('%B %Y')}**"
            )

            st.write(
                f"Sales change: {row['Change %']:.2f}%"
            )

            st.write(
                f"Detection: {row['Anomaly']}"
            )