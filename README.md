# Lotteries Caixa Download :moneybag:<br>
<img src='https://camo.githubusercontent.com/826560c5526525754718e6877d244af221d92634/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d696e666f726d6174696f6e616c'>
Extracted data with Python.


<br>

# :warning: Pending to resolve and Resolved:

- [X] Extract files
- [X] Create Web Page
- [X] Create API
- [X] Create API Documentation
- [X] Fix data storage in Mongodb - (Delay)
- [X] Create data view with Mongodb 
- [X] API Pagination
- [X] App in the Docker

# :pushpin: Requirements:

Library: <img src='https://img.shields.io/badge/Requests-2.24.0-informational'> <img src='https://img.shields.io/badge/Pandas-1.1.0-informational'><br>
Linguage: <img src='https://camo.githubusercontent.com/2857442965ab9a51229c075102012bdbd340abc3/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f72657175657374733f6c6162656c3d507974686f6e266c6f676f3d505954484f4e266c6f676f436f6c6f723d79656c6c6f77267374796c653d706c6173746963'> <br>
Database: <img src="https://img.shields.io/badge/Docker-MongoDB-informational"><br><br>


- Linux: <br><br>
  - Docker Server:<br><br>
    Create image MongoDb, Python and run app :<br><br>
    ```shell
    $ make start 
    ```

  - Without Docker. Download Files of Caixa:<br><br>

    ```shell
    $ make requirements-pip 
    ```

<br>


- Windows: <br><br>
   - Docker Server:<br><br>

     Create image MongoDb, Python and run app :<br><br>
     ```shell
     $ docker-compose up -d
     ```

   - Without Docker. Download Files of Caixa:<br><br>
     
     ```shell
     $ create_venv.bat
     ```
     and

     ```shell
     $ pip install -r requirements/requirements_dev.txt
     ```

# :rocket: Run the command without Docker:
- Parameters: **megasena | quina | lotofacil** <br>
   - Linux: <br>
        ```shell
        $ make run search="Parameters"
        ```

   - Windows:<br>
        ```shell
       $ python download.py "Parameters"
        ```
<br>

# :computer: Run Web Page and API:
- It is necessary to create an .env file with the following information: <br><br>
   - ```.env```:  <br>**URI=database** <br>**DATABASE=Choose a name**<br>

   - Command: <br>
        ```shell
        $ docker start {id}
        ```
- Access with Docker:<br>
  - Web Page: http://0.0.0.0/web/
  - API: http://0.0.0.0/api/

- Access without Docker: <br>
  - Web Page: http://0.0.0.0:8080/web/
  - API: http://0.0.0.0:8080/api/

<br>
  
- The data will be stored in the file and Mongodb.<br><br>
Consult File: <br><br>For Example: <br>
**raw/megasena/2020-08-14/files** - (Raw Data) html<br>
**swamp/megasena/2020-08-14/files** - (Raw Data) csv<br>
**lake/megasena/2020-08-14/files**
<br><br>
OBS: **The files are in the directory lake.**

<br><br>
- Consult MongoDb:<br><br>
     ```shell
     $ db.lotofacil.find({})
     ```
     ```shell
     $ db.quina.find({})
     ```
     ```shell
     $ db.megasena.find({})
     ```
<br>

Result directories:<br>

<img src='https://user-images.githubusercontent.com/17969551/90266677-b97a1580-de2a-11ea-8930-131a304ab4d6.png' width='400'>
<br>

Example the path file:<br>
<img src='https://user-images.githubusercontent.com/17969551/90266840-04942880-de2b-11ea-9007-a127c0b241fc.png' width='500'>

<br>

Result MongoDB:<br><br>
Example megasena:
```json
{ "_id" : ObjectId("5f57d2f536f72cb0f894e0c5"), "1ª Dezena" : 41, "2ª Dezena" : 5, "3ª Dezena" : 4, "4ª Dezena" : 52, "5ª Dezena" : 30, "6ª Dezena" : 33, "Acumulado" : "SIM", "Acumulado_Mega_da_Virada" : "000", "Arrecadacao_Total" : "000", "Cidade" : " ", "Concurso" : 1, "Data Sorteio" : "11/03/1996", "Estimativa_Prêmio" : "000", "Ganhadores_Quadra" : 2016, "Ganhadores_Quina" : 17, "Ganhadores_Sena" : 0, "Rateio_Quadra" : 33021, "Rateio_Quina" : 39.15892, "Rateio_Sena" : "000", "UF" : " ", "Valor_Acumulado" : "1.714.65023" }
```

# Do you need help with commands?

- Linux only
<img src='https://user-images.githubusercontent.com/17969551/89588975-208c3e80-d81b-11ea-9ba6-2fb460deca4b.png' width='600'>


## :page_facing_up: Get App Logs:

- The logs is in the directory: **log**

## Test on endpoint API:
- Return default: 300 
- Search the document: **term and search**
- Example:
  - megasena: 
  ```shell
  curl http://0.0.0.0/api/megasena?term=Data%20Sorteio&search=09/01/1999
  ```
  - quina: 
  ```shell
  curl http://0.0.0.0/api/quina?limit=2
  ```

  ```shell 
  curl http://0.0.0.0/api/quina?term=UF&search=MG&page=7&limit=1
  ```
  
  - lotofacil:
  ```shell
  curl http://0.0.0.0/api/lotofacil?term=UF&search=SP&limit=1
  ```

## Result:

- megasena: <br>
```json
{
  "count_data": 1, 
  "documents": [
    {
      "_id": "6022c6a9cacdf9adf128ddc6", 
      "Concurso": 149, 
      "Data Sorteio": "09/01/1999", 
      "1ª Dezena": 11, 
      "2ª Dezena": 45, 
      "3ª Dezena": 48, 
      "4ª Dezena": 7, 
      "5ª Dezena": 28, 
      "6ª Dezena": 20, 
      "Arrecadacao_Total": "000", 
      "Ganhadores_Sena": 0, 
      "Cidade": "null", 
      "UF": "null", 
      "Rateio_Sena": "000", 
      "Ganhadores_Quina": 106, 
      "Rateio_Quina": 9.79513, 
      "Ganhadores_Quadra": 6290, 
      "Rateio_Quadra": 16474.0, 
      "Acumulado": "SIM", 
      "Valor_Acumulado": "2.211.82094", 
      "Estimativa_Prêmio": "000", 
      "Acumulado_Mega_da_Virada": "000"
    }
  ]
}
``` 

- quina:<br> 
```json
{
  "count_data": 2, 
  "documents": [
    {
      "_id": "6022c6b4cacdf9adf12908d2", 
      "Concurso": 1, 
      "Data Sorteio": "13/03/1994", 
      "1ª Dezena": 25, 
      "2ª Dezena": 45, 
      "3ª Dezena": 60, 
      "4ª Dezena": 76, 
      "5ª Dezena": 79, 
      "Arrecadacao_Total": "000", 
      "Ganhadores_Quina": 3, 
      "Cidade": "null", 
      "UF": "null", 
      "Rateio_Quina": "75.731.22500", 
      "Ganhadores_Quadra": 127, 
      "Rateio_Quadra": "1.788.92700", 
      "Ganhadores_Terno": 7030, 
      "Rateio_Terno": 42.982, 
      "Ganhadores_Duque": 0, 
      "Rateio_Duque": 0, 
      "Acumulado": "NÃO", 
      "Valor_Acumulado": "000", 
      "Estimativa_Premio": "000", 
      "Valor_Acumulado_Sorteio_Especial_São_João": "000"
    }, 
    {
      "_id": "6022c6b4cacdf9adf12908d3", 
      "Concurso": 2, 
      "Data Sorteio": "17/03/1994", 
      "1ª Dezena": 13, 
      "2ª Dezena": 30, 
      "3ª Dezena": 58, 
      "4ª Dezena": 63, 
      "5ª Dezena": 64, 
      "Arrecadacao_Total": "000", 
      "Ganhadores_Quina": 1, 
      "Cidade": "null", 
      "UF": "null", 
      "Rateio_Quina": "118.499.39700", 
      "Ganhadores_Quadra": 105, 
      "Rateio_Quadra": "1.128.56500", 
      "Ganhadores_Terno": 4861, 
      "Rateio_Terno": 32.422, 
      "Ganhadores_Duque": 0, 
      "Rateio_Duque": 0, 
      "Acumulado": "NÃO", 
      "Valor_Acumulado": "000", 
      "Estimativa_Premio": "000", 
      "Valor_Acumulado_Sorteio_Especial_São_João": "000"
    }
  ]
}
```

Other example:<br>
```json
{
  "count_data": 1, 
  "documents": [
    {
      "_id": "6022c6b4cacdf9adf1290b98", 
      "Concurso": 670, 
      "Data Sorteio": "04/03/2000", 
      "1ª Dezena": 30, 
      "2ª Dezena": 76, 
      "3ª Dezena": 34, 
      "4ª Dezena": 8, 
      "5ª Dezena": 18, 
      "Arrecadacao_Total": "000", 
      "Ganhadores_Quina": 2, 
      "Cidade": "null", 
      "UF": "MG", 
      "Rateio_Quina": "315.26656", 
      "Ganhadores_Quadra": 340, 
      "Rateio_Quadra": "1.07814", 
      "Ganhadores_Terno": 14319, 
      "Rateio_Terno": 3402.0, 
      "Ganhadores_Duque": 0, 
      "Rateio_Duque": 0, 
      "Acumulado": "NÃO", 
      "Valor_Acumulado": "000", 
      "Estimativa_Premio": "000", 
      "Valor_Acumulado_Sorteio_Especial_São_João": "000"
    }
  ]
}
``` 

- lotofacil: <br>
```json
{
  "count_data": 1, 
  "documents": [
    {
      "_id": "6022c6aecacdf9adf128e76d", 
      "Concurso": 1, 
      "Data Sorteio": "29/09/2003", 
      "Bola1": 18, 
      "Bola2": 20, 
      "Bola3": 25, 
      "Bola4": 23, 
      "Bola5": 10, 
      "Bola6": 11, 
      "Bola7": 24, 
      "Bola8": 14, 
      "Bola9": 6, 
      "Bola10": 2, 
      "Bola11": 13, 
      "Bola12": 9, 
      "Bola13": 5, 
      "Bola14": 16, 
      "Bola15": 3, 
      "Arrecadacao_Total": "000", 
      "Ganhadores_15_Números": 5, 
      "Cidade": "null", 
      "UF": "SP", 
      "Ganhadores_14_Números": 154, 
      "Ganhadores_13_Números": 4645, 
      "Ganhadores_12_Números": 48807, 
      "Ganhadores_11_Números": 257593, 
      "Valor_Rateio_15_Números": "49.76582", 
      "Valor_Rateio_14_Números": 68984.0, 
      "Valor_Rateio_13_Números": 1000, 
      "Valor_Rateio_12_Números": 400, 
      "Valor_Rateio_11_Números": 200, 
      "Acumulado_15_Números": "000", 
      "Estimativa_Premio": "000", 
      "Valor_Acumulado_Especial": "000"
    }
  ]
}
```

