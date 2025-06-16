# Premier League 2026 Predictor README File

App Description: 

This app predicts the 2026 Premier League standings based on the 2025 season results using live data from the [Football-Data.org API](https://www.football-data.org/). Users can simulate, override, and visualize match results to see how changes affect the final table.

# Features

- ✅ View the current 2025 Premier League table (live API)
- ✅ Simulate outcomes of 2026 matches based on team stats from 2025
- ✅ Override match scores manually to see new predictions
- ✅ Dynamic point calculation (Win = 3, Draw = 1, Loss = 0)
- ✅ Automatically updates standings, goals for/against, and goal difference
- ✅ Bar charts to visualize team performance
- ✅ AI-informed predictions using past performance and goal trends
- ✅ User-friendly UI built with Streamlit

## How It Works

1. **Data Fetching**: Pulls live team and match data from the 2025 season via API.
2. **Simulation Engine**: Predicts 2026 results based on goals scored, conceded, and final standings from 2025.
3. **Table Calculation**: Calculates points and ranks teams using official Premier League rules.
4. **Visualization**: Uses Altair to generate bar charts showing predicted points and team performance.

## Tech Stack

- Python
- Streamlit
- Pandas
- Altair
- Football-Data.org API