from src.rules.extrato import Extrato
from src.utils.database import Database


class ExtratoService:
    def __init__(self):
        self.extrato_database = Database("extratos")
        self.extrato_collection = self.extrato_database.collection

    def retorna_extrato(self, codigo_extrato: str):
        extrato = Extrato().consultar_extrato(codigo_extrato)
        if extrato is not None:
            return extrato

        extrato = Extrato().gerar_extato(codigo_extrato)
        return extrato
