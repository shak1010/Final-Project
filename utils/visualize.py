# utils/visualize.py
import altair as alt
import streamlit as st


def plot_points_bar_chart(table_df):
    chart = alt.Chart(table_df).mark_bar().encode(
        x=alt.X('Points:Q', sort='-x'),
        y=alt.Y('Team:N', sort='-x'),
        color='Points:Q',
        tooltip=['Team', 'Points', 'GF', 'GA', 'GD']
    ).properties(width=600, height=400)


    st.altair_chart(chart, use_container_width=True)


