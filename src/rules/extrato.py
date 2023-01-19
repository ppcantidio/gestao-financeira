from src.rules.despesa_recorrente import DespesaRecorrente
from src.rules.receita_recorrente import ReceitaRecorrente
from src.utils.database import Database
from src.rules.usuario import Usuario
import datetime
from bson.objectid import ObjectId


class Extrato:
    def __init__(self, id_usuario):
        self.id_usuario = ObjectId(id_usuario)

        self.db = Database("extratos")
        self.collection = self.db.collection

    def consultar_extrato(self, codigo_extrato: str) -> dict:
        extrato = self.collection.find_one({"codigo": codigo_extrato, "id_usuario": self.id_usuario})
        return extrato

    def gerar_extato(self, codigo_extrato: str) -> dict:
        """
        insere recorrencias e gera extrato
        """
        if self.consultar_extrato(codigo_extrato) is not None:
            return {"erro": "ja existe um extrato gerado"}

        mes = int(codigo_extrato[0:2])
        ano = int(codigo_extrato[2:6])

        despesas_recorrentes = DespesaRecorrente(self.id_usuario).retorna_despesas_recorrentes()
        receitas_recorrentes = ReceitaRecorrente(self.id_usuario).retorna_receitas_recorrentes()

        dia_fechamento = Usuario(self.id_usuario).retorna_dia_fechamento()

        dt_fechamento = str(datetime.date(ano, mes, dia_fechamento))
        dt_inicio = str(datetime.date(ano, mes + 1, dia_fechamento))

        extrato = {
            "codigo": codigo_extrato,
            "id_usuario": self.id_usuario,
            "dt_inicio": dt_inicio,
            "dt_fechamento": dt_fechamento,
            "ls_receita": despesas_recorrentes,
            "ls_despesa": receitas_recorrentes,
            "nr_mes": mes,
            "nr_ano": ano,
        }

        self.__calcula_valores_extrato(extrato)

        self.collection.insert_one(extrato)

        return extrato

    def __calcula_valores_extrato(self, extrato: dict):
        receitas = extrato.get("ls_receita", [])
        despesas = extrato.get("ls_despesa", [])

        valor_total_receitas = self.__calcula_total(receitas)
        valor_total_despesas = self.__calcula_total(despesas)
        saldo = valor_total_receitas - valor_total_despesas

        extrato["vl_total_receitas"] = valor_total_receitas
        extrato["vl_total_despesas"] = valor_total_despesas
        extrato["saldo"] = saldo

    def adicionar_despesa(self, codigo_extrato: str, despesa: dict):
        extrato = self.consultar_extrato(codigo_extrato)
        extrato["ls_despesa"] += despesa
        self.collection.update_one(
            filter={"codigo": codigo_extrato, "id_usuario": self.id_usuario}, update={"$set": extrato}, upsert=True
        )
        return extrato

    def adicionar_receita(self, codigo_extrato: str, receita: dict):
        extrato = self.consultar_extrato(codigo_extrato)
        extrato["ls_receita"] += receita
        self.__atualiza_extrato(extrato)
        return extrato

    def atualiza_extratos_com_despesa_recorrente(self, despesa_recorrente):
        hoje = datetime.datetime.now()

        extratos = list(self.collection.find({"dt_fechamento": {"$gte": hoje}}))
        for extrato in extratos:
            in_despesa_atualizada = self.__atualiza_despesa(despesa_recorrente, extrato)
            if in_despesa_atualizada is False:
                extrato["ls_despesa"].append(despesa_recorrente)

            self.__calcula_valores_extrato(extrato)
            self.__atualiza_extrato(extrato)

        return extratos

    def atualiza_extratos_com_receita_recorrente(self, receita_recorrente):
        hoje = datetime.datetime.now()

        extratos = list(self.collection.find({"dt_fechamento": {"$gte": hoje}}))
        for extrato in extratos:
            receita_atualizada = self.__atualiza_receita(receita_recorrente, extrato)
            if receita_atualizada is False:
                extrato["ls_receita"].append(receita_recorrente)

            self.__calcula_valores_extrato(extrato)
            self.__atualiza_extrato(extrato)

        return extratos

    def __atualiza_despesa(self, despesa_a_atualizar, extrato):
        for despesa in extrato.get("ls_despesa", []):
            if despesa.get("identificador", 1) == despesa_a_atualizar.get("identificador", 0):
                despesa = despesa_a_atualizar
                return True
        return False

    def __atualiza_receita(self, receita_a_atualizar, extrato):
        for receita in extrato.get("ls_receita", []):
            if receita.get("identificador", 1) == receita_a_atualizar.get("identificador", 0):
                receita = receita_a_atualizar
                return True
        return False

    def __atualiza_extrato(self, extrato):
        self.collection.update_one({"_id": extrato.get("_id")}, update={"$set": extrato})

    def __calcula_total(self, itens_extrato):
        total = 0
        for item in itens_extrato:
            total += item.get("valor", 0)
        return total
