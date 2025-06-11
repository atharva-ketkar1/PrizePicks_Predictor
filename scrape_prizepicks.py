import requests
import pandas as pd
import datetime
import os

STAT_ABBREVIATIONS = {
    "Points": "PTS",
    "Rebounds": "REB",
    "Assists": "AST"
}

def scrape_prizepicks():
    url = "https://api.prizepicks.com/projections"
    params = {
        "league_id": "7",
        "per_page": "250"
    }
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    projections = data["data"]
    included = {item["id"]: item for item in data["included"]}

    all_records = []

    for proj in projections:
        attr = proj["attributes"]
        stat_type = attr["stat_type"]
        line_score = attr["line_score"]
        odds_type = attr.get("odds_type", "none")

        if odds_type != "standard":
            continue

        player_id = str(proj["relationships"]["new_player"]["data"]["id"])
        player_info = included.get(player_id, {}).get("attributes", {})
        name = player_info.get("name", "Unknown")
        team = player_info.get("team", "Unknown")

        mapped_stat_type = STAT_ABBREVIATIONS.get(stat_type, stat_type)

        all_records.append({
            "player": name,
            "team": team,
            "stat_type": mapped_stat_type,
            "line_score": line_score,
        })

    return pd.DataFrame(all_records)

def save_props(df, output_dir="data/prizepicks_slates"):
    today = datetime.date.today().isoformat()
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"prizepicks_slate_{today}.csv")
    df.to_csv(output_path, index=False)
    print(f"Saved prop slate to {output_path}")

if __name__ == "__main__":
    df = scrape_prizepicks()
    save_props(df)
