from pydantic import BaseModel
from typing import Optional
import datetime


class ReceitaModel(BaseModel):
    recorrente: bool
    valor: bool
    dt_pagamento: datetime.date
    nome: str
    categoria: str
    cartao_credito: Optional[str] = None
