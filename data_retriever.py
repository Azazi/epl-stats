import os
import requests
from loguru import logger

BASE_URL = 'https://www.worldfootball.net/schedule/eng-premier-league-{}-{}'
CACHE_URL = 'cache/{}-{}.html'


def _get_season_data_from_cache(start_year, end_year):
    logger.info(f'Loading {start_year}/{end_year} season data from cache')
    with open(CACHE_URL.format(start_year, end_year), "r") as file:
        return file.read()


def _get_season_data_from_web(start_year, end_year):
    logger.info(f'Loading {start_year}/{end_year} season data from the web')
    page = requests.get(BASE_URL.format(start_year, end_year))
    with open(CACHE_URL.format(start_year, end_year), "w") as file:
        file.write(page.text)
    return page.text


def get_season_data(start_year, end_year):
    if os.path.exists(CACHE_URL.format(start_year, end_year)):
        return _get_season_data_from_cache(start_year, end_year)
    return _get_season_data_from_web(start_year, end_year)
