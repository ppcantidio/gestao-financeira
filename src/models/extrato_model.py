from typing import Union, Dict, Optional
from pydantic import BaseModel, EmailStr, Field
import datetime
from bson.objectid import ObjectId as BsonObjectId


class Despesa(BaseModel):
    nm_identificador_despesa = str


class Receita(BaseModel):
    nm_identificador_receita = str


class ExtratoDB(BaseModel):
    ls_despesa: Despesa
    ls_receita: Receita
    dt_inicio: datetime.date
    dt_fechamento = datetime.date
