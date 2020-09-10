from datetime import datetime as dt
from os import makedirs, path
from sys import argv

import pandas as pd
from log_generator import RegisterLogs

logger = RegisterLogs()


class GeneratorCsv:
    def __init__(self):
        self.date = dt.now().strftime('%Y-%m-%d')

    def convert_to_csv(self, name_directory, name_file):

        if name_file == 'd_megase':
            name_file = 'd_mega'

        if path.exists(f'raw/{name_directory}/{self.date}/{name_file}.htm'):
            logger.debug_register(f'Reading {name_file}.htm file...')

            df = pd.read_html(
                f'raw/{name_directory}/{self.date}/{name_file}.htm'
            )

            df = df[0]

            data = {}

            logger.debug_register(f'Getting data {name_file} file...')

            for key, value in df.items():
                data.update({key: value})

            self.create_csv(
                data=data,
                path_file=f'swamp/{name_directory}/{self.date}',
                source_file='nao_tratado.csv',
            )

    def sanitize_csv(self, name_directory):

        path_file = f'swamp/{name_directory}/{self.date}/nao_tratado.csv'

        logger.debug_register(
            f'Searching swamp/{name_directory}/{self.date}/nao_tratado.csv...'
        )
        if path.exists(path_file):

            logger.debug_register('nao_tratado.csv file found!')

            df = pd.read_csv(f'{path_file}')
            sanitize_city = df['Cidade'].replace(['&nbsp'], ' ')
            sanitize_uf = df['UF'].replace(['&nbsp'], ' ')

            data = {}

            logger.debug_register('Getting data nao_tratado.csv...')
            for key, value in df.items():
                if key == 'Cidade':
                    data.update({key: sanitize_city})
                elif key == 'UF':
                    data.update({key: sanitize_uf})
                else:
                    data.update({key: value})

            self.create_csv(
                data=data,
                path_file=f'lake/{name_directory}/{self.date}',
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
