from datetime import datetime as dt
from os import path, remove
from zipfile import ZipFile

from requests import get
from requests.exceptions import HTTPError


class MegaSenaDownload:
    def __init__(self, main_word):
        self.url = (
            'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip'
        )
        self.response = get(self.url, stream=True)
        self.date = dt.now().strftime('%Y-%m-%d')
        self.main_word = main_word

    def get_file(self):
        try:
            with open(f'{self.main_word}', "wb") as file_zip:
                for data in self.response.iter_content():
                    file_zip.write(data)

        except HTTPError as e:
            raise SystemExit(f'Error: {e}')

    def extract_file(self):
        with ZipFile(f'{self.main_word}', 'r') as extract_file:
            extract_file.extractall(f'Mega-Sena/RawData/{self.date}')

        if path.exists(f'{self.main_word}'):
            remove(f'{self.main_word}')


if __name__ == '__main__':    
    main_word = 'mega-sena.zip'
    get_file = MegaSenaDownload(main_word=main_word)
    get_file.get_file()
    get_file.extract_file()
