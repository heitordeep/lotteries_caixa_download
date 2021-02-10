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
- [ ] API Pagination
- [X] App in the Docker

# :pushpin: Requirements:

Library: <img src='https://img.shields.io/badge/Requests-2.24.0-informational'> <img src='https://img.shields.io/badge/Pandas-1.1.0-informational'> 
<img src='https://img.shields.io/badge/Flask-1.1.2-informational'> <img src='https://img.shields.io/badge/Pymongo-3.10.1-informational'>
<br>
Linguage: <img src='https://camo.githubusercontent.com/2857442965ab9a51229c075102012bdbd340abc3/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f72657175657374733f6c6162656c3d507974686f6e266c6f676f3d505954484f4e266c6f676f436f6c6f723d79656c6c6f77267374796c653d706c6173746963'> <br>
Database: <img src="https://img.shields.io/badge/Docker-MongoDB-informational"><br><br>


- It is necessary to create an .env file with the following information: 
   - ```.env```:  <br>**URI=database** <br>**DATABASE=Choose a name**<br>

- Create images: <br>
  - Linux: <br>
    ```shell
    $ make start 
    ```

  - Windows: <br>
      ```shell
      $ docker-compose up -d
      ```
<br>

# :rocket: Run the command download files:
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

   - Command: <br>
        ```shell
        $ docker start caixa_download
        ```
        ```shell
        $ docker start bd_caixa_download
        ```
        
- Access endpoint:<br>
  - Web Page: http://0.0.0.0/web/
  - API: http://0.0.0.0/api/

<br>
  
- The data will be stored in the file and Mongodb.<br><br>
Consult File: <br><br>For Example: <br>
**raw/megasena/2020-08-14/files** - (Raw Data) html<br>
**swamp/megasena/2020-08-14/files** - (Raw Data) csv<br>
**lake/megasena/2020-08-14/files** - Final file.
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
  curl http://0.0.0.0/api/megasena?term=data_sorteio&search=09/01/1999
  ```

  ```shell
  curl http://0.0.0.0/api/megasena?term=acumulado&search=sim&limit=1
  ```

  - quina: 
  ```shell
  curl http://0.0.0.0/api/quina?limit=2
  ```

  ```shell 
  curl http://0.0.0.0/api/quina?term=uf&search=MG&page=7&limit=1
  ```
  
  - lotofacil:
  ```shell
  curl http://0.0.0.0/api/lotofacil?term=uf&search=SP&limit=1
  ```

## Result:

- megasena: <br>
```json
{
  "count_data": 1, 
  "documents": [
    {
      "_id": "60243dad35057afdd14504f9", 
      "concurso": "149", 
      "data_sorteio": "09/01/1999", 
      "1_dezena": "11", 
      "2_dezena": "45", 
      "3_dezena": "48", 
      "4_dezena": "7", 
      "5_dezena": "28", 
      "6_dezena": "20", 
      "arrecadacao_total": "000", 
      "ganhadores_sena": "0", 
      "cidade": "n/d", 
      "uf": "N/D", 
      "rateio_sena": "000", 
      "ganhadores_quina": "106", 
      "rateio_quina": "9.79513", 
      "ganhadores_quadra": "6290", 
      "rateio_quadra": "16474.0", 
      "acumulado": "sim", 
      "valor_acumulado": "2.211.82094", 
      "estimativa_prêmio": "000", 
      "acumulado_mega_da_virada": "000"
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
      "_id": "60243dad35057afdd1450463", 
      "concurso": "1", 
      "data_sorteio": "11/03/1996", 
      "1_dezena": "41", 
      "2_dezena": "5", 
      "3_dezena": "4", 
      "4_dezena": "52", 
      "5_dezena": "30", 
      "6_dezena": "33", 
      "arrecadacao_total": "000", 
      "ganhadores_sena": "0", 
      "cidade": "n/d", 
      "uf": "N/D", 
      "rateio_sena": "000", 
      "ganhadores_quina": "17", 
      "rateio_quina": "39.15892", 
      "ganhadores_quadra": "2016", 
      "rateio_quadra": "33021.0", 
      "acumulado": "sim", 
      "valor_acumulado": "1.714.65023", 
      "estimativa_prêmio": "000", 
      "acumulado_mega_da_virada": "000"
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
      "_id": "60243db835057afdd1452ff5", 
      "concurso": "1", 
      "data_sorteio": "13/03/1994", 
      "1_dezena": "25", 
      "2_dezena": "45", 
      "3_dezena": "60", 
      "4_dezena": "76", 
      "5_dezena": "79", 
      "arrecadacao_total": "000", 
      "ganhadores_quina": "3", 
      "cidade": "n/d", 
      "uf": "N/D", 
      "rateio_quina": "75.731.22500", 
      "ganhadores_quadra": "127", 
      "rateio_quadra": "1.788.92700", 
      "ganhadores_terno": "7030", 
      "rateio_terno": "42.982", 
      "ganhadores_duque": "0", 
      "rateio_duque": "0", 
      "acumulado": "não", 
      "valor_acumulado": "000", 
      "estimativa_premio": "000", 
      "valor_acumulado_sorteio_especial_são_joão": "000"
    }, 
    {
      "_id": "60243db835057afdd1452ff6", 
      "concurso": "2", 
      "data_sorteio": "17/03/1994", 
      "1_dezena": "13", 
      "2_dezena": "30", 
      "3_dezena": "58", 
      "4_dezena": "63", 
      "5_dezena": "64", 
      "arrecadacao_total": "000", 
      "ganhadores_quina": "1", 
      "cidade": "n/d", 
      "uf": "N/D", 
      "rateio_quina": "118.499.39700", 
      "ganhadores_quadra": "105", 
      "rateio_quadra": "1.128.56500", 
      "ganhadores_terno": "4861", 
      "rateio_terno": "32.422", 
      "ganhadores_duque": "0", 
      "rateio_duque": "0", 
      "acumulado": "não", 
      "valor_acumulado": "000", 
      "estimativa_premio": "000", 
      "valor_acumulado_sorteio_especial_são_joão": "000"
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
      "_id": "60243db835057afdd14530b1", 
      "concurso": "184", 
      "data_sorteio": "03/03/1996", 
      "1_dezena": "62", 
      "2_dezena": "22", 
      "3_dezena": "38", 
      "4_dezena": "29", 
      "5_dezena": "58", 
      "arrecadacao_total": "3.760.33000", 
      "ganhadores_quina": "2", 
      "cidade": "n/d", 
      "uf": "MG", 
      "rateio_quina": "173.72725", 
      "ganhadores_quadra": "244", 
      "rateio_quadra": "1.42399", 
      "ganhadores_terno": "11451", 
      "rateio_terno": "4046.0", 
      "ganhadores_duque": "0", 
      "rateio_duque": "0", 
      "acumulado": "não", 
      "valor_acumulado": "000", 
      "estimativa_premio": "240.00000", 
      "valor_acumulado_sorteio_especial_são_joão": "000"
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
      "_id": "60243db235057afdd1450e9d", 
      "concurso": "1", 
      "data_sorteio": "29/09/2003", 
      "bola1": "18", 
      "bola2": "20", 
      "bola3": "25", 
      "bola4": "23", 
      "bola5": "10", 
      "bola6": "11", 
      "bola7": "24", 
      "bola8": "14", 
      "bola9": "6", 
      "bola10": "2", 
      "bola11": "13", 
      "bola12": "9", 
      "bola13": "5", 
      "bola14": "16", 
      "bola15": "3", 
      "arrecadacao_total": "000", 
      "ganhadores_15_números": "5", 
      "cidade": "n/d", 
      "uf": "SP", 
      "ganhadores_14_números": "154", 
      "ganhadores_13_números": "4645", 
      "ganhadores_12_números": "48807", 
      "ganhadores_11_números": "257593", 
      "valor_rateio_15_números": "49.76582", 
      "valor_rateio_14_números": "68984.0", 
      "valor_rateio_13_números": "1000", 
      "valor_rateio_12_números": "400", 
      "valor_rateio_11_números": "200", 
      "acumulado_15_números": "000", 
      "estimativa_premio": "000", 
      "valor_acumulado_especial": "000"
    }
  ]
}
```