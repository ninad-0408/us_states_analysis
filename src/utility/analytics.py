def yearwise_top_states(st, master_df):
    """
    Renders a bar chart displaying the top 10 states by health and prosperity index for a given year.

    Parameters
    ----------
    st : streamlit.State
        The Streamlit state object
    master_df : pandas.DataFrame
        The DataFrame containing all the data with columns 'State', 'ID Year' and 'health_and_prosperity_index'
    """
    st.header("Year Top States")

    year = st.selectbox("Year", sorted(list(set(master_df['ID Year'])), reverse=True))

    master_df = master_df[master_df['ID Year'] == year]
    master_df = master_df.sort_values(by='health_and_prosperity_index', ascending=False)[:10]

    st.bar_chart(master_df, x='State', y='health_and_prosperity_index')


def state_year_line_chart(st, master_df):
    """
    Renders a line chart displaying the health and prosperity index vs year for
    multiple states.

    Parameters
    ----------
    st : streamlit.State
        The Streamlit state object
    master_df : pandas.DataFrame
        The DataFrame containing all the data with columns 'State', 'ID Year' and
        'health_and_prosperity_index'
    """
    st.header("Year vs Health and Prosperity Index")

    col1, col2 = st.columns(2)
    with col1:
        states = st.multiselect("State", list(set(master_df['State'])))
    with col2:
        years = st.multiselect("Year", sorted(list(set(master_df['ID Year']))))
        select_all_years = st.checkbox("All Years")

    state_year_df = master_df[master_df['State'].isin(states)]
    if not select_all_years:
        state_year_df = state_year_df[state_year_df['ID Year'].isin(years)]

    st.line_chart(state_year_df, x='ID Year', y='health_and_prosperity_index', color="State")
