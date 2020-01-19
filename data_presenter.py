from texttable import Texttable

from Stat import Stat

CELL_WIDTH = 120
NAME_LABEL = 'NAME'
TABLE_TITLE = 'EPL HISTORICAL STANDINGS ({})'


def _sort_teams(teams, stat, reverse):
    return sorted(teams, key=lambda x: (teams[x][stat]), reverse=reverse)


def _setup_table():
    table = Texttable(max_width=CELL_WIDTH)
    table.add_row([
        NAME_LABEL,
        Stat.PLAYED.value,
        Stat.WON.value,
        Stat.DRAW.value,
        Stat.LOST.value,
        Stat.GOALS_FOR.value,
        Stat.GOALS_AGAINST.value,
        Stat.POINTS.value,
        Stat.POINTS_ADJUSTED.value,
    ])
    return table


def print_standings_for(teams, limit, reverse=True, stat=Stat.POINTS_ADJUSTED):
    sorted_teams = _sort_teams(teams, stat, reverse)[0:limit]
    table = _setup_table()

    for team in sorted_teams:
        table.add_row([
            team,
            teams[team][Stat.PLAYED],
            teams[team][Stat.WON],
            teams[team][Stat.DRAW],
            teams[team][Stat.LOST],
            teams[team][Stat.GOALS_FOR],
            teams[team][Stat.GOALS_AGAINST],
            teams[team][Stat.POINTS],
            teams[team][Stat.POINTS_ADJUSTED]
        ])

    print()
    print(TABLE_TITLE.format(stat.value))
    print(table.draw())
