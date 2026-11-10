import streamlit as st
import plotly.express as px


def show_performance_analysis(df):

    st.header("Top and Bottom Performers")

    # Product performance
    product_sales = (
        df.groupby("Product")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top 5 Products")

        top_products = product_sales.head(5)

        fig = px.bar(
            top_products,
            x="Sales",
            y="Product",
            orientation="h",
            title="Top 5 Selling Products"
        )

        fig.update_layout(yaxis={"categoryorder": "total ascending"})

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Bottom 5 Products")

        bottom_products = product_sales.tail(5)

        fig = px.bar(
            bottom_products,
            x="Sales",
            y="Product",
            orientation="h",
            title="Lowest 5 Selling Products"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Region performance
    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Best Performing Regions")

        st.dataframe(
            region_sales.head(5),
            use_container_width=True
        )

    with col4:
        st.subheader("Lowest Performing Regions")

        st.dataframe(
            region_sales.tail(5),
            use_container_width=True
        )