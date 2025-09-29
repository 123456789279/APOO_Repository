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
    def get_id(self, id):
        return id
    def get_descricao(self, descricao):
        return descricao
    def get_quantidade(self, quantidade):
        return quantidade
    def __str__(self):
        return f"{self.__id}-{self.__descricao}-{self.__quantidade}"
    def to_json(self):
        dic = {"id":self.__id, "descricao":self.__descricao,"quantidade":self.__quantidade}
        return dic
    @staticmethod
    def from_json(dic):
        return Item(dic["id"], dic["descricao"], dic["quantidade"])
    
import json

class ItemDAO():
   __objetos = []
   @classmethod
   def inserir(cls, obj):
     cls.abrir()
     id = 0
     for aux in cls.__objetos:
       if aux.get_id() > id: id = aux.get_id()
     obj.set_id(id +1)
     cls.__objetos.append(obj)
     cls.salvar()
   
   @classmethod
   def listar(cls):
     cls.abrir()
     return cls.__objetos

   @classmethod
   def listar_id(cls, id):
     cls.abrir()
     for obj in cls.__objetos:
       if obj.get_id() == id: return obj
     return None
  
   @classmethod
   def atualizar(cls, obj):
     aux = cls.listar_id(obj.get_id())
     if aux != None:
       cls.__objetos.remove(aux)
       cls.__objetos.append(obj)
       cls.salvar()

   @classmethod
   def excluir(cls, obj):
     aux = cls.listar_id(obj.get_id())
     if aux != None:
       cls.__objetos.remove(aux)
       cls.salvar()

   @classmethod
   def abrir(cls):
     cls.__objetos = []
     try:
       with open("item.json", mode="r") as arquivo:
         list_dic = json.load(arquivo)
         for dic in list_dic:
           obj = Item.from_json(dic)
           cls.__objetos.append(obj)
     except FileNotFoundError:
       pass

   @classmethod
   def salvar(cls):
     with open("item.json", mode="w") as arquivo:
       json.dump(cls.__objetos, arquivo, default = Item.to_json)