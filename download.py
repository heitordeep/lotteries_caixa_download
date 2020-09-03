from sys import argv

from rich.console import Console

from app.generate_csv import GeneratorCsv
from app.lotteries_download import CaixaLotteriesDownload

console = Console()

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
        console.print(f'[bold red]Parameter {argv[1]} not exist![/bold red]')
        exit()

    url = f'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_{name_file}.zip'
    get_file = CaixaLotteriesDownload(source_file=argv[1], url=url)
    get_file.verification_http()
    create_csv.convert_to_csv(argv[1], f'd_{name_file}')
    create_csv.sanitize_csv(argv[1])
