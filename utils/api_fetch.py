import requests
import pandas as pd

def fetch_pl_teams(api_key):
    url = "https://api.football-data.org/v4/competitions/PL/teams"
    headers = {"X-Auth-Token": api_key}
    r = requests.get(url, headers=headers)
    data = r.json()

    print("DEBUG API response for teams:", data)

    if "teams" not in data:
        print(f"Warning: 'teams' key missing. API returned: {data}")
        return []

    teams = [team["name"] for team in data["teams"]]
    return sorted(teams)

def fetch_2025_matches(api_key):
    url = "https://api.football-data.org/v4/competitions/PL/matches"
    headers = {"X-Auth-Token": api_key}
    r = requests.get(url, headers=headers)
    data = r.json()

    print("DEBUG API response for matches:", data)

    if "matches" not in data:
        print(f"Warning: 'matches' key missing. API returned: {data}")
        return pd.DataFrame()

    match_data = []
    for match in data["matches"]:
        match_data.append({
            "HomeTeam": match["homeTeam"]["name"],
            "AwayTeam": match["awayTeam"]["name"],
            "HomeGoals": match["score"]["fullTime"]["home"],
            "AwayGoals": match["score"]["fullTime"]["away"],
            "MatchDate": match["utcDate"]
        })
    return pd.DataFrame(match_data)
