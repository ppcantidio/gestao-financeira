from pydantic import BaseModel
import datetime


class ReceitaModel(BaseModel):
    recorrente: bool
    valor: bool
    dt_pagamento: datetime.date
    nome: str
    categoria: str
