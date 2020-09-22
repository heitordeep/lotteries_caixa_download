from sys import argv

from app.generate_csv import GeneratorCsv
from app.lotteries_download import CaixaLotteriesDownload
from log_generator import RegisterLogs

url_allowed = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/'

list_prizes_allowed = {
    'megasena': 'megase',
    'quina': 'quina',
    'lotofacil': 'lotfac',
}

if __name__ == "__main__":
    # Parameters: megasena | quina | lotofacil

    prize = argv[1]

    if prize in list_prizes_allowed.keys():
        name_file = list_prizes_allowed.pop(prize)

        url = f'{url_allowed}D_{name_file}.zip'
        get_file = CaixaLotteriesDownload(source_file=prize, url=url)
        get_file.extract_zip_file()
        create_csv = GeneratorCsv()
        create_csv.convert_to_csv(
            directory_name=prize, name_file=f'd_{name_file}'
        )
        create_csv.sanitize_csv(directory_name=prize)
    else:
        log = RegisterLogs()
        log.warning_register(f"Parameter {prize} doesn't exist!")
