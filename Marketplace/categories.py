import subCategories

class Category:

        def __init__(self, id: int, name: str):
                self.__id = id
                self.__name = name
                self.__subCategories = subCategories


        def set_id(self, id: int) -> None:
                self.__id = int(id)

        def get_id(self) -> int:
                return self.__id


        def set_name(self, name: str) -> None:
                self.__name = name 

        def get_name(self) -> str:
                return self.__name
        
        def set_subCategory(self, name: str) -> None:
                self.__subCategories = subCategories 

        def get_subCategory(self) -> str:
                return self.__subCategories 
        


        def __str__(self):
                return f"""
                        Id: {self.get_id()}
                        Name: {self.get_name()}
                        SubCategory: {self.get_subCategory()}            
                        """


