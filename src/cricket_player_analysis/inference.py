import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Inference:
    def __init__(self) -> None:
        pass

    def plot_average_vs_team(
        self, df, column_teams, column_average, figsize=(12, 5), rotation_angle=45
    ):
        """
        Creates a bar chart of a cricketer's average runs against different teams.

        Parameters:
        df : pandas.DataFrame
            The DataFrame containing the cricket statistics.
        column_teams : str
            The name of the column in the DataFrame that contains team names.
        column_average : str
            The name of the column in the DataFrame that contains the average runs.
        figsize : tuple, optional
            A tuple defining the figure size (width, height) in inches. Default is (12, 5).
        rotation_angle : int, optional
            The angle of rotation for the x-axis labels. Default is 45 degrees.

        Returns:
        matplotlib.figure.Figure
            The Figure object for the plot.
        """
        # Create a figure with the specified figure size
        fig, ax = plt.subplots(figsize=figsize)

        # Create a bar plot
        ax.bar(df[column_teams], df[column_average], color="skyblue")

        # Set the title and labels of the plot
        ax.set_xlabel("Team")
        ax.set_ylabel(column_average)

        # Rotate the x-axis labels for better readability
        ax.tick_params(axis="x", rotation=rotation_angle)

    def plot_player_performance(
        self,
        df,
        year_col="overview",
        avg_col="average",
        sr_col="strike_rate",
        figsize=(10, 5),
    ):
        """
        Plots the evolution of a cricketer's batting average and strike rate over time.

        This function takes a DataFrame containing years and corresponding performance metrics,
        and plots a line chart showing trends in batting average and strike rate.

        Parameters:
        - df (DataFrame): The DataFrame containing the performance data.
        - year_col (str): The name of the column in df that contains the years.
        - avg_col (str): The name of the column in df that contains the batting averages.
        - sr_col (str): The name of the column in df that contains the strike rates.
        - figsize (tuple): The size of the figure to be plotted (width, height).

        Returns:
        - plt (Plot): The plot object with the performance trends.
        """

        # Ensure correct types for plotting
        df[year_col] = df[year_col].astype(str)

        # Create a figure and a set of subplots
        plt.figure(figsize=figsize)

        # Plot batting average
        plt.plot(df[year_col], df[avg_col], label="Average", marker="o", color="blue")

        # Plot strike rate
        plt.plot(df[year_col], df[sr_col], label="Strike Rate", marker="s", color="red")

        # Title and labels
        plt.title("Evolution of Average and Strike Rate")
        plt.xlabel("Years")
        plt.ylabel("Metrics")
        plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
        plt.legend()  # Show legend

        # Show grid
        plt.grid(True)

        # Show the plot
        plt.tight_layout()  # Adjust the padding between and around subplots
        plt.show()  # Display the plot
