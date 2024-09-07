import logging

import pandas as pd
import requests

from src.constants import API_URL


def fetch_data_convert_to_df(query):
    """
    Fetches data from the DataUSA API and converts it to a pandas DataFrame.

    Parameters
    ----------
    query : dict
        The query parameters to be passed to the DataUSA API.

    Returns
    -------
    pandas.DataFrame
        The JSON response from the API converted to a pandas DataFrame.

    Raises
    ------
    Exception
        If the request to the API fails for any reason.
    """
    
    try:
        response = requests.get(API_URL, params=query)
        response.raise_for_status()
        response_data_json = response.json()
        return pd.DataFrame(response_data_json['data'])
    except Exception as err:
        logging.error(f'Data fetch failed for params = {query}', err)

