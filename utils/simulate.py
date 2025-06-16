import pandas as pd
import numpy as np


def override_result(df, home_team, away_team, new_home_goals, new_away_goals):
    idx = df[(df['HomeTeam'] == home_team) & (df['AwayTeam'] == away_team)].index
    if not idx.empty:
        df.at[idx[0], 'HomeGoals'] = new_home_goals
        df.at[idx[0], 'AwayGoals'] = new_away_goals
    return df


def recalculate_table(df):
    teams = sorted(set(df['HomeTeam']).union(df['AwayTeam']))
    table = {team: {"Pts": 0, "GF": 0, "GA": 0} for team in teams}


    for _, row in df.iterrows():
        h, a, hg, ag = row['HomeTeam'], row['AwayTeam'], row['HomeGoals'], row['AwayGoals']
        table[h]['GF'] += hg
        table[h]['GA'] += ag
        table[a]['GF'] += ag
        table[a]['GA'] += hg


        if hg > ag:
            table[h]['Pts'] += 3
        elif hg < ag:
            table[a]['Pts'] += 3
        else:
            table[h]['Pts'] += 1
            table[a]['Pts'] += 1


    table_df = pd.DataFrame([
        {"Team": t, "Points": v["Pts"], "GF": v["GF"], "GA": v["GA"], "GD": v["GF"] - v["GA"]}
        for t, v in table.items()
    ])
    return table_df.sort_values(by=["Points", "GD", "GF"], ascending=False).reset_index(drop=True)


def simulate_all_matches(teams, past_table):
    simulated_data = []


    # Normalize strength based on 2025 points
    strength = {}
    max_points = past_table["Points"].max()
    for _, row in past_table.iterrows():
        strength[row["Team"]] = row["Points"] / max_points


    for home in teams:
        for away in teams:
            if home != away:
                home_strength = strength.get(home, 0.5)
                away_strength = strength.get(away, 0.5)


                # Add home advantage
                home_strength += 0.05


                # Simulate goals using Poisson distributions
                avg_home_goals = 1.5 * (home_strength / (home_strength + away_strength))
                avg_away_goals = 1.2 * (away_strength / (home_strength + away_strength))


                hg = np.random.poisson(avg_home_goals * 2)
                ag = np.random.poisson(avg_away_goals * 2)


                simulated_data.append({
                    "HomeTeam": home,
                    "AwayTeam": away,
                    "HomeGoals": hg,
                    "AwayGoals": ag,
                    "MatchDate": "2026-05-01"
                })


    return pd.DataFrame(simulated_data)
