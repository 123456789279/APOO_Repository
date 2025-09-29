class Item:
    def __init__(self, id, descricao, quantidade):
        self.__id = 0
        self.__descricao = ""
        self.__quantidade = 0
    def set_id(self, id):
        self.__id = id
    def set_descricao(self, descricao):
        self.__descricao = descricao
    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade
    def get_id(self):
        return id
    def get_descricao(self):
        return descricao
    def get_quantidade(self):
        return quantidade
    def __str__(self):
        return f"{self.__id}-{self.__descricao}-{self.__quantidade}"