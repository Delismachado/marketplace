import datetime
class Marketplace:
    def __init__(self, Marketplace: str):
        self.__namemkp = Marketplace

    def get_name(self) -> str:
        return self.__namemkp

    def __str__(self) -> str:
        return f'''{self.__namemkp}'''


class Category:
    def __init__(self, Category: str, Marketplace: Marketplace):
       self.__catmkp = Category
       self.__parent = Marketplace

    def get_name(self) -> str:
        return self.__catmkp

    def get_parentname(self) -> str:
        return self.__parent.get_name()


class Subcategory:
    def __init__(self, Subcategory: str, Category: Category):
        self.__subcat = Subcategory
        self.__parent = Category

    def get_subcat(self) -> str:
        return self.__subcat
    
    def get_parentname(self) -> str:
        return self.__parent.get_name()


class Dados:

    def set_maktplaces(self, mkplaces):
        arq = open('dados/mkplaces.txt', 'a')        
        arq.write(f'\n{mkplaces}')       


    def get_mktplaces() -> list:
        mktplaces = []
        arq = open('dados/mkplaces.txt', 'r')
        for i in arq:
            i = i.strip()
            i = {'mktplace':i} 
            mktplaces.append(i)
        arq.close()
        return mktplaces

    def set_cat(mkplaces, categoria):
        arq = open('dados/categorias.txt', 'a')
        arq.write(f'\n{mkplaces};{categoria}')

    def get_cat():
        cat = []
        arq = open('dados/categorias.txt', 'r')
        for i in arq:
            i = i.strip()
            j = i.split(';')
            i = {'categoria':j[1], 
                'mkplace':j[0]
            } 
            cat.append(i)
        arq.close()
        return cat


    def set_subcat(categorias, subcategorias):
        arq = open('dados/subcategorias.txt', 'a')
        arq.write(f'\n{categorias};{subcategorias}')

        
    def get_subcat():
        subcat = []
        arq = open('dados/subcategorias.txt', 'r')
        for i in arq:
            i = i.strip()
            j = i.split(';')
            i = {'subcategoria':j[1], 
                'categoria':j[0]
            } 
            subcat.append(i)
        arq.close()
        return subcat

    def log(acao):
        arquivo = open('dados/log.txt', 'a')
        l = datetime.datetime.now()
        l = l.strftime("%d /%m /%y access the %H:%M h/m.")
        arquivo.write(f'{l} {acao}\n')
        arquivo.close()


