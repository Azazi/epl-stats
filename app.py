from Stat import Stat
from data_processor import (
    STAT_PROCESSOR_MAP,
    get_team_name,
    get_standings_table
)
from teams import FORMER_TEAM_NAME_MAP
from data_presenter import print_standings_for
from data_retriever import get_season_data

# Constants START_YEAR & END_YEAR refer to the earlies
# and latest season years (at the time).
# EXCLUDED is an array of years during which the EPL was
# suspended.
START_YEAR = 1888
END_YEAR = 2020
EXCLUDED = [1915, 1916, 1917, 1918, 1939, 1940, 1941, 1942, 1943, 1944, 1945]

# A dictionary to store the data for each EPL team.
TEAMS = {}


def process_season(start_year):
    # Get standings data table.
    raw_data = get_season_data(start_year, start_year + 1)
    standings_table = get_standings_table(raw_data)

    # Iterate through the table.
    for item in standings_table:
        team_name = FORMER_TEAM_NAME_MAP[get_team_name(item)]
        TEAMS.setdefault(team_name, {})

        for key in STAT_PROCESSOR_MAP:
            TEAMS[team_name][key] = \
                TEAMS[team_name].setdefault(key, 0) + \
                STAT_PROCESSOR_MAP[key](item)


for season in range(START_YEAR, END_YEAR):
    if season not in EXCLUDED:
        process_season(season)

print_standings_for(TEAMS, limit=10, stat=Stat.POINTS_ADJUSTED)
print_standings_for(TEAMS, limit=10, stat=Stat.POINTS)
