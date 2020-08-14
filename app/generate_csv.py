from datetime import datetime as dt
from os import makedirs, path
from time import sleep

import pandas as pd
from rich.console import Console

from app.mega_sena import MegaSenaDownload


class GeneratorCsv:
    def __init__(self):
        self.date = dt.now().strftime('%Y-%m-%d')
        self.console = Console()

    def convert_to_csv(self):
        self.console.log(f'Buscando arquivo [bold cyan]d_mega.htm[/bold cyan]')
        if path.exists(f'raw/megasena/{self.date}/d_mega.htm'):
            sleep(1)
            self.console.log(
                f'Arquivo [bold cyan]d_mega.htm[/bold cyan] encontrado :smiley:'
            )
            df = pd.read_html(f'raw/megasena/{self.date}/d_mega.htm')

            df = df[0]

            data = {
                'Concurso': df['Concurso'],
                'Data Sorteio': df['Data Sorteio'],
                '1ª Dezena': df['1ª Dezena'],
                '2ª Dezena': df['2ª Dezena'],
                '3ª Dezena': df['3ª Dezena'],
                '4ª Dezena': df['4ª Dezena'],
                '5ª Dezena': df['5ª Dezena'],
                '6ª Dezena': df['6ª Dezena'],
                'Arrecadacao_Total': df['Arrecadacao_Total'],
                'Ganhadores_Sena': df['Ganhadores_Sena'],
                'Cidade': df['Cidade'],
                'UF': df['UF'],
                'Rateio_Sena': df['Rateio_Sena'],
                'Ganhadores_Quina': df['Ganhadores_Quina'],
                'Rateio_Quina': df['Rateio_Quina'],
                'Ganhadores_Quadra': df['Ganhadores_Quadra'],
                'Rateio_Quadra': df['Rateio_Quadra'],
                'Acumulado': df['Acumulado'],
                'Valor_Acumulado': df['Valor_Acumulado'],
                'Acumulado_Mega_da_Virada': df['Acumulado_Mega_da_Virada'],
            }

            self.console.log(
                f'Obtendo os dados do arquivo [bold cyan]d_mega.htm[/bold cyan]...'
            )
            sleep(1)
            self.create_csv(
                data=data,
                path_file=f'swamp/megasena/{self.date}',
                source_file='nao_tratado.csv',
            )

    def sanitize_csv(self):

        path_file = f'swamp/megasena/{self.date}/nao_tratado.csv'
        sleep(1)
        self.console.log(
            f'Buscando arquivo [bold cyan]nao_tratado.csv[/bold cyan]'
        )
        if path.exists(path_file):
            sleep(1)
            self.console.log(
                f'Arquivo [bold cyan]nao_tratado.csv[/bold cyan] encontrado :smiley:'
            )
            df = pd.read_csv(f'{path_file}')
            sanitize_city = df['Cidade'].replace(['&nbsp', 'NaN'], ' ')
            sanitize_uf = df['UF'].replace(['&nbsp', 'NaN'], ' ')

            data = {
                'Concurso': df['Concurso'],
                'Data Sorteio': df['Data Sorteio'],
                '1ª Dezena': df['1ª Dezena'],
                '2ª Dezena': df['2ª Dezena'],
                '3ª Dezena': df['3ª Dezena'],
                '4ª Dezena': df['4ª Dezena'],
                '5ª Dezena': df['5ª Dezena'],
                '6ª Dezena': df['6ª Dezena'],
                'Arrecadacao_Total': df['Arrecadacao_Total'],
                'Ganhadores_Sena': df['Ganhadores_Sena'],
                'Cidade': sanitize_city,
                'UF': sanitize_uf,
                'Rateio_Sena': df['Rateio_Sena'],
                'Ganhadores_Quina': df['Ganhadores_Quina'],
                'Rateio_Quina': df['Rateio_Quina'],
                'Ganhadores_Quadra': df['Ganhadores_Quadra'],
                'Rateio_Quadra': df['Rateio_Quadra'],
                'Acumulado': df['Acumulado'],
                'Valor_Acumulado': df['Valor_Acumulado'],
                'Acumulado_Mega_da_Virada': df['Acumulado_Mega_da_Virada'],
            }

            self.console.log(
                f'Obtendo os dados do arquivo [bold cyan]nao_tratado.csv[/bold cyan]...'
            )

            sleep(1)

            self.create_csv(
                data=data,
                path_file=f'lake/megasena/{self.date}',
                source_file='tratado.csv',
            )

    def create_csv(self, **kwargs):

        data_csv = pd.DataFrame(kwargs['data'])

        makedirs(kwargs["path_file"], exist_ok=True)
        data_csv.to_csv(
            f'{kwargs["path_file"]}/{kwargs["source_file"]}', index=False
        )
        sleep(1)
        self.console.log(
            f'Arquivo [bold cyan]{kwargs["source_file"]}[/bold cyan] criado com sucesso! '
            f'Verifique na pasta: {kwargs["path_file"]} '
        )

    def main(self):
        source_file = 'mega-sena.zip'
        url = (
            'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip'
        )
        get_file = MegaSenaDownload(source_file=source_file, url=url)
        get_file.verification_http()
        csv = GeneratorCsv()
        csv.convert_to_csv()
        csv.sanitize_csv()
