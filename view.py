from item import Item, ItemDAO
class View:
   def item_inserir(data, confirmado, id_descricao, id_quantidade):
     c = Item(0, data)
     c.set_confirmado(confirmado)
     c.set_id_descricao(id_descricao)
     c.set_id_quantidade(id_quantidade)
     ItemDAO.inserir(c)
   def item_listar():
     return ItemDAO.listar()
   def item_atualizar(id, data, confirmado, id_descricao, id_quantidade):
     c = Item(id, data)
     c.set_confirmado(confirmado)
     c.set_id_descricao(id_descricao)
     c.set_id_quantidade(id_quantidade)
     ItemDAO.atualizar(c)
   def item_excluir(id):
     c = Item(id, None)
     ItemDAO.excluir(c)