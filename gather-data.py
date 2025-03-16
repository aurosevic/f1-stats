import os

import pandas as pd
import requests
from bs4 import BeautifulSoup

from enums import RaceSection

F1_BASE_URL = 'https://www.formula1.com/en/results'
TABLE_CLASS = 'f1-table f1-table-with-data w-full'
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


def get_table(url: str, table_class: str) -> BeautifulSoup:
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.find('table', {'class': table_class})

        if not table:
            raise f'Could not find the table with class \'{table_class}\' on the page.'

        return table

    except Exception as e:
        raise e


def save_race_results(gp_table: BeautifulSoup, year: int, file_name: str, gp_name: str):
    data = []
    for gp_row in gp_table.find('tbody').find_all('tr'):
        cols = gp_row.find_all('td')

        position = cols[0].text.strip()
        driver_number = cols[1].text.strip()
        driver = cols[2].text.replace('&nbsp;', ' ').replace('\xa0', ' ').strip()
        car = cols[3].text.strip()
        laps = cols[4].text.strip()
        time_retired = cols[5].text.strip()
        pts = cols[6].text.strip()

        data.append({
            'Position': position,
            'Driver Number': driver_number,
            'Driver': driver,
            'Car': car,
            'Laps': laps,
            'Time/Retired': time_retired,
            'Points': pts
        })

    df = pd.DataFrame(data)
    file_path = f'data/{year}/{file_name}/{gp_name}.csv'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    df.to_csv(file_path, index=False)


def save_fastest_laps(gp_table: BeautifulSoup, year: int, file_name: str, gp_name: str):
    data = []
    for gp_row in gp_table.find('tbody').find_all('tr'):
        cols = gp_row.find_all('td')

        position = cols[0].text.strip()
        driver_number = cols[1].text.strip()
        driver = cols[2].text.replace('&nbsp;', ' ').replace('\xa0', ' ').strip()
        car = cols[3].text.strip()
        lap = cols[4].text.strip()
        time_of_day = cols[5].text.strip()
        time = cols[6].text.strip()
        avg_speed = cols[5].text.strip()

        data.append({
            'Position': position,
            'Driver Number': driver_number,
            'Driver': driver,
            'Car': car,
            'Lap': lap,
            'Time of Day': time_of_day,
            'Time': time,
            'Avg Speed': avg_speed
        })

    df = pd.DataFrame(data)
    file_path = f'data/{year}/{file_name}/{gp_name}.csv'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    df.to_csv(file_path, index=False)


def save_pit_stop_summary(gp_table: BeautifulSoup, year: int, file_name: str, gp_name: str):
    data = []
    for gp_row in gp_table.find('tbody').find_all('tr'):
        cols = gp_row.find_all('td')

        stop = cols[0].text.strip()
        driver_number = cols[1].text.strip()
        driver = cols[2].text.replace('&nbsp;', ' ').replace('\xa0', ' ').strip()
        car = cols[3].text.strip()
        lap = cols[4].text.strip()
        time_of_day = cols[5].text.strip()
        time = cols[6].text.strip()
        duration = cols[7].text.strip()

        data.append({
            'Stop': stop,
            'Driver Number': driver_number,
            'Driver': driver,
            'Car': car,
            'Lap': lap,
            'Time of Day': time_of_day,
            'Time': time,
            'Duration': duration
        })

    df = pd.DataFrame(data)
    file_path = f'data/{year}/{file_name}/{gp_name}.csv'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    df.to_csv(file_path, index=False)


def save_starting_grid(gp_table: BeautifulSoup, year: int, file_name: str, gp_name: str):
    data = []
    for gp_row in gp_table.find('tbody').find_all('tr'):
        cols = gp_row.find_all('td')

        position = cols[0].text.strip()
        driver_number = cols[1].text.strip()
        driver = cols[2].text.replace('&nbsp;', ' ').replace('\xa0', ' ').strip()
        car = cols[3].text.strip()
        time = cols[4].text.strip()

        data.append({
            'Position': position,
            'Driver Number': driver_number,
            'Driver': driver,
            'Car': car,
            'Time': time
        })

    df = pd.DataFrame(data)
    file_path = f'data/{year}/{file_name}/{gp_name}.csv'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    df.to_csv(file_path, index=False)


def save_qualifying(gp_table: BeautifulSoup, year: int, file_name: str, gp_name: str):
    data = []
    for gp_row in gp_table.find('tbody').find_all('tr'):
        cols = gp_row.find_all('td')

        position = cols[0].text.strip()
        driver_number = cols[1].text.strip()
        driver = cols[2].text.replace('&nbsp;', ' ').replace('\xa0', ' ').strip()
        car = cols[3].text.strip()
        q1 = cols[4].text.strip()
        q2 = cols[5].text.strip()
        q3 = cols[6].text.strip()
        laps = cols[7].text.strip()

        data.append({
            'Position': position,
            'Driver Number': driver_number,
            'Driver': driver,
            'Car': car,
            'Q1': q1,
            'Q2': q2,
            'Q3': q3,
            'Laps': laps
        })

    df = pd.DataFrame(data)
    file_path = f'data/{year}/{file_name}/{gp_name}.csv'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    df.to_csv(file_path, index=False)


def save_practice(gp_table: BeautifulSoup, year: int, file_name: str, gp_name: str):
    data = []
    for gp_row in gp_table.find('tbody').find_all('tr'):
        cols = gp_row.find_all('td')

        position = cols[0].text.strip()
        driver_number = cols[1].text.strip()
        driver = cols[2].text.replace('&nbsp;', ' ').replace('\xa0', ' ').strip()
        car = cols[3].text.strip()
        time = cols[4].text.strip()
        gap = cols[5].text.strip()
        laps = cols[6].text.strip()

        data.append({
            'Position': position,
            'Driver Number': driver_number,
            'Driver': driver,
            'Car': car,
            'Time': time,
            'Gap': gap,
            'Laps': laps
        })

    df = pd.DataFrame(data)
    file_path = f'data/{year}/{file_name}/{gp_name}.csv'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    df.to_csv(file_path, index=False)


def should_scrape(year: int, file_name: str) -> bool:
    for section in RaceSection:
        if not os.path.exists(f'data/{year}/{section.value}/{file_name}.csv'):
            return True
    return False


def scrape_f1_table(year=2025):
    url = f'{F1_BASE_URL}/{year}/races'

    try:
        table = get_table(url, TABLE_CLASS)

        for i, row in enumerate(table.find('tbody').find_all('tr')):
            cols = row.find_all('td')

            grand_prix = cols[0].find('a').text.strip()
            date = cols[1].text.strip()

            file_name = f'{i + 1}-{grand_prix}'
            if not should_scrape(year, file_name):
                continue

            print(f'Gathering data for {grand_prix} {date}...')

            gp_id = cols[0].find('a')['href'].split('/', 1)[1].rsplit('/', 1)[0]

            for section in RaceSection:
                if os.path.exists(f'data/{year}/{section.value}/{file_name}.csv'):
                    continue

                print(f'Going through {section.name}')

                grand_prix_link = f'{url}/{gp_id}/{section.value}'
                gp_table = get_table(grand_prix_link, TABLE_CLASS)

                match section:
                    case RaceSection.PRACTICE_1:
                        save_practice(gp_table, year, section.value, file_name)
                    case RaceSection.PRACTICE_2:
                        save_practice(gp_table, year, section.value, file_name)
                    case RaceSection.PRACTICE_3:
                        save_practice(gp_table, year, section.value, file_name)
                    case RaceSection.QUALIFYING:
                        save_qualifying(gp_table, year, section.value, file_name)
                    case RaceSection.STARTING_GRID:
                        save_starting_grid(gp_table, year, section.value, file_name)
                    case RaceSection.PIT_STOP_SUMMARY:
                        save_pit_stop_summary(gp_table, year, section.value, file_name)
                    case RaceSection.FASTEST_LAPS:
                        save_fastest_laps(gp_table, year, section.value, file_name)
                    case RaceSection.RACE_RESULT:
                        save_race_results(gp_table, year, section.value, file_name)
    except Exception as e:
        print(f'An error occurred: {e}')


scrape_f1_table()
