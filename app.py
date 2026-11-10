# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from performance_analysis import show_performance_analysis
# from anomaly_detection import show_anomaly_detection
# from chatbot import show_chatbot

# from auth import google_login

# from data_processing import (
#     load_sales_data,
#     clean_sales_data,
#     get_sales_summary,
#     get_yearly_sales,
#     get_monthly_sales
# )

# from forecasting import forecast_sales


# # =====================================================
# # 1. PAGE CONFIGURATION
# # =====================================================

# st.set_page_config(
#     page_title="AI Sales Analytics Dashboard",
#     page_icon="📊",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )


# # =====================================================
# # 2. GOOGLE LOGIN
# # =====================================================

# google_login()


# # =====================================================
# # 3. APPLICATION DESIGN
# # =====================================================

# st.markdown("""
# <style>

# .stApp {
#     background: #FAFAFE;
# }

# .block-container {
#     max-width: 1500px !important;
#     padding-top: 2.5rem !important;
#     padding-bottom: 2rem !important;
# }

# .main-title {
#     font-size: 34px;
#     line-height: 1.4;
#     font-weight: 800;
#     color: #292477;
#     margin-top: 15px;
#     margin-bottom: 8px;
# }

# .page-description {
#     color: #64748b;
#     font-size: 15px;
#     margin-bottom: 22px;
# }

# .welcome-banner {
#     background: linear-gradient(110deg,#4338ca,#7c3aed);
#     padding: 27px 30px;
#     border-radius: 16px;
#     margin-bottom: 22px;
# }

# .welcome-banner h2 {
#     color: white;
#     font-size: 27px;
#     margin: 0 0 8px 0;
# }

# .welcome-banner p {
#     color: #ede9fe;
#     font-size: 15px;
#     margin: 0;
# }

# .feature-card {
#     background: white;
#     border: 1px solid #e5e7eb;
#     border-radius: 13px;
#     padding: 19px;
#     min-height: 125px;
#     margin-bottom: 12px;
# }

# .feature-card h3 {
#     color: #292477;
#     font-size: 18px;
#     margin-bottom: 8px;
# }

# .feature-card p {
#     color: #64748b;
#     font-size: 14px;
# }

# /* METRIC CARD DESIGN */

# div[data-testid="stMetric"] {
#     background: white;
#     border: 1px solid #e5e7eb;
#     padding: 18px;
#     border-radius: 12px;
#     min-height: 105px;
# }

# /* FIX: DISPLAY COMPLETE METRIC VALUES */

# div[data-testid="stMetricValue"] {
#     font-size: clamp(16px, 1.5vw, 23px) !important;
#     white-space: normal !important;
#     overflow: visible !important;
#     text-overflow: clip !important;
#     overflow-wrap: anywhere !important;
#     word-break: break-word !important;
#     line-height: 1.4 !important;
# }

# div[data-testid="stMetricValue"] > div {
#     white-space: normal !important;
#     overflow: visible !important;
#     text-overflow: clip !important;
#     overflow-wrap: anywhere !important;
#     word-break: break-word !important;
# }

# /* SIDEBAR */

# [data-testid="stSidebar"] {
#     background: #f8f7ff;
#     border-right: 1px solid #e5e7eb;
# }

# [data-testid="stSidebar"] .block-container {
#     padding-top: 1.5rem !important;
# }

# [data-testid="stSidebar"] div[role="radiogroup"] {
#     gap: 7px;
# }

# [data-testid="stSidebar"] div[role="radiogroup"] label {
#     background: white;
#     border: 1px solid #eeeaf8;
#     border-radius: 9px;
#     padding: 9px;
# }

# div.stButton > button {
#     border-radius: 9px;
#     font-weight: 600;
#     min-height: 42px;
# }

# </style>
# """, unsafe_allow_html=True)


# # =====================================================
# # 4. MAIN TITLE
# # =====================================================

# st.markdown("""
# <div class="main-title">
#     📊 AI Sales Analytics Dashboard
# </div>
# <div class="page-description">
#     A centralized platform to analyze historical sales,
#     identify business trends and forecast future performance.
# </div>
# """, unsafe_allow_html=True)


# # =====================================================
# # 5. SIDEBAR BRANDING - NATIVE STREAMLIT
# # =====================================================

# st.sidebar.title("📊 AI Sales Analytics")

# st.sidebar.caption("Business Intelligence Platform")

# st.sidebar.divider()


# # =====================================================
# # 6. SIDEBAR NAVIGATION
# # =====================================================

# st.sidebar.markdown("### 🧭 NAVIGATION")

# page_options = {
#     "📊 Dashboard Overview": "Dashboard Overview",
#     "📅 Yearly Sales Analysis": "Yearly Sales Analysis",
#     "📈 Monthly Sales Analysis": "Monthly Sales Analysis",
#     "📉 Sales Growth Trends": "Sales Growth Trends",
#     "🔄 Year Comparison": "Year Comparison",
#     "🤖 AI Sales Report": "AI Sales Report",
#     "🔮 Five-Year Forecast": "Five-Year Forecast",
#     "📁 Processed Sales Data": "Processed Sales Data"
# }

# selected_option = st.sidebar.radio(
#     "Choose a page",
#     options=list(page_options.keys()),
#     key="page_navigation",
#     label_visibility="collapsed"
# )

# page = page_options[selected_option]


# # =====================================================
# # 7. PROFILE AND LOGOUT
# # =====================================================

# st.sidebar.divider()

# st.sidebar.markdown("### 👤 USER PROFILE")

# st.sidebar.success(f"Welcome, {st.user.name}")

# st.sidebar.caption("Google authenticated")

# if st.sidebar.button(
#     "Logout",
#     use_container_width=True,
#     key="sidebar_logout"
# ):
#     st.logout()


# # =====================================================
# # 8. UPLOAD SALES REPORT
# # =====================================================

# st.sidebar.divider()

# st.sidebar.markdown("### 📁 Upload Sales Report")

# st.sidebar.caption(
#     "Upload your company sales report in Excel format."
# )

# uploaded_file = st.sidebar.file_uploader(
#     "Choose Excel file",
#     type=["xlsx", "xls"],
#     key="sales_file"
# )


# # =====================================================
# # 9. HELPER FUNCTIONS
# # =====================================================

# def show_page_heading(title, description):
#     st.header(title)
#     st.caption(description)


# def show_chart(fig, height=420):

#     fig.update_layout(
#         template="plotly_white",
#         height=height,
#         margin=dict(l=20, r=20, t=55, b=20),
#         hovermode="x unified"
#     )

#     st.plotly_chart(
#         fig,
#         use_container_width=True
#     )


# # =====================================================
# # 10. WELCOME PAGE
# # =====================================================

# if uploaded_file is None:

#     st.markdown("""
#     <div class="welcome-banner">
#         <h2>Welcome to AI Sales Analytics 👋</h2>
#         <p>
#             Turn your sales data into meaningful business insights.
#             Explore performance, understand trends and plan ahead.
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

#     st.subheader("🚀 Explore the Platform")

#     col1, col2 = st.columns(2)

#     with col1:

#         st.markdown("""
#         <div class="feature-card">
#             <h3>📅 Yearly Sales Analysis</h3>
#             <p>Understand yearly sales, profit and business performance.</p>
#         </div>

#         <div class="feature-card">
#             <h3>🤖 Automated Sales Report</h3>
#             <p>Review automatically generated business insights.</p>
#         </div>
#         """, unsafe_allow_html=True)

#     with col2:

#         st.markdown("""
#         <div class="feature-card">
#             <h3>📈 Monthly Sales Analysis</h3>
#             <p>Explore monthly sales patterns and trends.</p>
#         </div>

#         <div class="feature-card">
#             <h3>🔮 Five-Year Forecast</h3>
#             <p>Explore estimated future sales performance.</p>
#         </div>
#         """, unsafe_allow_html=True)

#     st.divider()

#     st.info(
#         "📁 Upload your Excel sales report from the sidebar "
#         "to begin the analysis."
#     )

#     st.stop()


# # =====================================================
# # 11. LOAD DATA
# # =====================================================

# try:

#     raw_df = load_sales_data(uploaded_file)

#     df = clean_sales_data(raw_df)

#     if df.empty:
#         st.warning("The uploaded Excel file contains no valid records.")
#         st.stop()

#     summary = get_sales_summary(df)

#     yearly = get_yearly_sales(df)

#     monthly = get_monthly_sales(df)

#     yearly = yearly.sort_values("Year").reset_index(drop=True)

#     monthly = monthly.sort_values(
#         ["Year", "Month"]
#     ).reset_index(drop=True)

# except Exception as e:

#     st.error(f"Error processing sales report: {e}")
#     st.stop()


# st.success(
#     f"Sales report successfully processed! "
#     f"{len(df):,} records are ready for analysis."
# )


# # =====================================================
# # 12. DASHBOARD OVERVIEW
# # =====================================================

# if page == "Dashboard Overview":

#     st.markdown("""
#     <div class="welcome-banner">
#         <h2>Welcome to your Sales Dashboard 📊</h2>
#         <p>
#             Explore business performance, discover trends
#             and understand your sales data.
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

#     st.subheader("📋 Dataset Overview")

#     c1, c2, c3 = st.columns(3)

#     c1.metric("Total Records", f"{len(df):,}")

#     c2.metric("Years Covered", df["Year"].nunique())

#     c3.metric(
#         "Products",
#         df["Product"].nunique()
#         if "Product" in df.columns else "N/A"
#     )

#     st.divider()

#     st.subheader("💰 Business Performance Summary")

#     c1, c2, c3, c4 = st.columns(4)

#     c1.metric(
#         "Total Sales",
#         f"₹{summary['Total Sales']:,.2f}"
#     )

#     c2.metric(
#         "Total Profit",
#         f"₹{summary['Total Profit']:,.2f}"
#     )

#     c3.metric(
#         "Total Quantity",
#         f"{summary['Total Quantity']:,.0f}"
#     )

#     c4.metric(
#         "Total Orders",
#         f"{summary['Total Orders']:,}"
#     )

#     st.divider()

#     st.subheader("📊 Yearly Sales Performance")

#     fig = px.bar(
#         yearly,
#         x="Year",
#         y="Total_Sales",
#         text_auto=".2s",
#         title="Total Sales by Year"
#     )

#     fig.update_traces(marker_color="#6366F1")

#     show_chart(fig)


# # =====================================================
# # 13. YEARLY SALES ANALYSIS
# # =====================================================

# elif page == "Yearly Sales Analysis":

#     show_page_heading(
#         "📅 Yearly Sales Analysis",
#         "Analyze yearly sales, profit and quantity."
#     )

#     st.dataframe(
#         yearly,
#         use_container_width=True,
#         hide_index=True
#     )

#     fig = px.bar(
#         yearly,
#         x="Year",
#         y=["Total_Sales", "Total_Profit"],
#         barmode="group",
#         title="Yearly Sales vs Profit"
#     )

#     show_chart(fig)

#     fig2 = px.line(
#         yearly,
#         x="Year",
#         y="Total_Sales",
#         markers=True,
#         title="Sales Movement Across Years"
#     )

#     show_chart(fig2)


# # =====================================================
# # 14. MONTHLY SALES ANALYSIS
# # =====================================================

# elif page == "Monthly Sales Analysis":

#     show_page_heading(
#         "📈 Monthly Sales Analysis",
#         "Explore monthly sales patterns and trends."
#     )

#     st.dataframe(
#         monthly,
#         use_container_width=True,
#         hide_index=True
#     )

#     monthly_chart = monthly.copy()

#     monthly_chart["Period"] = (
#         monthly_chart["Year"].astype(str)
#         + "-"
#         + monthly_chart["Month"].astype(str).str.zfill(2)
#     )

#     fig = px.line(
#         monthly_chart,
#         x="Period",
#         y="Sales",
#         markers=True,
#         title="Month-wise Sales Trend"
#     )

#     show_chart(fig)

#     fig2 = px.bar(
#         monthly_chart,
#         x="Period",
#         y="Sales",
#         title="Monthly Sales Distribution"
#     )

#     show_chart(fig2)


# # =====================================================
# # 15. SALES GROWTH TRENDS
# # =====================================================

# elif page == "Sales Growth Trends":

#     show_page_heading(
#         "📉 Sales Growth and Decline Trends",
#         "Identify positive and negative changes in sales."
#     )

#     growth = yearly.sort_values("Year").copy()

#     growth["Growth_Percentage"] = (
#         growth["Total_Sales"].pct_change() * 100
#     )

#     growth["Performance"] = growth["Growth_Percentage"].apply(
#         lambda x:
#             "First Year" if pd.isna(x)
#             else "Growth" if x > 0
#             else "Decline" if x < 0
#             else "No Change"
#     )

#     valid_growth = growth.dropna(
#         subset=["Growth_Percentage"]
#     )

#     c1, c2 = st.columns(2)

#     c1.metric(
#         "Growth Years",
#         int((valid_growth["Performance"] == "Growth").sum())
#     )

#     c2.metric(
#         "Decline Years",
#         int((valid_growth["Performance"] == "Decline").sum())
#     )

#     fig = px.bar(
#         valid_growth,
#         x="Year",
#         y="Growth_Percentage",
#         color="Performance",
#         title="Year-over-Year Sales Growth",
#         color_discrete_map={
#             "Growth": "#16A34A",
#             "Decline": "#DC2626",
#             "No Change": "#64748B"
#         }
#     )

#     fig.add_hline(y=0, line_dash="dash")

#     show_chart(fig)

#     st.dataframe(
#         growth,
#         use_container_width=True,
#         hide_index=True
#     )


# # =====================================================
# # 16. YEAR COMPARISON
# # =====================================================

# elif page == "Year Comparison":

#     show_page_heading(
#         "🔄 Year Comparison",
#         "Compare sales and profit between two years."
#     )

#     years = sorted(
#         yearly["Year"].astype(int).unique().tolist()
#     )

#     if len(years) < 2:

#         st.warning("At least two years are required.")

#     else:

#         c1, c2 = st.columns(2)

#         year1 = c1.selectbox(
#             "Select First Year",
#             years,
#             index=0
#         )

#         year2 = c2.selectbox(
#             "Select Second Year",
#             years,
#             index=1
#         )

#         if year1 == year2:

#             st.warning("Select two different years.")

#         else:

#             first = yearly[
#                 yearly["Year"] == year1
#             ].iloc[0]

#             second = yearly[
#                 yearly["Year"] == year2
#             ].iloc[0]

#             sales_change = (
#                 second["Total_Sales"] - first["Total_Sales"]
#             )

#             sales_percent = (
#                 sales_change / first["Total_Sales"] * 100
#                 if first["Total_Sales"] != 0 else 0
#             )

#             profit_change = (
#                 second["Total_Profit"] - first["Total_Profit"]
#             )

#             profit_percent = (
#                 profit_change / first["Total_Profit"] * 100
#                 if first["Total_Profit"] != 0 else 0
#             )

#             c1, c2 = st.columns(2)

#             c1.metric(
#                 f"Sales {year1}",
#                 f"₹{first['Total_Sales']:,.2f}"
#             )

#             c2.metric(
#                 f"Sales {year2}",
#                 f"₹{second['Total_Sales']:,.2f}",
#                 delta=f"{sales_percent:.2f}%"
#             )

#             c3, c4 = st.columns(2)

#             c3.metric(
#                 f"Profit {year1}",
#                 f"₹{first['Total_Profit']:,.2f}"
#             )

#             c4.metric(
#                 f"Profit {year2}",
#                 f"₹{second['Total_Profit']:,.2f}",
#                 delta=f"{profit_percent:.2f}%"
#             )

#             compare_df = pd.DataFrame({
#                 "Year": [str(year1), str(year2)],
#                 "Sales": [
#                     first["Total_Sales"],
#                     second["Total_Sales"]
#                 ],
#                 "Profit": [
#                     first["Total_Profit"],
#                     second["Total_Profit"]
#                 ]
#             })

#             fig = px.bar(
#                 compare_df,
#                 x="Year",
#                 y=["Sales", "Profit"],
#                 barmode="group",
#                 title="Year-wise Business Comparison"
#             )

#             show_chart(fig)


# # =====================================================
# # 17. AUTOMATED SALES REPORT
# # =====================================================

# elif page == "AI Sales Report":

#     show_page_heading(
#         "🤖 Automated Sales Report",
#         "Automatically generated business insights."
#     )

#     best_year = yearly.loc[
#         yearly["Total_Sales"].idxmax()
#     ]

#     lowest_year = yearly.loc[
#         yearly["Total_Sales"].idxmin()
#     ]

#     c1, c2 = st.columns(2)

#     c1.metric(
#         "Total Sales",
#         f"₹{summary['Total Sales']:,.2f}"
#     )

#     c2.metric(
#         "Total Profit",
#         f"₹{summary['Total Profit']:,.2f}"
#     )

#     st.divider()

#     c1, c2 = st.columns(2)

#     c1.metric(
#         "Best Sales Year",
#         int(best_year["Year"])
#     )

#     c2.metric(
#         "Lowest Sales Year",
#         int(lowest_year["Year"])
#     )

#     growth = yearly.sort_values("Year")[
#         "Total_Sales"
#     ].pct_change() * 100

#     latest_growth = growth.iloc[-1]

#     st.subheader("Business Insights")

#     if pd.isna(latest_growth):

#         st.info("More yearly data is required to calculate growth.")

#     elif latest_growth > 0:

#         st.success(
#             f"Sales increased by {latest_growth:.2f}% "
#             "compared with the previous year."
#         )

#     elif latest_growth < 0:

#         st.warning(
#             f"Sales decreased by {abs(latest_growth):.2f}% "
#             "compared with the previous year."
#         )

#     else:

#         st.info("Sales remained unchanged.")

#     st.caption(
#         "These are rule-based automated insights, not an LLM-generated report."
#     )


# # =====================================================
# # 18. FIVE-YEAR FORECAST
# # =====================================================

# elif page == "Five-Year Forecast":

#     show_page_heading(
#         "🔮Next Five Years Sales Prediction",
#          "Predict sales performance for the next five years using historical sales data."
#     )

#     try:

#         forecast_df, yearly_forecast, mae = forecast_sales(monthly)

#         st.success("Five-year forecast generated successfully.")

#         c1, c2 = st.columns(2)

#         c1.metric(
#             "Total Predicted Sales",
#             f"₹{yearly_forecast['Predicted_Sales'].sum():,.2f}"
#         )

#         c2.metric(
#             "Average Yearly Sales",
#             f"₹{yearly_forecast['Predicted_Sales'].mean():,.2f}"
#         )

#         st.subheader("Yearly Forecast")

#         st.dataframe(
#             yearly_forecast,
#             use_container_width=True,
#             hide_index=True
#         )

#         fig = px.bar(
#             yearly_forecast,
#             x="Year",
#             y="Predicted_Sales",
#             title="Five-Year Sales Forecast"
#         )

#         show_chart(fig)

#         st.subheader("Monthly Forecast")

#         fig2 = px.line(
#             forecast_df,
#             x="Date",
#             y="Predicted_Sales",
#             markers=True,
#             title="Monthly Sales Prediction"
#         )

#         show_chart(fig2)

#         forecast_display = forecast_df.copy()

#         forecast_display["Date"] = (
#             pd.to_datetime(forecast_display["Date"])
#             .dt.strftime("%Y-%m-%d")
#         )

#         st.dataframe(
#             forecast_display,
#             use_container_width=True,
#             hide_index=True
#         )

#         c1, c2 = st.columns(2)

#         with c1:

#             st.download_button(
#                 "Download Yearly Forecast",
#                 yearly_forecast.to_csv(index=False),
#                 file_name="yearly_forecast.csv",
#                 mime="text/csv",
#                 use_container_width=True
#             )

#         with c2:

#             st.download_button(
#                 "Download Monthly Forecast",
#                 forecast_df.to_csv(index=False),
#                 file_name="monthly_forecast.csv",
#                 mime="text/csv",
#                 use_container_width=True
#             )

#         st.caption(
#             "Forecasts are estimates; actual future sales may differ."
#         )

#     except Exception as e:

#         st.error(f"Forecasting error: {e}")


# # =====================================================
# # 19. PROCESSED SALES DATA
# # =====================================================

# elif page == "Processed Sales Data":

#     show_page_heading(
#         "📁 Processed Sales Data",
#         "View the cleaned sales records."
#     )

#     st.write(f"Total Records: **{len(df):,}**")

#     st.dataframe(
#         df,
#         use_container_width=True,
#         hide_index=True
#     )

#     st.download_button(
#         "⬇️ Download Processed Data",
#         df.to_csv(index=False),
#         file_name="processed_sales_data.csv",
#         mime="text/csv"
#     )


# # =====================================================
# # 20. FOOTER
# # =====================================================

# st.divider()

# st.caption(
#     "AI Sales Analytics | Sales Analysis • Business Insights • "
#     "Predictive Forecasting"
# )

# # Performance Analysis
# if not filtered_df.empty:
#     show_performance_analysis(filtered_df)

#     # Anomaly Detection
#     show_anomaly_detection(filtered_df)

#     # AI Sales Chatbot
#     show_chatbot(
#         filtered_df,
#         client,
#         model
#     )

# else:
#     st.warning("No data available for the selected filters.")



import streamlit as st
import os
import pandas as pd
import plotly.express as px

from performance_analysis import show_performance_analysis
from anomaly_detection import show_anomaly_detection
from chatbot import show_chatbot

from auth import google_login

from data_processing import (
    load_sales_data,
    clean_sales_data,
    get_sales_summary,
    get_yearly_sales,
    get_monthly_sales
)

from forecasting import forecast_sales


# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="AI Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# 2. GOOGLE LOGIN
# =====================================================

google_login()


# =====================================================
# 3. APPLICATION DESIGN
# =====================================================

st.markdown("""
<style>

.stApp {
    background: #FAFAFE;
}

.block-container {
    max-width: 1500px !important;
    padding-top: 2.5rem !important;
    padding-bottom: 2rem !important;
}

.main-title {
    font-size: 34px;
    line-height: 1.4;
    font-weight: 800;
    color: #292477;
    margin-top: 15px;
    margin-bottom: 8px;
}

.page-description {
    color: #64748b;
    font-size: 15px;
    margin-bottom: 22px;
}

.welcome-banner {
    background: linear-gradient(110deg,#4338ca,#7c3aed);
    padding: 27px 30px;
    border-radius: 16px;
    margin-bottom: 22px;
}

.welcome-banner h2 {
    color: white;
    font-size: 27px;
    margin: 0 0 8px 0;
}

.welcome-banner p {
    color: #ede9fe;
    font-size: 15px;
    margin: 0;
}

.feature-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 13px;
    padding: 19px;
    min-height: 125px;
    margin-bottom: 12px;
}

.feature-card h3 {
    color: #292477;
    font-size: 18px;
    margin-bottom: 8px;
}

.feature-card p {
    color: #64748b;
    font-size: 14px;
}

/* METRIC CARD DESIGN */

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e5e7eb;
    padding: 18px;
    border-radius: 12px;
    min-height: 105px;
}

/* DISPLAY COMPLETE METRIC VALUES */

div[data-testid="stMetricValue"] {
    font-size: clamp(16px, 1.5vw, 23px) !important;
    white-space: normal !important;
    overflow: visible !important;
    text-overflow: clip !important;
    overflow-wrap: anywhere !important;
    word-break: break-word !important;
    line-height: 1.4 !important;
}

div[data-testid="stMetricValue"] > div {
    white-space: normal !important;
    overflow: visible !important;
    text-overflow: clip !important;
    overflow-wrap: anywhere !important;
    word-break: break-word !important;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background: #f8f7ff;
    border-right: 1px solid #e5e7eb;
}

[data-testid="stSidebar"] .block-container {
    padding-top: 1.5rem !important;
}

[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 7px;
}

[data-testid="stSidebar"] div[role="radiogroup"] label {
    background: white;
    border: 1px solid #eeeaf8;
    border-radius: 9px;
    padding: 9px;
}

div.stButton > button {
    border-radius: 9px;
    font-weight: 600;
    min-height: 42px;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# 4. MAIN TITLE
# =====================================================

st.markdown("""
<div class="main-title">
    📊 AI Sales Analytics Dashboard
</div>
<div class="page-description">
    A centralized platform to analyze historical sales,
    identify business trends and forecast future performance.
</div>
""", unsafe_allow_html=True)


# =====================================================
# 5. SIDEBAR BRANDING
# =====================================================

st.sidebar.title("📊 AI Sales Analytics")

st.sidebar.caption("Business Intelligence Platform")

st.sidebar.divider()


# =====================================================
# 6. SIDEBAR NAVIGATION
# =====================================================

st.sidebar.markdown("### 🧭 NAVIGATION")

page_options = {
    "📊 Dashboard Overview": "Dashboard Overview",
    "📅 Yearly Sales Analysis": "Yearly Sales Analysis",
    "📈 Monthly Sales Analysis": "Monthly Sales Analysis",
    "📉 Sales Growth Trends": "Sales Growth Trends",
    "🔄 Year Comparison": "Year Comparison",
    "🤖 AI Sales Report": "AI Sales Report",
    "🔮 Five-Year Forecast": "Five-Year Forecast",
    "📁 Processed Sales Data": "Processed Sales Data",
    "🤖 Advanced Analytics": "Advanced Analytics"
}

selected_option = st.sidebar.radio(
    "Choose a page",
    options=list(page_options.keys()),
    key="page_navigation",
    label_visibility="collapsed"
)

page = page_options[selected_option]


# =====================================================
# 7. PROFILE AND LOGOUT
# =====================================================

st.sidebar.divider()

st.sidebar.markdown("### 👤 USER PROFILE")

st.sidebar.success(f"Welcome, {st.user.name}")

st.sidebar.caption("Google authenticated")

if st.sidebar.button(
    "Logout",
    use_container_width=True,
    key="sidebar_logout"
):
    st.logout()


# =====================================================
# 8. UPLOAD SALES REPORT
# =====================================================

st.sidebar.divider()

st.sidebar.markdown("### 📁 Upload Sales Report")

st.sidebar.caption(
    "Upload your company sales report in Excel format."
)

uploaded_file = st.sidebar.file_uploader(
    "Choose Excel file",
    type=["xlsx", "xls"],
    key="sales_file"
)


# =====================================================
# 9. HELPER FUNCTIONS
# =====================================================

def show_page_heading(title, description):
    st.header(title)
    st.caption(description)


def show_chart(fig, height=420):

    fig.update_layout(
        template="plotly_white",
        height=height,
        margin=dict(l=20, r=20, t=55, b=20),
        hovermode="x unified"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# 10. WELCOME PAGE
# =====================================================

if uploaded_file is None:

    st.markdown("""
    <div class="welcome-banner">
        <h2>Welcome to AI Sales Analytics 👋</h2>
        <p>
            Turn your sales data into meaningful business insights.
            Explore performance, understand trends and plan ahead.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🚀 Explore the Platform")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="feature-card">
            <h3>📅 Yearly Sales Analysis</h3>
            <p>Understand yearly sales, profit and business performance.</p>
        </div>

        <div class="feature-card">
            <h3>🤖 Automated Sales Report</h3>
            <p>Review automatically generated business insights.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="feature-card">
            <h3>📈 Monthly Sales Analysis</h3>
            <p>Explore monthly sales patterns and trends.</p>
        </div>

        <div class="feature-card">
            <h3>🔮 Five-Year Forecast</h3>
            <p>Explore estimated future sales performance.</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.info(
        "📁 Upload your Excel sales report from the sidebar "
        "to begin the analysis."
    )

    st.stop()


# =====================================================
# 11. LOAD DATA
# =====================================================

try:

    raw_df = load_sales_data(uploaded_file)

    df = clean_sales_data(raw_df)

    if df.empty:
        st.warning("The uploaded Excel file contains no valid records.")
        st.stop()

    summary = get_sales_summary(df)

    yearly = get_yearly_sales(df)

    monthly = get_monthly_sales(df)

    yearly = yearly.sort_values("Year").reset_index(drop=True)

    monthly = monthly.sort_values(
        ["Year", "Month"]
    ).reset_index(drop=True)

except Exception as e:

    st.error(f"Error processing sales report: {e}")
    st.stop()


st.success(
    f"Sales report successfully processed! "
    f"{len(df):,} records are ready for analysis."
)
# =====================================================
# 12. DASHBOARD OVERVIEW
# =====================================================

if page == "Dashboard Overview":

    st.markdown("""
    <div class="welcome-banner">
        <h2>Welcome to your Sales Dashboard 📊</h2>
        <p>
            Explore business performance, discover trends
            and understand your sales data.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📋 Dataset Overview")

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Records", f"{len(df):,}")

    c2.metric("Years Covered", df["Year"].nunique())

    c3.metric(
        "Products",
        df["Product"].nunique()
        if "Product" in df.columns else "N/A"
    )

    st.divider()

    st.subheader("💰 Business Performance Summary")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Sales",
        f"₹{summary['Total Sales']:,.2f}"
    )

    c2.metric(
        "Total Profit",
        f"₹{summary['Total Profit']:,.2f}"
    )

    c3.metric(
        "Total Quantity",
        f"{summary['Total Quantity']:,.0f}"
    )

    c4.metric(
        "Total Orders",
        f"{summary['Total Orders']:,}"
    )

    st.divider()

    st.subheader("📊 Yearly Sales Performance")

    fig = px.bar(
        yearly,
        x="Year",
        y="Total_Sales",
        text_auto=".2s",
        title="Total Sales by Year"
    )

    fig.update_traces(marker_color="#6366F1")

    show_chart(fig)


# =====================================================
# 13. YEARLY SALES ANALYSIS
# =====================================================

elif page == "Yearly Sales Analysis":

    show_page_heading(
        "📅 Yearly Sales Analysis",
        "Analyze yearly sales, profit and quantity."
    )

    st.dataframe(
        yearly,
        use_container_width=True,
        hide_index=True
    )

    fig = px.bar(
        yearly,
        x="Year",
        y=["Total_Sales", "Total_Profit"],
        barmode="group",
        title="Yearly Sales vs Profit"
    )

    show_chart(fig)

    fig2 = px.line(
        yearly,
        x="Year",
        y="Total_Sales",
        markers=True,
        title="Sales Movement Across Years"
    )

    show_chart(fig2)


# =====================================================
# 14. MONTHLY SALES ANALYSIS
# =====================================================

elif page == "Monthly Sales Analysis":

    show_page_heading(
        "📈 Monthly Sales Analysis",
        "Explore monthly sales patterns and trends."
    )

    st.dataframe(
        monthly,
        use_container_width=True,
        hide_index=True
    )

    monthly_chart = monthly.copy()

    monthly_chart["Period"] = (
        monthly_chart["Year"].astype(str)
        + "-"
        + monthly_chart["Month"].astype(str).str.zfill(2)
    )

    fig = px.line(
        monthly_chart,
        x="Period",
        y="Sales",
        markers=True,
        title="Month-wise Sales Trend"
    )

    show_chart(fig)

    fig2 = px.bar(
        monthly_chart,
        x="Period",
        y="Sales",
        title="Monthly Sales Distribution"
    )

    show_chart(fig2)


# =====================================================
# 15. SALES GROWTH TRENDS
# =====================================================

elif page == "Sales Growth Trends":

    show_page_heading(
        "📉 Sales Growth and Decline Trends",
        "Identify positive and negative changes in sales."
    )

    growth = yearly.sort_values("Year").copy()

    growth["Growth_Percentage"] = (
        growth["Total_Sales"].pct_change() * 100
    )

    growth["Performance"] = growth["Growth_Percentage"].apply(
        lambda x:
            "First Year" if pd.isna(x)
            else "Growth" if x > 0
            else "Decline" if x < 0
            else "No Change"
    )

    valid_growth = growth.dropna(
        subset=["Growth_Percentage"]
    )

    c1, c2 = st.columns(2)

    c1.metric(
        "Growth Years",
        int((valid_growth["Performance"] == "Growth").sum())
    )

    c2.metric(
        "Decline Years",
        int((valid_growth["Performance"] == "Decline").sum())
    )

    fig = px.bar(
        valid_growth,
        x="Year",
        y="Growth_Percentage",
        color="Performance",
        title="Year-over-Year Sales Growth",
        color_discrete_map={
            "Growth": "#16A34A",
            "Decline": "#DC2626",
            "No Change": "#64748B"
        }
    )

    fig.add_hline(y=0, line_dash="dash")

    show_chart(fig)

    st.dataframe(
        growth,
        use_container_width=True,
        hide_index=True
    )


# =====================================================
# 16. YEAR COMPARISON
# =====================================================

elif page == "Year Comparison":

    show_page_heading(
        "🔄 Year Comparison",
        "Compare sales and profit between two years."
    )

    years = sorted(
        yearly["Year"].astype(int).unique().tolist()
    )

    if len(years) < 2:

        st.warning("At least two years are required.")

    else:

        c1, c2 = st.columns(2)

        year1 = c1.selectbox(
            "Select First Year",
            years,
            index=0
        )

        year2 = c2.selectbox(
            "Select Second Year",
            years,
            index=1
        )

        if year1 == year2:

            st.warning("Select two different years.")

        else:

            first = yearly[
                yearly["Year"] == year1
            ].iloc[0]

            second = yearly[
                yearly["Year"] == year2
            ].iloc[0]

            sales_change = (
                second["Total_Sales"] - first["Total_Sales"]
            )

            sales_percent = (
                sales_change / first["Total_Sales"] * 100
                if first["Total_Sales"] != 0 else 0
            )

            profit_change = (
                second["Total_Profit"] - first["Total_Profit"]
            )

            profit_percent = (
                profit_change / first["Total_Profit"] * 100
                if first["Total_Profit"] != 0 else 0
            )

            c1, c2 = st.columns(2)

            c1.metric(
                f"Sales {year1}",
                f"₹{first['Total_Sales']:,.2f}"
            )

            c2.metric(
                f"Sales {year2}",
                f"₹{second['Total_Sales']:,.2f}",
                delta=f"{sales_percent:.2f}%"
            )

            c3, c4 = st.columns(2)

            c3.metric(
                f"Profit {year1}",
                f"₹{first['Total_Profit']:,.2f}"
            )

            c4.metric(
                f"Profit {year2}",
                f"₹{second['Total_Profit']:,.2f}",
                delta=f"{profit_percent:.2f}%"
            )

            compare_df = pd.DataFrame({
                "Year": [str(year1), str(year2)],
                "Sales": [
                    first["Total_Sales"],
                    second["Total_Sales"]
                ],
                "Profit": [
                    first["Total_Profit"],
                    second["Total_Profit"]
                ]
            })

            fig = px.bar(
                compare_df,
                x="Year",
                y=["Sales", "Profit"],
                barmode="group",
                title="Year-wise Business Comparison"
            )

            show_chart(fig)
            # =====================================================
# 17. AUTOMATED SALES REPORT
# =====================================================

elif page == "AI Sales Report":

    show_page_heading(
        "🤖 Automated Sales Report",
        "Automatically generated business insights."
    )

    best_year = yearly.loc[
        yearly["Total_Sales"].idxmax()
    ]

    lowest_year = yearly.loc[
        yearly["Total_Sales"].idxmin()
    ]

    c1, c2 = st.columns(2)

    c1.metric(
        "Total Sales",
        f"₹{summary['Total Sales']:,.2f}"
    )

    c2.metric(
        "Total Profit",
        f"₹{summary['Total Profit']:,.2f}"
    )

    st.divider()

    c1, c2 = st.columns(2)

    c1.metric(
        "Best Sales Year",
        int(best_year["Year"])
    )

    c2.metric(
        "Lowest Sales Year",
        int(lowest_year["Year"])
    )

    growth = yearly.sort_values("Year")[
        "Total_Sales"
    ].pct_change() * 100

    latest_growth = growth.iloc[-1]

    st.subheader("Business Insights")

    if pd.isna(latest_growth):

        st.info("More yearly data is required to calculate growth.")

    elif latest_growth > 0:

        st.success(
            f"Sales increased by {latest_growth:.2f}% "
            "compared with the previous year."
        )

    elif latest_growth < 0:

        st.warning(
            f"Sales decreased by {abs(latest_growth):.2f}% "
            "compared with the previous year."
        )

    else:

        st.info("Sales remained unchanged.")

    st.caption(
        "These are rule-based automated insights, not an LLM-generated report."
    )


# =====================================================
# 18. FIVE-YEAR FORECAST
# =====================================================

elif page == "Five-Year Forecast":

    show_page_heading(
        "🔮 Next Five Years Sales Prediction",
        "Predict sales performance for the next five years using historical sales data."
    )

    try:

        forecast_df, yearly_forecast, mae = forecast_sales(monthly)

        st.success("Five-year forecast generated successfully.")

        c1, c2 = st.columns(2)

        c1.metric(
            "Total Predicted Sales",
            f"₹{yearly_forecast['Predicted_Sales'].sum():,.2f}"
        )

        c2.metric(
            "Average Yearly Sales",
            f"₹{yearly_forecast['Predicted_Sales'].mean():,.2f}"
        )

        st.subheader("Yearly Forecast")

        st.dataframe(
            yearly_forecast,
            use_container_width=True,
            hide_index=True
        )

        fig = px.bar(
            yearly_forecast,
            x="Year",
            y="Predicted_Sales",
            title="Five-Year Sales Forecast"
        )

        show_chart(fig)

        st.subheader("Monthly Forecast")

        fig2 = px.line(
            forecast_df,
            x="Date",
            y="Predicted_Sales",
            markers=True,
            title="Monthly Sales Prediction"
        )

        show_chart(fig2)

        forecast_display = forecast_df.copy()

        forecast_display["Date"] = (
            pd.to_datetime(forecast_display["Date"])
            .dt.strftime("%Y-%m-%d")
        )

        st.dataframe(
            forecast_display,
            use_container_width=True,
            hide_index=True
        )

        c1, c2 = st.columns(2)

        with c1:

            st.download_button(
                "Download Yearly Forecast",
                yearly_forecast.to_csv(index=False),
                file_name="yearly_forecast.csv",
                mime="text/csv",
                use_container_width=True
            )

        with c2:

            st.download_button(
                "Download Monthly Forecast",
                forecast_df.to_csv(index=False),
                file_name="monthly_forecast.csv",
                mime="text/csv",
                use_container_width=True
            )

        st.caption(
            "Forecasts are estimates; actual future sales may differ."
        )

    except Exception as e:

        st.error(f"Forecasting error: {e}")


# =====================================================
# 19. PROCESSED SALES DATA
# =====================================================

elif page == "Processed Sales Data":

    show_page_heading(
        "📁 Processed Sales Data",
        "View the cleaned sales records."
    )

    st.write(f"Total Records: **{len(df):,}**")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.download_button(
        "⬇️ Download Processed Data",
        df.to_csv(index=False),
        file_name="processed_sales_data.csv",
        mime="text/csv"
    )


# =====================================================
# 20. ADVANCED ANALYTICS
# =====================================================

elif page == "Advanced Analytics":

    show_page_heading(
        "🤖 Advanced Sales Analytics",
        "Explore top and bottom performers, unusual sales patterns, "
        "and ask questions about your sales data."
    )

    # Use all cleaned records.
    # No additional filters are currently configured.
    filtered_df = df.copy()

    if not filtered_df.empty:

        # 1. TOP AND BOTTOM PERFORMERS
        st.subheader("🏆 Top and Bottom Performers")

        show_performance_analysis(filtered_df)

        st.divider()

        # 2. AUTOMATIC ANOMALY DETECTION
        st.subheader("🚨 Automatic Anomaly Detection")

        show_anomaly_detection(filtered_df)

        st.divider()

        # 3. AI SALES CHATBOT
        st.subheader("💬 AI Sales Chatbot")

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:

            try:
                api_key = st.secrets["GEMINI_API_KEY"]

            except Exception:
                api_key = None

        if api_key:

            try:

                from google import genai

                client = genai.Client(
                    api_key=api_key
                )

                model = os.getenv(
                    "GEMINI_MODEL",
                    "gemini-2.5-flash"
                )

                show_chatbot(
                    filtered_df,
                    client,
                    model
                )

            except Exception as e:

                st.error(
                    "Unable to start the AI Sales Chatbot. "
                    f"Please check your Gemini API configuration. Details: {e}"
                )

        else:

            st.info(
                "To use the AI Sales Chatbot, configure GEMINI_API_KEY "
                "in your environment or .streamlit/secrets.toml file."
            )

    else:

        st.warning(
            "No data available for the selected dataset."
        )


# =====================================================
# 21. FOOTER
# =====================================================

st.divider()

st.caption(
    "AI Sales Analytics | Sales Analysis • Business Insights • "
    "Predictive Forecasting"
)