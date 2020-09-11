from sys import argv

from app.generate_csv import GeneratorCsv
from app.lotteries_download import CaixaLotteriesDownload
from log_generator import RegisterLogs

logger = RegisterLogs()

create_csv = GeneratorCsv()

url_allowed = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/'


def validation(premium):

    list_premium = {
        'megasena': 'megase',
        'quina': 'quina',
        'lotofacil': 'lotfac',
    }

    if premium in list_premium.keys():
        return list_premium[premium]
    logger.warning_register(f'Parameter {argv[1]} not exist!')
    return


if __name__ == "__main__":
    # Parameters: megasena | quina | lotofacil

    name_file = validation(argv[1])

    if name_file:
        url = f'{url_allowed}D_{name_file}.zip'
        get_file = CaixaLotteriesDownload(source_file=argv[1], url=url)
        get_file.verification_http()
        create_csv.convert_to_csv(argv[1], f'd_{name_file}')
        create_csv.sanitize_csv(argv[1])
