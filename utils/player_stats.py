from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
import pandas as pd

def get_player_id(player_name):
    try:
        return players.find_players_by_full_name(player_name)[0]['id']
    except IndexError:
        return None

def get_last5_and_season_avg(player_name, stat='PTS'):
    pid = get_player_id(player_name)
    if pid is None: return None, None

    try:
        log = playergamelog.PlayerGameLog(player_id=pid, season='2024-25', season_type_all_star='Playoffs')
        df = log.get_data_frames()[0].sort_values('GAME_DATE')
        return df[stat].tail(5).mean(), df[stat].mean()
    except:
        return None, None
