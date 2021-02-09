from datetime import datetime as dt
from os import path, remove
from zipfile import ZipFile

from requests import get
from requests.exceptions import ConnectionError, HTTPError
from retry import retry

from log_generator import RegisterLogs

logger = RegisterLogs()


class CaixaLotteriesDownload:
    def __init__(self, source_file, url):
        self.response = get(url, stream=True)
        self.date = dt.now().strftime('%Y-%m-%d')
        self.source_file = source_file

    @retry(
        exceptions=(HTTPError, Exception, ConnectionError), tries=3, delay=30
    )
    def extract_zip_file(self):

        self.response.raise_for_status()

        # Download File
        with open(f'{self.source_file}.zip', 'wb') as file_zip:
            for data in self.response.iter_content(chunk_size=250):
                file_zip.write(data)

            logger.debug_register(
                f'{self.source_file} file downloaded successfully!'
            )

        # Extracted File
        with ZipFile(f'{self.source_file}.zip', 'r') as extract_file:
            extract_file.extractall(f'raw/{self.source_file}/{self.date}')

        logger.debug_register(
            f'{self.source_file} file successfully extracted!'
        )
        remove(f'{self.source_file}.zip')
        logger.debug_register(
            f'{self.source_file}.zip file successfully removed!'
        )
