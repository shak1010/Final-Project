import streamlit as st
from utils.api_fetch import fetch_pl_teams, fetch_2025_matches
from utils.simulate import override_result, recalculate_table, simulate_all_matches
from utils.visualize import plot_points_bar_chart

st.set_page_config(page_title="PL 2026 Predictor", layout="wide")
st.title("🏆 Premier League Table Predictor")

API_KEY = st.secrets["API_KEY"]

with st.expander("ℹ️ How This Works"):
    st.markdown("""
    - **Live 2025 Data**: Pulled from [Football-Data.org](https://www.football-data.org/).
    - **2026 Simulation**: Based on 2025 team performance, using weighted probabilities and home advantage.
    - **Manual Override**: You can tweak match results to see the impact on the standings.
    """)

@st.cache_data
def load_real_data():
    matches_df = fetch_2025_matches(API_KEY)
    teams = fetch_pl_teams(API_KEY)
    return matches_df, teams

# Radio toggle to choose between 2025 and predicted 2026
mode = st.radio("Select data mode:", ["2025 Real Results", "2026 Predicted Season"])

if mode == "2025 Real Results":
    matches_df, teams = load_real_data()
else:
    # Load 2025 to base predictions on
    past_df, teams = load_real_data()
    past_table = recalculate_table(past_df)
    matches_df = simulate_all_matches(teams, past_table)

# Sidebar override
st.sidebar.header("🔧 Override a Match Result")
home = st.sidebar.selectbox("Home Team", teams)
away = st.sidebar.selectbox("Away Team", [t for t in teams if t != home])
hg = st.sidebar.number_input("Home Goals", 0, 10, 1)
ag = st.sidebar.number_input("Away Goals", 0, 10, 0)

if st.sidebar.button("Update Match Result"):
    matches_df = override_result(matches_df, home, away, hg, ag)

# Output table
st.subheader(f"📊 {'2025 Table' if mode == '2025 Real Results' else 'Predicted 2026 Table'}")
predicted_table = recalculate_table(matches_df)
st.dataframe(predicted_table, use_container_width=True)
plot_points_bar_chart(predicted_table)
