import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title, search_by_date, search_by_category)
from tech_news.analyzer.ratings import top_5_categories


# Requisitos 11 e 12  https://www.w3schools.com/python/python_lambda.asp
def analyzer_menu():
    """Seu código deve vir aqui"""
    print('Selecione uma das opções a seguir:\n'
          ' 0 - Popular o banco com notícias;\n'
          ' 1 - Buscar notícias por título;\n'
          ' 2 - Buscar notícias por data;\n'
          ' 3 - Buscar notícias por categoria;\n'
          ' 4 - Listar top 5 categorias;\n'
          ' 5 - Sair.')
    opt = input('')

    func = {
        '0': lambda: get_tech_news(
            int(input('Digite quantas notícias serão buscadas:'))
        ),
        '1': lambda: search_by_title(
            input('Digite o título:')
        ),
        '2': lambda: search_by_date(input('Digite a data YYYY-MM-DD')),
        '3': lambda: search_by_category(input('Digite a categoria:')),
        '4': lambda: top_5_categories(),
        '5': lambda: print('Encerrando script')
    }

    if opt in func:
        return func[opt]()

    print('Opção inválida', file=sys.stderr)
