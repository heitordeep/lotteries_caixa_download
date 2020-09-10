from sys import argv

from app.generate_csv import GeneratorCsv
from app.lotteries_download import CaixaLotteriesDownload
from log_generator import RegisterLogs

logger = RegisterLogs()

create_csv = GeneratorCsv()

if __name__ == "__main__":
    # Parameters: megasena | quina | lotofacil

    name_file = None

    if argv[1] == 'megasena':
        name_file = 'megase'
    elif argv[1] == 'quina':
        name_file = 'quina'
    elif argv[1] == 'lotofacil':
        name_file = 'lotfac'
    else:
        logger.warning_register(f'Parameter {argv[1]} not exist!')
        exit()

    url = f'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_{name_file}.zip'
    get_file = CaixaLotteriesDownload(source_file=argv[1], url=url)
    get_file.verification_http()
    create_csv.convert_to_csv(argv[1], f'd_{name_file}')
    create_csv.sanitize_csv(argv[1])
