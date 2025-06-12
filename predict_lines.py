from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
import pandas as pd
import time
import datetime
import os 

def get_avg_stat(player_name, stat='PTS', n=5):
    try:
        player = players.find_players_by_full_name(player_name)[0]
        pid = player["id"]
        log = playergamelog.PlayerGameLog(player_id=pid, season='2024-25', season_type_all_star='Playoffs')
        df = log.get_data_frames()[0]
        return df.sort_values('GAME_DATE')[stat].tail(n).mean()
    except:
        return None

def predict_edges(slate_csv, stat_filter='PTS', threshold=2.5):
    df = pd.read_csv(slate_csv)
    df = df[df['stat_type'] == stat_filter]

    picks = []
    for _, row in df.iterrows():
        player = row['player']
        line = float(row['line_score'])

        avg = get_avg_stat(player, stat_filter)
        time.sleep(0.5) 

        if avg is not None:
            edge = avg - line
            if abs(edge) > threshold:
                pick = "OVER" if edge > 0 else "UNDER"
                picks.append({
                    'player': player,
                    'line_score': line,
                    'predicted_avg': round(avg, 2),
                    'edge': round(edge, 2),
                    'pick': pick,
                    'abs_edge': abs(round(edge, 2))  
                })

    result_df = pd.DataFrame(picks)
    return result_df.sort_values(by='abs_edge', ascending=False).drop(columns='abs_edge')


def save_predictions(df, output_dir='predictions'):
    today = datetime.date.today().isoformat()
    output_path = os.path.join(output_dir, f"predictions_{today}.csv")
    df.to_csv(output_path, index=False)
    print(f"Saved recommended picks to: {output_path}")

if __name__ == "__main__":
    slate_path = "data/prizepicks_slates/prizepicks_slate_2025-06-12.csv"
    df = predict_edges(slate_path, stat_filter='PTS')
    save_predictions(df)
