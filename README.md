# Lotteries Caixa Download :moneybag:<br>
<img src='https://camo.githubusercontent.com/826560c5526525754718e6877d244af221d92634/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d696e666f726d6174696f6e616c'>
Extracted data with Python.


<br>

# :warning: Pending to resolve and Resolved:

- [X] Extract files
- [X] Create Web Page
- [X] Create API
- [X] Create API Documentation
- [ ] Fix data storage in Mongodb - (Delay)
- [X] Create data view with Mongodb 
- [X] API Pagination
- [X] App in the Docker

# :pushpin: Requirements:

Library: <img src='https://img.shields.io/badge/Requests-2.24.0-informational'> <img src='https://img.shields.io/badge/Pandas-1.1.0-informational'><br>
Linguage: <img src='https://camo.githubusercontent.com/2857442965ab9a51229c075102012bdbd340abc3/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f72657175657374733f6c6162656c3d507974686f6e266c6f676f3d505954484f4e266c6f676f436f6c6f723d79656c6c6f77267374796c653d706c6173746963'> <br>
Database: <img src="https://img.shields.io/badge/Docker-MongoDB-informational"><br><br>


- For Linux: <br><br>
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


- For Windows: <br><br>
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
   - For Linux: <br>
        ```shell
        $ make run search="Parameters"
        ```

   - For Windows:<br>
        ```shell
       $ python download.py "Parameters"
        ```
<br>

# :computer: Run Web Page and API:
- It is necessary to create an .env file with the following information: <br><br>
   - ```.env```:  <br>**DEBUG=False**<br>**MONGO_URI=database** <br>**MONGO_DATABASE=Choose a name** <br>

   - Command: <br>
        ```shell
        $ docker start {id}
        ```
- Access -> Web Page: http://0.0.0.0:5000/web/ or API: http://0.0.0.0:5000/api/

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

- Without Docker. The logs is in the directory: **log**

- With Docker:

  ```shell
  $ docker cp {id}:/app/log/ .
  ```

