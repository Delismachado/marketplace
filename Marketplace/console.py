from catalogo import Marketplace, Category, Subcategory

marketplaces = [Marketplace('Enjoei'), Marketplace('BigCommerce'), Marketplace('Etsy'), Marketplace('Evolutto'), Marketplace('Sair')]
categories = [Category('Home', marketplaces[1]), Category('Dinner', marketplaces[0]), Category('Food', marketplaces[1])]
subcategories = [Subcategory('Lunch', categories[0]), Subcategory('Style', categories[0]), Subcategory('Go', categories[1])]

def menu(): 

    print('\nMENU: ')

    i = 1
    for option in marketplaces:
        print(f'{i} - {option}')
        i += 1

    op = int(input('Choose an option: '))
    return op

while True:
    try:
        op = menu()
        if op == 1:
            item = 1
            print(f'\nYour choice! {marketplaces[0]}\n')
            for i in categories:
                if i.get_parentname() ==  marketplaces[0].get_name():
                    print(f'{item} - {i.get_name()}')
                    item += 1
            choose_cat = int(input(f'\nChoose a category: '))
            while True:
                try:
                    if choose_cat == 1:
                        for i in subcategories:
                            if i.get_parentname() == categories[1].get_name():
                                print(f'\nCategory options:')
                                print(f'\n{i.get_subcat()}')
                        break
                except Exception as e: 
                    print(e)
                    break
                
        elif op == 2:
            item = 1
            print(f'\nYour choice! {marketplaces[1]}\n')
            for i in categories:
                if i.get_parentname() ==  marketplaces[1].get_name():
                    print(f'{item} - {i.get_name()}')
                    item += 1
            choose_cat = int(input(f'\nChoose a category: '))
            while True:
                try:
                    if choose_cat == 1:
                        for i in subcategories:
                            if i.get_parentname() == categories[0].get_name():
                                print(f'\n{i.get_subcat()}')

                        break
                except Exception as e: 
                    print(e)
                    break
                
        elif op == 3:
            item = 1
            print(f'\nYour choice! {marketplaces[2]}\n')
            for i in categories:
                if i.get_parentname() ==  marketplaces[2].get_name():
                    print(f'{item} - {i.get_name()}')
                    item += 1
            choose_cat = int(input(f'\nChoose a category: '))
            while True:
                try:
                    if choose_cat == 1:
                        for i in subcategories:
                            if i.get_parentname() == categories[0].get_name():
                                print(f'\n{i.get_subcat()}')
                        break
                except Exception as e: 
                    print(e)
                    break

        elif op == 4:
            item = 1
            print(f'\nYour choice {marketplaces[3]}\n')
            for i in categories:
                if i.get_parentname() ==  marketplaces[3].get_name():
                    print(f'{item} - {i.get_name()}')
                    item += 1
            choose_cat = int(input(f'\nChoose a category: '))
            while True:
                try:
                    if choose_cat == 1:
                        for i in subcategories:
                            if i.get_parentname() == categories[0].get_name():
                                print(f'\n{i.get_subcat()}')
                        break
                except Exception as e: 
                    print(e)
                    break
            
        elif op == 5:
            exit(0)
        else:
            print('Enter a valid option.!')
        break

    except ValueError:
        print('Option unavailable. Try again.')