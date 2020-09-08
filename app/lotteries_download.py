from datetime import datetime as dt
from os import path, remove
from time import sleep
from zipfile import ZipFile

from rich.console import Console

from requests import get
from requests.exceptions import HTTPError

console = Console()


class CaixaLotteriesDownload:
    def __init__(self, source_file, url):
        self.response = get(url, stream=True)
        self.date = dt.now().strftime('%Y-%m-%d')
        self.source_file = source_file
        self.count = 2

    def verification_http(self):

        try:
            self.response.raise_for_status()

            # Download File
            with open(f'{self.source_file}.zip', 'wb') as file_zip:
                for data in self.response.iter_content(chunk_size=250):
                    file_zip.write(data)
                console.log(
                    f'Arquivo [bold cyan]{self.source_file}[/bold cyan] baixado com sucesso!'
                )

            # Extracted File
            with ZipFile(f'{self.source_file}.zip', 'r') as extract_file:
                extract_file.extractall(f'raw/{self.source_file}/{self.date}')
            console.log(
                f'Arquivo [bold cyan]{self.source_file}[/bold cyan] extraido com sucesso! '
                f'Verifique na pasta raw/{self.source_file}/{self.date}'
            )
            remove(f'{self.source_file}.zip')

        except HTTPError as e:
            if self.count != 0:
                console.log(
                    f'{e}'
                    f'\nAguarde [bold yellow]60[/bold yellow] segundos para tentar novamente.'
                )
                sleep(60)
                self.count -= 1
                self.verification_http()

            raise SystemExit(f'Error: {e}')

        except Exception as e:
            raise SystemExit(f'Error: {e}')
