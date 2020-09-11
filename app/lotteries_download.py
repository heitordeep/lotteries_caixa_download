from datetime import datetime as dt
from os import path, remove
from time import sleep
from zipfile import ZipFile

from requests import get
from requests.exceptions import HTTPError

from log_generator import RegisterLogs

logger = RegisterLogs()


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

        except HTTPError as e:
            if self.count != 0:
                logger.debug_register(f'Error: {e} - Wait 60 seconds...')
                sleep(60)
                self.count -= 1
                logger.debug_register(
                    f'Retrying to download the {self.source_file} file...'
                )
                self.verification_http()

            logger.debug_register(f'Error: {e} - Finish')
            raise SystemExit(f'Error: {e}')

        except Exception as e:
            logger.debug_register(f'Error: {e} - Finish')
            raise SystemExit(f'Error: {e}')
