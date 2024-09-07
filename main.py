import pandas as pd
import streamlit as st
from apscheduler.schedulers.background import BackgroundScheduler

from src.constants import INTERVAL_HOUR
from src.cron.update_data import refresh_data
from src.utility.analytics import yearwise_top_states, state_year_line_chart


def get_refresh_scheduler(interval_hours):
    """
    Creates a BackgroundScheduler that calls refresh_data every interval_hours and returns it.

    Parameters
    ----------
    interval_hours : int
        The number of hours between each call to refresh_data

    Returns
    -------
    apscheduler.schedulers.background.BackgroundScheduler
        The scheduler that calls refresh_data every interval_hours
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=refresh_data, name='refresh_data', trigger='interval', hours=interval_hours,
                      id='refresh_data')
    return scheduler


def render_app(with_scheduler):
    """
    Renders the Streamlit app that displays the yearwise top 10 states by health and prosperity index
    and a line chart displaying the health and prosperity index vs year for multiple states.

    Parameters
    ----------
    with_scheduler : bool
        Whether to refresh the data every INTERVAL_HOUR hours
    """
    if with_scheduler:
        refresh_scheduler = get_refresh_scheduler(INTERVAL_HOUR)
        refresh_scheduler.start()

    st.title('Health and Prosperity Index')

    master_df = pd.read_csv('./master_index_data.csv')

    yearwise_top_states(st, master_df)
    state_year_line_chart(st, master_df)


if __name__ == "__main__":
    render_app(False)
