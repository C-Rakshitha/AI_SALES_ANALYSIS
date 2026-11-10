
import streamlit as st
import pandas as pd


def show_chatbot(df, client, model, forecast_summary=None):

    st.header("AI Sales Assistant")

    st.write(
        "Ask questions about your uploaded sales data."
    )

    # Calculate actual sales information
    yearly = (
        df.groupby(df["Order Date"].dt.year)["Sales"]
        .sum()
    )

    products = (
        df.groupby("Product")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    regions = (
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    monthly = (
        df.groupby(
            pd.Grouper(key="Order Date", freq="MS")
        )["Sales"]
        .sum()
    )

    summary = f"""
    SALES DATA SUMMARY

    Total Sales: {df['Sales'].sum():,.2f}
    Total Profit: {df['Profit'].sum():,.2f}

    Yearly Sales:
    {yearly.to_string()}

    Product Sales:
    {products.to_string()}

    Regional Sales:
    {regions.to_string()}

    Recent Monthly Sales:
    {monthly.tail(12).to_string()}

    Future Forecast:
    {forecast_summary or 'Forecast information not supplied.'}
    """

    # Initialize conversation
    if "sales_chat_history" not in st.session_state:
        st.session_state.sales_chat_history = []

    # Display previous messages
    for message in st.session_state.sales_chat_history:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input(
        "Ask something about your sales..."
    )

    if question:

        st.session_state.sales_chat_history.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.markdown(question)

        prompt = f"""
        You are an AI Sales Analytics Assistant.

        Answer questions using only the supplied sales summary.

        Rules:
        1. Use actual figures from the supplied data.
        2. Never invent sales numbers.
        3. If information is unavailable, clearly say so.
        4. Explain sales increases and decreases using available
           comparisons. Do not assume their causes.
        5. For future predictions, use the supplied forecast.
        6. Give clear, professional business insights.

        {summary}

        User Question:
        {question}
        """

        try:

            with st.chat_message("assistant"):

                with st.spinner("Analyzing sales data..."):

                    response = client.models.generate_content(
                        model=model,
                        contents=prompt
                    )

                    answer = response.text

                st.markdown(answer)

            st.session_state.sales_chat_history.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as e:

            st.error(f"Unable to generate response: {e}")

    if st.button("Clear Chat"):
        st.session_state.sales_chat_history = []
        st.rerun()
