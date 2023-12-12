class EDA:
    def __init__(self) -> None:
        pass

    def virat_rename_columns(self, dataframe):
        """
        Rename columns in a DataFrame if they have not been renamed already.

        This function checks if the DataFrame columns match a predefined mapping of old column names to new,
        more descriptive column names. If the old names exist, they are renamed; if the DataFrame already
        has the new names, no action is taken.

        Parameters:
        dataframe (pd.DataFrame): The DataFrame whose columns may need to be renamed.

        Returns:
        pd.DataFrame: The DataFrame with potentially updated column names.
        """
        virat_columns_names = {
            "tt": "overview",
            "sp": "span",
            "mt": "matches",
            "in": "innings",
            "rn": "runs",
            "fo": "4s",
            "si": "6s",
            "ft": "50s",
            "hn": "100s",
            "bf": "balls_faced",
            "dk": "0s",
            "no": "not_out",
            "hs": "high_score",
            "bta": "average",
            "btsr": "strike_rate",
        }

        # Check if any of the old column names are in the DataFrame, and if so, rename them
        columns_to_rename = {
            old: new
            for old, new in virat_columns_names.items()
            if old in dataframe.columns
        }
        dataframe.rename(columns=columns_to_rename, inplace=True)

        return dataframe

    def bumrah_rename_columns(self, dataframe):
        """
        Rename columns in a DataFrame if they have not been renamed already.

        This function checks if the DataFrame columns match a predefined mapping of old column names to new,
        more descriptive column names. If the old names exist, they are renamed; if the DataFrame already
        has the new names, no action is taken.

        Parameters:
        dataframe (pd.DataFrame): The DataFrame whose columns may need to be renamed.

        Returns:
        pd.DataFrame: The DataFrame with potentially updated column names.
        """
        virat_columns_names = {
            "tt": "overview",
            "sp": "span",
            "mt": "matches",
            "in": "innings",
            "ov": "overs",
            "cd": "runs",
            "md": "maiden",
            "wk": "wickets",
            "fw": "5w",
            "tw": "10w",
            "bbi": "best_bowling_in_innings",
            "bbm": "best_bowling_in_match",
            "bwa": "average",
            "bwe": "economy",
            "bwsr": "strike_rate",
        }

        # Check if any of the old column names are in the DataFrame, and if so, rename them
        columns_to_rename = {
            old: new
            for old, new in virat_columns_names.items()
            if old in dataframe.columns
        }
        dataframe.rename(columns=columns_to_rename, inplace=True)

        return dataframe

    def remove_columns(self, dataframe):
        """
        Remove specified columns from a DataFrame permanently, if they exist.

        Parameters:
        dataframe (pd.DataFrame): The DataFrame from which columns are to be removed.

        Returns:
        pd.DataFrame: A DataFrame with the specified columns removed, if they were present.
        """

        columns_to_remove = ["pr", "fwk", "bl"]

        # Filter out any column names that do not exist in the DataFrame
        columns_to_remove = [
            column for column in columns_to_remove if column in dataframe.columns
        ]

        # Remove the columns that do exist in the DataFrame
        dataframe.drop(columns=columns_to_remove, inplace=True)
        # return dataframe
