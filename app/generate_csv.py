from datetime import datetime as dt
from os import makedirs, path
from sys import argv

import pandas as pd

from log_generator import RegisterLogs

logger = RegisterLogs()


class GeneratorCsv:
    def __init__(self):
        self.date = dt.now().strftime('%Y-%m-%d')

    def read_file(self, tag, path_name):

        allowed_files = {'html': pd.read_html, 'csv': pd.read_csv}

        if path.exists(path_name) and tag in allowed_files:
            return allowed_files[tag](path_name)
        else:
            raise SystemExit(f"Error: Parameter {tag} forbidden!")

    def convert_to_csv(self, directory_name, name_file):

        if name_file == 'd_megase':
            name_file = 'd_mega'

        path_name = f'raw/{directory_name}/{self.date}/{name_file}.htm'

        logger.debug_register(f'Reading {name_file}.htm file...')

        df = self.read_file('html', path_name)

        logger.debug_register(f'Getting data {name_file} file...')

        self.create_csv(
            data=df[0],
            path_file=f'swamp/{directory_name}/{self.date}',
            source_file='nao_tratado.csv',
        )

    def sanitize_csv(self, directory_name):

        path_name = f'swamp/{directory_name}/{self.date}/nao_tratado.csv'

        logger.debug_register(
            f'Searching swamp/{directory_name}/{self.date}/nao_tratado.csv...'
        )

        logger.debug_register('nao_tratado.csv file found!')

        df = self.read_file('csv', path_name)

        df['Cidade'] = df['Cidade'].replace(['&nbsp'], ' ')
        df['UF'] = df['UF'].replace(['&nbsp'], ' ')

        logger.debug_register('Getting data nao_tratado.csv...')

        self.create_csv(
            data=df,
            path_file=f'lake/{directory_name}/{self.date}',
            source_file='tratado.csv',
        )

    def create_csv(self, data, path_file, source_file):

        data_csv = pd.DataFrame(data)

        makedirs(path_file, exist_ok=True)
        data_csv.to_csv(
            f'{path_file}/{source_file}', index=False, chunksize=300
        )

        logger.debug_register(
            f'Created {source_file} file success! - Check in the folder {path_file}'
        )
