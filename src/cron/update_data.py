import pandas as pd

from src.utility.metrics_utility import CONSIDERED_METRICS, TOTAL_POPULATION, POPULATION_METRICS, NEGATION_METRICS
from src.utility.utilities import fetch_data_convert_to_df


def fetch_and_clean_data(metric):
    """
    Fetches data from DataUSA API based on metric['params'], cleans the data and returns a
    pandas DataFrame. The DataFrame is indexed by ['ID State', 'State', 'ID Year'] and has a
    single column with the name metric['name'].

    Parameters
    ----------
    metric : dict
        A dictionary containing the parameters for the DataUSA API request and the name for
        the column in the returned DataFrame.

    Returns
    -------
    pandas.DataFrame
        A pandas DataFrame with the cleaned data.
    """
    raw_data_df = fetch_data_convert_to_df(metric['params'])

    if len(raw_data_df):
        raw_data_df = raw_data_df[raw_data_df['ID State'] != "#null"]
        raw_data_df = raw_data_df.set_index(['ID State', 'State', 'ID Year']).rename(
            columns=({metric['params']['measure']: metric['name']}))[[metric['name']]]

    return raw_data_df


def population_percentage_calculation(master_data_df):
    """
    Calculates the percentage of the population for the given metrics.

    Parameters
    ----------
    master_data_df : pandas.DataFrame
        The DataFrame containing all the data with columns 'State', 'ID Year' and 'total_population'

    Returns
    -------
    pandas.DataFrame
        The DataFrame with the population percentages calculated.
    """
    for metric in POPULATION_METRICS:
        master_data_df[metric['name']] = master_data_df[metric['name']] / master_data_df['total_population']

    return master_data_df


def preprocess_data(master_data_df):
    """
    Preprocesses the master data DataFrame by filling NaNs with the mean of the respective column, negating the values of the metrics in NEGATION_METRICS, calculating the population percentages, normalizing the values to the range [0, 1], and resetting the index.

    Parameters
    ----------
    master_data_df : pandas.DataFrame
        The DataFrame containing all the data with columns 'State', 'ID Year' and the metrics in CONSIDERED_METRICS

    Returns
    -------
    pandas.DataFrame
        The preprocessed DataFrame
    """
    master_data_df = master_data_df.fillna(master_data_df.mean())

    for metric in NEGATION_METRICS:
        master_data_df[metric['name']] = -1 * master_data_df[metric['name']]

    master_data_df = population_percentage_calculation(master_data_df)

    master_data_df = (master_data_df - master_data_df.min()) / (master_data_df.max() - master_data_df.min())

    master_data_df.reset_index(inplace=True)

    return master_data_df


def calculate_index(master_data_df, considered_metrics, index_name):
    """
    Calculates a weighted average of the given metrics and assigns it to a new
    column in the DataFrame.

    Parameters
    ----------
    master_data_df : pandas.DataFrame
        The DataFrame containing all the data with columns 'State', 'ID Year' and
        the metrics in CONSIDERED_METRICS
    considered_metrics : list
        A list of dictionaries containing the metric configuration and weight
    index_name : str
        The name of the new column to be created

    Returns
    -------
    pandas.DataFrame
        The DataFrame with the new column added
    """

    total_weight = sum([metric['weight'] for metric in considered_metrics])

    master_data_df[index_name] = [0] * len(master_data_df)

    for metric in considered_metrics:
        master_data_df[index_name] += master_data_df[metric['config']['name']] * metric['weight']

    master_data_df[index_name] = master_data_df[index_name] / total_weight

    return master_data_df


def refresh_data():
    """
    Fetches and cleans data from the DataUSA API, preprocesses it and calculates a
    health and prosperity index. The data is then saved to a CSV file.

    The data fetched includes the total population and the metrics in
    CONSIDERED_METRICS. The data is then preprocessed by filling NaNs with the mean
    of the respective column, negating the values of the metrics in NEGATION_METRICS,
    calculating the population percentages, normalizing the values to the range [0, 1],
    and resetting the index. The health and prosperity index is then calculated as a
    weighted average of the metrics in CONSIDERED_METRICS and assigned to a new column
    named 'health_and_prosperity_index'.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    master_data_df = fetch_and_clean_data(TOTAL_POPULATION)

    for metric in CONSIDERED_METRICS:
        master_data_df = pd.merge(left=master_data_df, right=fetch_and_clean_data(metric['config']), left_index=True,
                                  right_index=True, how='left')

    master_data_df = preprocess_data(master_data_df)

    master_data_df = calculate_index(master_data_df, CONSIDERED_METRICS, 'health_and_prosperity_index')

    master_data_df.to_csv('../../master_index_data.csv', index=False)


if __name__ == "__main__":
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    refresh_data()
