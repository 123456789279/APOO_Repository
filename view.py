from item import Item, ItemDAO
class View:
   def item_inserir(data, confirmado, id_cliente, id_servico):
     c = Item(0, data)
     c.set_confirmado(confirmado)
     c.set_id_cliente(id_cliente)
     c.set_id_servico(id_servico)
     ItemDAO.inserir(c)
   def item_listar():
     return ItemDAO.listar()
   def item_atualizar(id, data, confirmado, id_cliente, id_servico):
     c = Item(id, data)
     c.set_confirmado(confirmado)
     c.set_id_cliente(id_cliente)
     c.set_id_servico(id_servico)
     ItemDAO.atualizar(c)
   def item_excluir(id):
     c = Item(id, None)
     ItemDAO.excluir(c)