from datetime import datetime as dt
from os import path, remove
from zipfile import ZipFile

from requests import get
from requests.exceptions import HTTPError


class MegaSenaDownload:
    def __init__(self, source_file, url):
        self.url = url
        self.response = get(self.url, stream=True)
        self.date = dt.now().strftime('%Y-%m-%d')
        self.source_file = source_file

    def verification_http(self):

        try:
            self.response.raise_for_status()
        except HTTPError as e:
            raise SystemExit(e)
        except Exception as e:
            raise SystemExit(f'Error: {e}')
        else:
            self.write_file()

    def write_file(self):
        try:
            with open(f'{self.source_file}', "wb") as file_zip:
                for data in self.response.iter_content():
                    file_zip.write(data)

            self.extract_file()

        except Exception as e:
            raise SystemExit(f'Error: {e}')

    def extract_file(self):
        try:

            with ZipFile(f'{self.source_file}', 'r') as extract_file:
                extract_file.extractall(f'Mega-Sena/RawData/{self.date}')

            if path.exists(f'{self.source_file}'):
                remove(f'{self.source_file}')

        except Exception as e:
            raise SystemExit(f'Error: {e}')


if __name__ == '__main__':
    source_file = 'mega-sena.zip'
    url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip'
    get_file = MegaSenaDownload(source_file=source_file, url=url)
    get_file.verification_http()
