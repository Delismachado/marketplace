import categories

class Marketplace:

        def __init__(self, id: int, name: str):
                self.__id = id
                self.__name = name
                self.__categories = categories        



def get_id(self) -> int:
        return self.__id

def set_id(self, id: int) -> None:
        self.__id = id


def get_name(self) -> str:
        return self.__name    
        
def set_name(self, name: str) -> None:
        self.__name = name

def get_categories(self) -> list:
        return self.__categories

def set_categories(self, categories:str) -> None:
        self.__categories = categories


def __str__(self):
    return f"""
            Id: {self.get_id()}
            Name: {self.get_name()}
            Category: {self.get_categories()}
            subCategories: {self.get_subCategories()}            
            """