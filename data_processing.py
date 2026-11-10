
import pandas as pd


def load_sales_data(uploaded_file):
    """Load sales data from an uploaded Excel file."""
    try:
        df = pd.read_excel(uploaded_file)

        if df.empty:
            raise ValueError("The uploaded Excel file is empty.")

        return df

    except Exception as e:
        raise ValueError(f"Error loading Excel file: {e}")


def clean_sales_data(df):
    """Clean and prepare the sales dataset."""

    df = df.copy()

    # Remove duplicate records
    df = df.drop_duplicates()

    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()

    # Check required columns
    required_columns = [
        "Order Date",
        "Sales",
        "Profit",
        "Quantity"
    ]

    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Convert date column
    df["Order Date"] = pd.to_datetime(
        df["Order Date"], errors="coerce"
    )

    # Convert numeric columns
    for col in ["Sales", "Profit", "Quantity"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove invalid rows
    df = df.dropna(
        subset=["Order Date", "Sales", "Profit", "Quantity"]
    )

    # Extract year and month
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    df["Month Name"] = df["Order Date"].dt.strftime("%B")

    return df


def get_sales_summary(df):
    """Calculate overall sales summary."""

    return {
        "Total Sales": df["Sales"].sum(),
        "Total Profit": df["Profit"].sum(),
        "Total Quantity": df["Quantity"].sum(),
        "Total Orders": len(df),
        "Average Sales": df["Sales"].mean()
    }


def get_yearly_sales(df):
    """Calculate year-wise sales and profit."""

    yearly = df.groupby("Year").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum")
    ).reset_index()

    return yearly


def get_monthly_sales(df):
    monthly = df.groupby(
        ["Year", "Month", "Month Name"]
    )["Sales"].sum().reset_index()

    return monthly