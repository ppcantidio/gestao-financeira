from src.utils.database import Database
from bson.objectid import ObjectId
import datetime


class DespesaRecorrente:
    def __init__(self, id_usuario):
        self.id_usuario = ObjectId(id_usuario)

        self.db = Database("despesas_recorrentes")
        self.db_extrato = Database("extratos")
        self.collection_extrato = self.db_extrato.collection
        self.collection = self.db.collection

    def cria_despesa_recorrente(self, despesa_recorrente):
        self.collection.insert_one(despesa_recorrente)
        return despesa_recorrente

    # def atualiza_despesa_recorrente(self, id, despesa_recorrente):
