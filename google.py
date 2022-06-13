from googlesearch import search

#Criando o texto de busca
query = 'batman'

#Fazendo a busca
result = list(
    search(
        query,
        lang='pt-br',
        num_results=5
    )
)

#Mostrando resultados
print(result)