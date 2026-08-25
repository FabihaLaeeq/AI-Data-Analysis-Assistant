import pandas as pd


def answer_question(df, question):

    if not question or not question.strip():
        return "Please enter a question."

    q = question.lower().strip()

    # -------------------------------------------------
    # DATASET SIZE
    # -------------------------------------------------

    if (
        "how many rows" in q
        or "number of rows" in q
        or "how many records" in q
        or "number of records" in q
    ):
        return f"The dataset contains {len(df)} rows."


    if (
        "how many columns" in q
        or "number of columns" in q
    ):
        return f"The dataset contains {len(df.columns)} columns."


    # -------------------------------------------------
    # MISSING VALUES
    # -------------------------------------------------

    if (
        "missing values" in q
        or "missing data" in q
        or "null values" in q
    ):

        total_missing = int(
            df.isnull().sum().sum()
        )

        return (
            f"The dataset contains "
            f"{total_missing} missing values in total."
        )


    # -------------------------------------------------
    # DUPLICATES
    # -------------------------------------------------

    if (
        "duplicate" in q
        or "duplicates" in q
    ):

        duplicates = int(
            df.duplicated().sum()
        )

        return (
            f"The dataset contains "
            f"{duplicates} duplicate rows."
        )


    # -------------------------------------------------
    # HIGHEST SALES
    # -------------------------------------------------

    if (
        "highest sales" in q
        or "highest sale" in q
        or "best selling product" in q
        or "top selling product" in q
        or "best product" in q
    ):

        if "Sales" not in df.columns:
            return (
                "The dataset does not contain "
                "a Sales column."
            )

        if "Product" not in df.columns:
            return (
                "The dataset does not contain "
                "a Product column."
            )

        try:

            sales = pd.to_numeric(
                df["Sales"],
                errors="coerce"
            )

            index = sales.idxmax()

            product = df.loc[
                index,
                "Product"
            ]

            value = sales.loc[index]

            return (
                f"{product} generated the highest "
                f"sales with a value of {value:.2f}."
            )

        except Exception:

            return (
                "I could not calculate the "
                "highest sales."
            )


    # -------------------------------------------------
    # TOTAL SALES
    # -------------------------------------------------

    if (
        "total sales" in q
        or "overall sales" in q
    ):

        if "Sales" not in df.columns:
            return (
                "The dataset does not contain "
                "a Sales column."
            )

        sales = pd.to_numeric(
            df["Sales"],
            errors="coerce"
        )

        total = sales.sum()

        return (
            f"The total sales are {total:.2f}."
        )


    # -------------------------------------------------
    # AVERAGE SALES
    # -------------------------------------------------

    if (
        "average sales" in q
        or "mean sales" in q
    ):

        if "Sales" not in df.columns:
            return (
                "The dataset does not contain "
                "a Sales column."
            )

        sales = pd.to_numeric(
            df["Sales"],
            errors="coerce"
        )

        average = sales.mean()

        return (
            f"The average sales value is "
            f"{average:.2f}."
        )


    # -------------------------------------------------
    # AVERAGE AGE
    # -------------------------------------------------

    if (
        "average age" in q
        or "mean age" in q
    ):

        if "Customer_Age" not in df.columns:
            return (
                "The dataset does not contain "
                "a Customer_Age column."
            )

        age = pd.to_numeric(
            df["Customer_Age"],
            errors="coerce"
        )

        average_age = age.mean()

        return (
            f"The average customer age is "
            f"{average_age:.2f} years."
        )


    # -------------------------------------------------
    # MOST ORDERS BY CITY
    # -------------------------------------------------

    if (
        "most orders" in q
        or "most customers" in q
        or "top city" in q
        or "most popular city" in q
    ):

        if "City" not in df.columns:
            return (
                "The dataset does not contain "
                "a City column."
            )

        counts = df["City"].value_counts()

        city = counts.idxmax()
        count = counts.max()

        return (
            f"{city} has the highest number "
            f"of records with {count}."
        )


    # -------------------------------------------------
    # MOST FREQUENT CATEGORY
    # -------------------------------------------------

    if (
        "most frequent category" in q
        or "most common category" in q
        or "popular category" in q
        or "most common product category" in q
    ):

        if "Category" not in df.columns:
            return (
                "The dataset does not contain "
                "a Category column."
            )

        counts = df["Category"].value_counts()

        category = counts.idxmax()
        count = counts.max()

        return (
            f"{category} is the most frequent "
            f"category with {count} records."
        )


    # -------------------------------------------------
    # COLUMN NAMES
    # -------------------------------------------------

    if (
        "what columns" in q
        or "column names" in q
        or "list columns" in q
    ):

        columns = ", ".join(
            df.columns.astype(str)
        )

        return (
            f"The dataset contains these columns: "
            f"{columns}"
        )


    # -------------------------------------------------
    # NUMERICAL COLUMNS
    # -------------------------------------------------

    if (
        "numerical columns" in q
        or "numeric columns" in q
    ):

        numeric_columns = (
            df.select_dtypes(
                include="number"
            )
            .columns
            .tolist()
        )

        if not numeric_columns:
            return (
                "The dataset does not contain "
                "numerical columns."
            )

        return (
            "The numerical columns are: "
            + ", ".join(numeric_columns)
        )


    # -------------------------------------------------
    # FALLBACK
    # -------------------------------------------------

    return (
        "I could not answer that question from "
        "the current dataset. Try asking about "
        "sales, products, categories, cities, "
        "rows, columns, missing values, duplicates, "
        "or average age."
    )