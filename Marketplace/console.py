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
        if op == 1:
            item = 1
            print(f'\nYour choice: {mktplaces[0]}\n')
            Dados.log(f'Access to the marketplace category {mktplaces[0]}')
            for i in categorias:
                if i.get_parentname() ==  mktplaces[0].get_name():
                    print(f'{item} - {i.get_name()}')
                    item += 1
            escolher_cat = int(input(f'\nChoose an option: '))
            while True:
                try:
                    if escolher_cat == 1:
                        for i in subcategorias:
                            if i.get_parentname() == categorias[1].get_name():
                                print(f'\n Categories:')
                                print(f'\n{i.get_subcat()}')
                        break
                except Exception as e: 
                    print(e)
                    break
                
        elif op == 2:
            item = 1
            print(f'\nYour option: {mktplaces[1]}\n')
            Dados.log(f'Access to the marketplace category {mktplaces[1]}')
            for i in categorias:
                if i.get_parentname() ==  mktplaces[1].get_name():
                    print(f'{item} - {i.get_name()}')
                    item += 1
            escolher_cat = int(input(f'\nChoose an option: '))
            while True:
                try:
                    if escolher_cat == 1:
                        print('Categorias:')
                        for i in subcategorias:                            
                            if i.get_parentname() == categorias[1].get_name():
                                print(f'\n{i.get_subcat()}')
                            break
                except Exception as e: 
                    print(e)
                    break
                
        elif op == 3:
            item = 1
            print(f'\nVocê escolheu a opção {mktplaces[2]}\n')
            Dados.log(f'Access to the marketplace category {mktplaces[2]}')
            for i in categorias:
                if i.get_parentname() ==  mktplaces[2].get_name():
                    print(f'{item} - {i.get_name()}')
                    item += 1
            escolher_cat = int(input(f'\nChoose an option for category: '))
            while True:
                try:
                    if escolher_cat == 1:
                        for i in subcategorias:
                            if i.get_parentname() == categorias[1].get_name():
                                print(f'\n{i.get_subcat()}')
                        break
                except Exception as e: 
                    print(e)
                    break

        elif op == 4:
            item = 1
            print(f'\nYour option: {mktplaces[3]}\n')
            Dados.log(f'Access to the marketplace category {mktplaces[3]}')
            for i in categorias:
                if i.get_parentname() ==  mktplaces[3].get_name():
                    print(f'{item} - {i.get_name()}')
                    item += 1
            escolher_cat = int(input(f'\nChoose an option: '))
            while True:
                try:
                    if escolher_cat == 1:
                        for i in subcategorias:
                            if i.get_parentname() == categorias[0].get_name():
                                print(f'\n{i.get_subcat()}')
                            break
                except Exception as e: 
                    print(e)
                    break
            
        elif op == 5:
            exit(0) 
        else:
            print('Please enter a valid option!')
        break

    except ValueError:
        print('Option unavailable. Try again.')