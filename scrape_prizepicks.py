import requests
import pandas as pd
import datetime
import os

# Map full stat names to NBA API abbreviations
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

    today = datetime.date.today()
    all_records = []

    for proj in projections:
        attr = proj["attributes"]
        stat_type = attr["stat_type"]
        line_score = attr["line_score"]
        is_main = attr.get("is_main", False)
        date_str = attr.get("starts_at", None)

        if date_str:
            try:
                game_datetime = datetime.datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                if game_datetime.date() != today:
                    continue
            except:
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
            "is_main": is_main
        })

    full_df = pd.DataFrame(all_records)

    # Retain all lines, but tag only one line per player+stat_type as the "official" for prediction
    keep_rows = []
    for (player, stat), group in full_df.groupby(['player', 'stat_type']):
        main = group[group['is_main'] == True]
        if not main.empty:
            keep_rows.append(main.iloc[0])
        else:
            keep_rows.append(group.sort_values("line_score").iloc[len(group)//2])

    main_df = pd.DataFrame(keep_rows)

    # Flag official lines in full dataset
    full_df["official"] = False
    for _, row in main_df.iterrows():
        mask = (
            (full_df["player"] == row["player"]) &
            (full_df["stat_type"] == row["stat_type"]) &
            (full_df["line_score"] == row["line_score"])
        )
        full_df.loc[mask, "official"] = True

    return full_df.drop(columns=["is_main"])

def save_props(df, output_dir="data/prizepicks_slates"):
    today = datetime.date.today().isoformat()
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"prizepicks_slate_{today}.csv")
    df.to_csv(output_path, index=False)
    print(f"✅ Saved prop slate to {output_path}")

if __name__ == "__main__":
    df = scrape_prizepicks()
    save_props(df)
