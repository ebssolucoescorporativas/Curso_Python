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
        # print(cursor)
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
        # print(sql, data)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data2 = {
            "age": 37,
            "name": "Le",
        }
        result = cursor.execute(sql, data2)  # type: ignore
        # print(sql)
        # print(data2)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data3 = (
            {"name": "Sah", "age": 33, },
            {"name": "Júlia", "age": 74, },
            {"name": "Rose", "age": 53, },
        )
        result = cursor.executemany(sql, data3)  # type: ignore
        # print(sql)
        # print(data3)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data4 = (
            ("Siri", 22, ),
            ("Helena", 15, ),
        )
        result = cursor.executemany(sql, data4)  # type: ignore
        # print(sql)
        # print(data2)
        # print(data4)
        # print(result)
    connection.commit()

    # # Lendo os valores com SELECT
    # with connection.cursor() as cursor:
    #     sql = (
    #         f'SELECT * FROM {TABLE_NAME} '
    #     )
    #     cursor.execute(sql)  # type: ignore
    #     data5 = cursor.fetchall()  # type: ignore

    #     for row in data5:
    #         print(row)

    # Lendo os valores com SELECT
    with connection.cursor() as cursor:
        menor_id = int(input('Digite o menor id: '))
        maior_id = int(input('Digite o maior id: '))

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s  '
        )
        # cursor.execute(sql)  # type: ignore

        cursor.execute(sql, (menor_id, maior_id))  # type: ignore
        print(cursor.mogrify(sql, (menor_id, maior_id)))  # type: ignore
        data6 = cursor.fetchall()  # type: ignore

        for row in data6:
            print(row)

    # Apagando com DELETE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s'
        )
        print(cursor.execute(sql, (1,)))  # type: ignore
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')  # type: ignore

        for row in cursor.fetchall():  # type: ignore
            print(row)