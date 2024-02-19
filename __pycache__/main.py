# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import pymysql # type: ignore

TABLE_NAME = 'customers'

connection = pymysql.connect(
    host = 'localhost',
    user = 'usuario',
    password = '123456',
    database= 'base_de_dados',
    charset='utf8mb4'
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(  # type: ignore
            'CREATE TABLE IF NOT EXISTS customers ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        print(cursor)
                # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  # type: ignore
        connection.commit()

    # Começo a manipular dados a partir daqui

    with connection.cursor() as cursor:
        sql = (f'INSERT INTO {TABLE_NAME} '
           '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        fulano = 'Luiz'
        idade  = 30 
        data = (fulano, idade)
        result = cursor.execute(sql, data)  # type: ignore
        print(sql, data)
        print(result)
    connection.commit()