from bs4 import BeautifulSoup

from Stat import Stat


def _get_team_stat(row, index=0, cast=int, sep=':', sep_pos=0):
    return int(row.find_all('td')[index].text.split(sep)[sep_pos])


def _get_team_played(row):
    return _get_team_stat(row, index=3)


def _get_team_won(row):
    return _get_team_stat(row, index=4)


def _get_team_draw(row):
    return _get_team_stat(row, index=5)


def _get_team_lost(row):
    return _get_team_stat(row, index=6)


def _get_team_goals_for(row):
    return _get_team_stat(row, index=7, sep_pos=0)


def _get_team_goals_against(row):
    return _get_team_stat(row, index=7, sep_pos=1)


def _get_team_goals_diff(row):
    return _get_team_stat(row, index=8)


def _get_team_points(row):
    return _get_team_stat(row, index=9, sep_pos=0)


def _get_team_points_adjusted(row):
    return (_get_team_won(row) * 3) + _get_team_draw(row)


def get_standings_table(raw_data):
    soup_data = BeautifulSoup(raw_data, 'html.parser')

    # Get standings table.
    raw_table = soup_data.find_all(
        'table',
        attrs={'class': 'standard_tabelle'}
    )[1]
    
    # Extract the data rows from the raw table.
    return raw_table.find_all('tr')[1:]


def get_team_name(row):
    return row.find('a')['title']


STAT_PROCESSOR_MAP = {
    Stat.PLAYED: _get_team_played,
    Stat.WON: _get_team_won,
    Stat.DRAW: _get_team_draw,
    Stat.LOST: _get_team_lost,
    Stat.GOALS_FOR: _get_team_goals_for,
    Stat.GOALS_AGAINST: _get_team_goals_against,
    Stat.GOAL_DIFF: _get_team_goals_diff,
    Stat.POINTS: _get_team_points,
    Stat.POINTS_ADJUSTED: _get_team_points_adjusted
}
