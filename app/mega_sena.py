from datetime import datetime as dt
from os import path, remove
from time import sleep
from zipfile import ZipFile

from requests import get
from requests.exceptions import HTTPError
from rich.console import Console


class MegaSenaDownload:
    def __init__(self, source_file, url):
        self.url = url
        self.response = get(self.url, stream=True)
        self.date = dt.now().strftime('%Y-%m-%d')
        self.source_file = source_file
        self.console = Console()

    def verification_http(self):

        try:
            self.response.raise_for_status()
        except HTTPError as e:
            raise SystemExit(f'Error: {e}')
        except Exception as e:
            raise SystemExit(f'Error: {e}')
        else:
            self.write_file()

    def write_file(self):
        try:

            with open(f'{self.source_file}', "wb") as file_zip:
                for data in self.response.iter_content():
                    file_zip.write(data)
                self.console.log(
                    f'Arquivo [bold cyan]{self.source_file}[/bold cyan] baixado com sucesso!'
                )
            sleep(1)
            self.extract_file()

        except Exception as e:
            raise SystemExit(f'Error: {e}')

    def extract_file(self):
        try:

            if path.exists(f'{self.source_file}'):

                with ZipFile(f'{self.source_file}', 'r') as extract_file:
                    extract_file.extractall(f'raw/megasena/{self.date}')
                self.console.log(
                    f'Arquivo [bold cyan]{self.source_file}[/bold cyan] extraido com sucesso! '
                    f'Verifique na pasta raw/megasena/{self.date}'
                )
                remove(f'{self.source_file}')

        except Exception as e:
            raise SystemExit(f'Error: {e}')
