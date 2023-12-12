"""
This module provides a class 'DataSummary' for fetching and processing cricket player statistics. 
The class contains methods for retrieving player stats from the ESPN Cricinfo API, creating pandas 
DataFrames from JSON data, removing unwanted columns from DataFrames, and creating global variables 
for DataFrames with specified prefixes.

Classes:
    DataSummary: Offers methods to fetch and process cricket player statistics.

Methods:
    fetch_player_stats: Fetches a player's stats summary from the ESPN Cricinfo API.
    create_dataframes_from_json: Creates a dictionary of DataFrames from JSON data.
    remove_columns: Removes specified columns from a DataFrame.
    create_prefixed_global_dataframes: Creates global variables for DataFrames with prefixed names.
"""

import requests
import json
import pandas as pd
import numpy as np


class DataSummary:
    """
    The DataSummary class provides functionalities for fetching and processing cricket player statistics.

    It facilitates interaction with the ESPN Cricinfo API to retrieve statistical data of cricket players.
    The class also includes methods to manipulate and organize this data into structured formats such as
    pandas DataFrames, making it easier to perform data analysis tasks.

    Methods include fetching player statistics, creating DataFrames from JSON data, removing unnecessary
    DataFrame columns, and creating global DataFrames with specific naming conventions.
    """

    def __init__(self) -> None:
        """
        Initializes the DataSummary class. This class is designed to handle various tasks related to data retrieval
        and processing of cricket player statistics.
        """
        pass

    def fetch_player_stats(self, player_id, record_class_id, stat_type):
        """
        Fetch a cricket player's stats summary from ESPN Cricinfo API.

        Parameters:
        player_id (int): Unique identifier for the player.
        record_class_id (int): Identifier for the class of record (e.g., Test, ODI).
        stat_type (str): Type of statistics to retrieve (e.g., 'BATTING', 'BOWLING').

        Returns:
        dict: A dictionary containing the player's stats summary.
        """

        # Construct the URL with the provided parameters
        url = f"https://hs-consumer-api.espncricinfo.com/v1/pages/player/stats/summary?playerId={player_id}&recordClassId={record_class_id}&type={stat_type}"

        # Make the HTTP GET request to the API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response body
            stats_summary = json.loads(response.text)
            return stats_summary
        else:
            # Return an error message if something went wrong with the request
            return f"Error: Received status code {response.status_code}"

    def create_dataframes_from_json(self, json_data):
        """
        Create a dictionary of pandas DataFrames from a JSON object that contains cricket statistics.

        Parameters:
        json_data (dict): A JSON object containing the player's statistics grouped under 'summary' and 'groups'.
        dataframes_names (list): A list of keys representing the names for each DataFrame corresponding to each group of statistics in the JSON object.

        Returns:
        dict: A dictionary where keys are the names of the dataframes and values are the corresponding DataFrames created from the JSON data.
        """
        df_dic = {}
        dataframes_names = [
            "df_career_averages",
            "df_in_format",
            "df_vs_team",
            "df_in_host_country",
            "df_in_continent",
            "df_home_vs_away",
            "df_by_year",
            "df_by_season",
            "df_captains_involved",
            "df_is_not_captain",
            "df_is_not_keeper",
            "df_toss",
            "df_toss_and_batting_sequence",
            "df_batting_first_vs_fielding_first",
            "df_in_team_innings",
            "df_in_match_innings",
            "df_in_match_type",
            "df_match_result",
            "df_result_and_batting_sequence",
            "df_in_tournament_type",
            "df_in_match_number_per_series",
            "df_in_major_trophies",
            "df_in_finals",
            "df_position",
        ]

        # Iterate over each group of statistics in the JSON data
        for i, group in enumerate(json_data["summary"]["groups"]):
            # Assign a new DataFrame to the corresponding entry in the dictionary
            # Use the list of dataframe names provided as keys
            if i < len(dataframes_names):
                df_dic[dataframes_names[i]] = pd.DataFrame(group["stats"])
            else:
                # Handle cases where there are more groups than names provided
                df_dic[f"unnamed_dataframe_{i}"] = pd.DataFrame(group["stats"])

        return df_dic

    def remove_columns(self, dataframe, columns_to_remove):
        """
        Remove specified columns from a DataFrame permanently, if they exist.

        Parameters:
        dataframe (pd.DataFrame): The DataFrame from which columns are to be removed.
        columns_to_remove (list): A list of column names to be removed from the DataFrame.

        Returns:
        pd.DataFrame: A DataFrame with the specified columns removed, if they were present.
        """
        # Filter out any column names that do not exist in the DataFrame
        columns_to_remove = [
            column for column in columns_to_remove if column in dataframe.columns
        ]

        # Remove the columns that do exist in the DataFrame
        dataframe.drop(columns=columns_to_remove, inplace=True)
        return dataframe

    def create_prefixed_global_dataframes(self, df_dic, prefix):
        """
        Create global variables for each DataFrame in a dictionary, with a specified prefix added to the names.

        This function takes each key-value pair in the `df_dic` dictionary, prefixes the key with `prefix`,
        and then creates a global variable with that new name pointing to the value (DataFrame). This is
        useful when you have a large number of DataFrames that you want to access by name without the
        dictionary syntax.

        Parameters:
        df_dic (dict): A dictionary where keys are the original names of the DataFrames.
        prefix (str): A string that will be prefixed to each key to create the global variable names.

        Returns:
        None
        """
        for key, value in df_dic.items():
            # Create a new global variable for each DataFrame
            globals()[prefix + key] = value.copy()
