import pandas as pd


def load_data(file):
    """
    Load a CSV file into a pandas DataFrame.
    """

    try:
        df = pd.read_csv(file)

        if df.empty:
            raise ValueError(
                "The uploaded CSV file is empty."
            )

        return df

    except pd.errors.EmptyDataError:
        raise ValueError(
            "The uploaded CSV file is empty."
        )

    except pd.errors.ParserError:
        raise ValueError(
            "Unable to read this CSV file. "
            "Please check that the file is a valid CSV."
        )

    except Exception as e:
        raise ValueError(
            f"Unable to load the CSV file: {str(e)}"
        )


def get_dataset_info(df):
    """
    Return basic information about the dataset.
    """

    return {
        "rows": len(df),

        "columns": len(df.columns),

        "column_names": list(
            df.columns
        ),

        "missing_values": (
            df.isnull()
            .sum()
            .to_dict()
        ),

        "data_types": (
            df.dtypes
            .astype(str)
            .to_dict()
        )
    }


def get_basic_statistics(df):
    """
    Generate descriptive statistics.
    """

    try:

        return df.describe(
            include="all"
        )

    except Exception:

        # Fallback for unusual datasets
        return df.describe()