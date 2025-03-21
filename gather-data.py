import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date

import pandas as pd
import requests
from bs4 import BeautifulSoup

from enums import RaceSection

F1_BASE_URL = 'https://www.formula1.com/en/results'
TABLE_CLASS = 'f1-table f1-table-with-data w-full'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def get_table(url: str, table_class: str) -> BeautifulSoup:
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.find('table', {'class': table_class})

        if not table:
            raise ValueError(f'Could not find the table with class \'{table_class}\' on the page.')

        return table
    except Exception as e:
        raise e


def save_table_data(gp_table: BeautifulSoup, year: int, section: RaceSection, gp_name: str):
    print(f'Going through {section.name}...', end=' ')
    data = []
    for gp_row in gp_table.find('tbody').find_all('tr'):
        cols = gp_row.find_all('td')
        headers = [th.text.strip() for th in gp_table.find('thead').find_all('th')]

        data.append({
            header: col.text.replace('&nbsp;', ' ').replace('\xa0', ' ').strip()
            for col, header in zip(cols, headers)
        })

    df = pd.DataFrame(data)
    file_path = f'data/{year}/{section.value}/{gp_name}.csv'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    df.to_csv(file_path, index=False)
    print(f'Finished with {section.name}.')


def scrape_grand_prix(year: int, url: str, grand_prix: str, gp_id: str, file_name: str):
    for section in RaceSection:
        if os.path.exists(f'data/{year}/{section.value}/{file_name}.csv'):
            continue

        grand_prix_link = f'{url}/{gp_id}/{section.value}'

        try:
            gp_table = get_table(grand_prix_link, TABLE_CLASS)
        except ValueError:
            continue  # In case the race weekend doesn't have the section(for example no sprint qualifying)

        save_table_data(gp_table, year, section, file_name)


def scrape_f1_table(year=date.today().year, max_workers=10):
    url = f'{F1_BASE_URL}/{year}/races'

    try:
        table = get_table(url, TABLE_CLASS)
        tasks = []

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for i, row in enumerate(table.find('tbody').find_all('tr')):
                cols = row.find_all('td')
                grand_prix = cols[0].find('a').text.strip()
                race_date = cols[1].text.strip()

                print(f'\n🏁 Gathering data for {grand_prix} {race_date}...')

                file_name = f'{i + 1}-{grand_prix}'
                gp_id = cols[0].find('a')['href'].split('/', 1)[1].rsplit('/', 1)[0]
                tasks.append(executor.submit(scrape_grand_prix, year, url, grand_prix, gp_id, file_name))

            for task in as_completed(tasks):
                task.result()
    except Exception as e:
        print(f'An error occurred: {e}')


scrape_f1_table()
