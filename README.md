# Lotteries Caixa Download :moneybag:<br>
<img src='https://camo.githubusercontent.com/826560c5526525754718e6877d244af221d92634/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d696e666f726d6174696f6e616c'>
Extracted data with Python.


<br>

# :warning: Pending to resolve and Resolved:

- [X] Extract files
- [X] Create Web Page
- [X] Create API
- [X] Create API Documentation
- [ ] Fix data entry in Mongodb
- [ ] Create data view with Mongodb 
- [ ] API Pagination


# :pushpin: Requirements:

Library: <img src='https://img.shields.io/badge/Requests-2.24.0-informational'> <img src='https://img.shields.io/badge/Pandas-1.1.0-informational'><br>
Linguage: <img src='https://camo.githubusercontent.com/2857442965ab9a51229c075102012bdbd340abc3/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f72657175657374733f6c6162656c3d507974686f6e266c6f676f3d505954484f4e266c6f676f436f6c6f723d79656c6c6f77267374796c653d706c6173746963'> <br>
Database: <img src="https://img.shields.io/badge/docker-mongodb-informational">

- For Linux: <br>
   Installation requirements:<br>
    ```shell
    $ make requirements 
    ```

    and 

    ```shell
    $ make up 
    ```


- For Windows: <br>
   Create venv and Installation requirements:<br>
     ```shell
     $ create_venv.bat
     ```
    and

   ```shell
  $ pip install -r requirements/requirements_dev.txt
    ```

    and

    ```shell
    $ docker-compose up -d 
    ```

# :rocket: Run the command:
- Parameters: megasena, quina or lotofacil. For example: <br>
   - For Linux: <br>
        ```shell
        $ make run search=quina
        ```

   - For Windows:<br>
        ```shell
       $ python download.py.py quina
        ```
<br>

# :computer: Run Web Page and API:
- It is necessary to create an .env file with the following information: <br><br>
   - ```.env```:  <br>**DEBUG=True**<br>**MONGO_URI=127.0.0.1** <br>**MONGO_DATABASE=Choose a name** <br>**COLLECTION=Choose a name**

   - For Linux: <br>
        ```shell
        $ make runserver
        ```

   - For Windows:<br>
        ```shell
       $ python run.py
        ```
- Access -> Web Page: http://127.0.0.1:5000/web/ or API: http://127.0.0.1:5000/api/ 

<br>
  
The data will be stored in the file.<br>
For Example: <br>
**raw/megasena/2020-08-14/files** - (Raw Data) html<br>
**swamp/megasena/2020-08-14/files** - (Raw Data) csv<br>
**lake/megasena/2020-08-14/files**
<br>

Result directories:<br>

<img src='https://user-images.githubusercontent.com/17969551/90266677-b97a1580-de2a-11ea-8930-131a304ab4d6.png' width='400'>
<br>

Example the path file:<br>
<img src='https://user-images.githubusercontent.com/17969551/90266840-04942880-de2b-11ea-9007-a127c0b241fc.png' width='500'>

# Do you need help with commands?

- Linux only
<img src='https://user-images.githubusercontent.com/17969551/89588975-208c3e80-d81b-11ea-9ba6-2fb460deca4b.png' width='600'>
