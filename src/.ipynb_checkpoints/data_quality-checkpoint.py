import pandas as pd


def missing_summary(df):
    """
    Return missing-value counts and percentages.
    """
    return (
        pd.DataFrame(
            {
                "missing_count": df.isna().sum(),
                "missing_pct": df.isna().mean() * 100,
            }
        )
        .sort_values("missing_pct", ascending=False)
    )


def duplicate_count(df, subset=None):
    """
    Return the number of duplicate rows.

    Parameters
    ----------
    df : pandas.DataFrame
    subset : list or None
        Columns to use when identifying duplicates.
    """
    return df.duplicated(subset=subset).sum()


def foreign_key_check(
    child_df,
    child_column,
    parent_df,
    parent_column,
):
    """
    Identify values in child_column that do not exist
    in the parent table.
    """

    child_values = set(child_df[child_column].dropna())
    parent_values = set(parent_df[parent_column].dropna())

    return sorted(child_values - parent_values)


def date_range_summary(df, date_column):
    """
    Return minimum and maximum dates for a column.
    """
    return {
        "min_date": df[date_column].min(),
        "max_date": df[date_column].max(),
    }