from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
import pandas as pd
import datetime, time, os

def fetch_player_log(player_name):
    try:
        player = players.find_players_by_full_name(player_name)[0]
        pid = player['id']
        log = playergamelog.PlayerGameLog(player_id=pid, season='2024-25', season_type_all_star='Playoffs')
        df = log.get_data_frames()[0]
        return df.sort_values('GAME_DATE')
    except:
        return None

def extract_features(df, stat):
    df = df.head(10)
    return {
        f'{stat}_avg_3': df[stat].head(3).mean(),
        f'{stat}_avg_5': df[stat].head(5).mean(),
        f'{stat}_avg_10': df[stat].mean(),
        'minutes_avg': df['MIN'].mean(),
        'home_avg': df[df['MATCHUP'].str.contains('vs')][stat].mean(),
        'away_avg': df[df['MATCHUP'].str.contains('@')][stat].mean(),
    }

def predict_edges(slate_csv, stat_types=['PTS', 'REB', 'AST'], threshold=2.5):
    df = pd.read_csv(slate_csv)
    all_picks = []

    for stat_filter in stat_types:
        filtered_df = df[df['stat_type'] == stat_filter]

        for _, row in filtered_df.iterrows():
            player = row['player']
            line = float(row['line_score'])

            gamelog = fetch_player_log(player)
            if gamelog is None or len(gamelog) < 5:
                continue

            features = extract_features(gamelog, stat_filter)
            predicted_avg = features[f'{stat_filter}_avg_5']
            edge = predicted_avg - line
            time.sleep(0.6)

            if abs(edge) > threshold:
                pick = 'OVER' if edge > 0 else 'UNDER'

                result_row = {
                    'player': player,
                    'stat_type': stat_filter,
                    'line_score': line,
                    'predicted_avg': round(predicted_avg, 2),
                    'edge': round(edge, 2),
                    'pick': pick,
                    'minutes_avg': round(features['minutes_avg'], 2),
                    'home_avg': round(features['home_avg'], 2),
                    'away_avg': round(features['away_avg'], 2),
                }

                # Add stat-specific averages
                for key, val in features.items():
                    if stat_filter in key:
                        result_row[key] = round(val, 2)

                all_picks.append(result_row)

    return pd.DataFrame(all_picks)

def save_predictions(df, output_dir='predictions'):
    today = datetime.date.today().isoformat()
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"predictions_{today}_v2.csv")
    df.to_csv(output_path, index=False)
    print(f"Saved predictions to: {output_path}")

if __name__ == "__main__":
    slate_path = "data/prizepicks_slates/prizepicks_slate_2025-06-12.csv"
    df = predict_edges(slate_path, stat_types=['PTS', 'REB', 'AST'])
    save_predictions(df)
