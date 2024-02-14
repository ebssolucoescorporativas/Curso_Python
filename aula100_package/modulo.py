def aumenta_10_por_cento(listas):


    return [
         {**produto, 'preco': round(produto['preco'] * 1.10,2)}
        for produto in listas
    ]

