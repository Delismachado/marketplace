from catalogo import Marketplace, Category, Subcategory, Dados

mktplaces = []
result_mktplaces = Dados.get_mktplaces()
for i in result_mktplaces:
    mktplaces.append(Marketplace(i['mktplace']))

categorias = []
result_cat = Dados.get_cat()
for i in result_cat:
    for j in mktplaces:
        if i['mkplace'] == j.get_name():
            categorias.append(Category(i['categoria'], j))

subcategorias = []
result_subcat = Dados.get_subcat()
for i in result_subcat:
    for j in categorias:
        if i['categoria'] == j.get_name():
            subcategorias.append(Subcategory(i['subcategoria'], j))
            break


def menu(): 

    print('\nMENU: ')

    i = 1
    for option in mktplaces:
        print(f'{i} - {option}')
        i += 1

    op = int(input('Choose an option: '))
    return op

while True:
    try:
        op = menu()
        if op == 0 :
            break
        marketplace_index = op - 1
        print(f'\nYour choice: {mktplaces[marketplace_index]}\n')
        Dados.log(f'Access to the marketplace category {mktplaces[marketplace_index]}')

        # function: get_categories(mktplaces[marketplace_index]) || OO: mktplaces[marketplace_index].get_categories()
        market_categories = []
        for i in categorias:
            if i.get_parentname() ==  mktplaces[marketplace_index].get_name():
                market_categories.append(i)
        if len(market_categories) == 0 :
            continue

        for i, category in enumerate(market_categories):
            print(f'{i + 1} - {category.get_name()}')
        escolher_cat = int(input(f'\nChoose an option: '))
        category_index = escolher_cat - 1

        # function: get_subcategories(market_categories[category_index]) || OO: market_categories[category_index].get_subcategories()
        category_subcategories = []
        for i in subcategorias:
            if i.get_parentname() ==  market_categories[category_index].get_name():
                category_subcategories.append(i)

        print(f'\n Sub categories:')
        for i, subcategories in enumerate(category_subcategories):
            print(f'{i + 1} - {subcategories.get_subcat()}')

    except ValueError:
        print('Option unavailable. Try again.')

"""
while true:
  market = choose_market(markets)
  category = choose_category(market.get_categories())
  list_subcategories(category.get_subcategories())
"""
"""
while true:
  market = choose_market(markets)
  category = choose_category(get_categories(market))
  list_subcategories(get_subcategories(category))
"""