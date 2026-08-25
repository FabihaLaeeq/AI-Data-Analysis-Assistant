import plotly.express as px
import pandas as pd


def sales_by_product(df):
    """
    Create a bar chart showing total sales by product.
    Works when Product and Sales columns are available.
    """

    if "Product" not in df.columns or "Sales" not in df.columns:
        return None

    sales = (
        df.groupby("Product")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )

    fig = px.bar(
        sales,
        x="Product",
        y="Sales",
        title="Sales by Product",
        labels={
            "Product": "Product",
            "Sales": "Total Sales"
        }
    )

    fig.update_layout(
        xaxis_tickangle=-45
    )

    return fig


def numerical_histogram(df, column):
    """
    Create a histogram for a numerical column.
    """

    if column not in df.columns:
        return None

    fig = px.histogram(
        df,
        x=column,
        title=f"Distribution of {column}",
        marginal="box"
    )

    return fig


def box_plot(df, column):
    """
    Create a box plot for a numerical column.
    Useful for detecting outliers.
    """

    if column not in df.columns:
        return None

    fig = px.box(
        df,
        y=column,
        title=f"Box Plot of {column}"
    )

    return fig


def correlation_heatmap(df):
    """
    Create a correlation heatmap for numerical columns.
    """

    numeric_df = df.select_dtypes(
        include="number"
    )

    if numeric_df.shape[1] < 2:
        return None

    correlation = numeric_df.corr()

    fig = px.imshow(
        correlation,
        text_auto=True,
        title="Correlation Heatmap",
        aspect="auto"
    )

    return fig


def scatter_plot(df, x_column, y_column):
    """
    Create a scatter plot between two numerical columns.
    """

    if (
        x_column not in df.columns
        or y_column not in df.columns
    ):
        return None

    fig = px.scatter(
        df,
        x=x_column,
        y=y_column,
        title=f"{x_column} vs {y_column}"
    )

    return fig