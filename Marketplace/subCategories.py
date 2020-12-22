class SubCategory(Category):
        def __init__(self, id: int, name: str):
                self.__id = id
                self.__name = name               
        
        def set_id(self, id: int) -> None:
                self.__id = int(id)

        def get_id(self) -> int:
                return self.__id


        def set_name(self, name: str) -> None:
                self.__name = name 

        def get_name(self) -> str:
                return self.__name


        def __str__(self):
                return f"""
                        Id: {self.id()}
                        Name: {self.name()}                        
                        """