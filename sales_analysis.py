
def calculate_yearly_growth(yearly_data):
    """
    Calculate yearly sales growth and decline percentage.
    """

    yearly_data = yearly_data.copy()

    yearly_data = yearly_data.sort_values("Year")

    yearly_data["Previous_Year_Sales"] = (
        yearly_data["Total_Sales"].shift(1)
    )

    yearly_data["Growth_Percentage"] = (
        (
            yearly_data["Total_Sales"]
            - yearly_data["Previous_Year_Sales"]
        )
        / yearly_data["Previous_Year_Sales"]
    ) * 100

    yearly_data["Performance"] = yearly_data[
        "Growth_Percentage"
    ].apply(
        lambda x: (
            "First Year" if x != x
            else "Growth" if x > 0
            else "Decline" if x < 0
            else "No Change"
        )
    )

    return yearly_data


def get_best_and_worst_year(yearly_data):
    """
    Find the highest and lowest sales years.
    """

    best_year = yearly_data.loc[
        yearly_data["Total_Sales"].idxmax()
    ]

    worst_year = yearly_data.loc[
        yearly_data["Total_Sales"].idxmin()
    ]

    return best_year, worst_year


def get_sales_performance(yearly_data):
    """
    Generate overall sales performance information.
    """

    total_sales = yearly_data["Total_Sales"].sum()

    average_sales = yearly_data["Total_Sales"].mean()

    return {
        "Total Sales": total_sales,
        "Average Yearly Sales": average_sales,
        "Best Year": int(
            yearly_data.loc[
                yearly_data["Total_Sales"].idxmax(), "Year"
            ]
        ),
        "Worst Year": int(
            yearly_data.loc[
                yearly_data["Total_Sales"].idxmin(), "Year"
            ]
        )
    }
