from datetime import datetime as dt
from os import makedirs, path
from sys import argv

import pandas as pd
from rich.console import Console

console = Console()


class GeneratorCsv:
    def __init__(self):
        self.date = dt.now().strftime('%Y-%m-%d')

    def convert_to_csv(self, name_directory, name_file):
        console.log(f'Buscando arquivo [bold cyan]{name_file}.htm[/bold cyan]')

        if name_file == 'd_megase':
            name_file = 'd_mega'

        if path.exists(f'raw/{name_directory}/{self.date}/{name_file}.htm'):

            console.log(
                f'Arquivo [bold cyan]{name_file}.htm[/bold cyan] encontrado :smiley:'
            )
            df = pd.read_html(
                f'raw/{name_directory}/{self.date}/{name_file}.htm'
            )

            df = df[0]

            data = {}

            for key, value in df.items():
                data.update({key: value})

            console.log(
                f'Obtendo os dados do arquivo [bold cyan]{name_file}.htm[/bold cyan]...'
            )

            self.create_csv(
                data=data,
                path_file=f'swamp/{name_directory}/{self.date}',
                source_file='nao_tratado.csv',
            )

    def sanitize_csv(self, name_directory):

        path_file = f'swamp/{name_directory}/{self.date}/nao_tratado.csv'

        console.log(f'Buscando arquivo [bold cyan]nao_tratado.csv[/bold cyan]')
        if path.exists(path_file):

            console.log(
                f'Arquivo [bold cyan]nao_tratado.csv[/bold cyan] encontrado :smiley:'
            )
            df = pd.read_csv(f'{path_file}')
            sanitize_city = df['Cidade'].replace(['&nbsp'], ' ')
            sanitize_uf = df['UF'].replace(['&nbsp'], ' ')

            data = {}

            for key, value in df.items():
                if key == 'Cidade':
                    data.update({key: sanitize_city})
                elif key == 'UF':
                    data.update({key: sanitize_uf})
                else:
                    data.update({key: value})

            console.log(
                f'Obtendo os dados do arquivo [bold cyan]nao_tratado.csv[/bold cyan]...'
            )

            self.create_csv(
                data=data,
                path_file=f'lake/{name_directory}/{self.date}',
                source_file='tratado.csv',
            )

    def create_csv(self, data, path_file, source_file):

        data_csv = pd.DataFrame(data)

        makedirs(path_file, exist_ok=True)
        data_csv.to_csv(f'{path_file}/{source_file}', index=False, chunksize=300)

        console.log(
            f'Arquivo [bold cyan]{source_file}[/bold cyan] criado com sucesso! '
            f'Verifique na pasta: {path_file} '
        )
