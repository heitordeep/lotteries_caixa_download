from datetime import datetime as dt
from os import path, remove
from time import sleep
from zipfile import ZipFile

from requests import get
from requests.exceptions import HTTPError
from rich.console import Console

console = Console()


class MegaSenaDownload:
    def __init__(self, source_file, url):
        self.response = get(url, stream=True)
        self.date = dt.now().strftime('%Y-%m-%d')
        self.source_file = source_file

    def verification_http(self):

        try:
            self.response.raise_for_status()
            
            # Download File 
            with open(f'{self.source_file}', 'wb') as file_zip:
                for data in self.response.iter_content():
                    file_zip.write(data)
                console.log(
                    f'Arquivo [bold cyan]{self.source_file}[/bold cyan] baixado com sucesso!'
                )
                
            # Extracted File
            with ZipFile(f'{self.source_file}', 'r') as extract_file:
                extract_file.extractall(f'raw/megasena/{self.date}')
            console.log(
                f'Arquivo [bold cyan]{self.source_file}[/bold cyan] extraido com sucesso! '
                f'Verifique na pasta raw/megasena/{self.date}'
            )
            remove(f'{self.source_file}')

        except HTTPError as e:
            count = 3
            if count != 0:
                console.log(
                    f'{e}'
                    f'\nAguarde [bold yellow]60[/bold yellow] segundos para tentar novamente.'
                )
                sleep(60)
                self.verification_http()

            raise SystemExit(f'Error: {e}')

        except Exception as e:
            raise SystemExit(f'Error: {e}')
