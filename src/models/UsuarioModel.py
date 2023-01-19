from typing import Union, Dict, Optional
from pydantic import BaseModel, EmailStr, Field
import datetime
from bson.objectid import ObjectId as BsonObjectId


class PydanticObjectId(BsonObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, BsonObjectId):
            raise TypeError("ObjectId required")
        return str(v)


class ConfiguracaoUsuario(BaseModel):
    dt_fechamento: datetime.date


class UsuarioEntradaDB(BaseModel):
    nome: str
    email: str
    senha_criptografada: str
    configuracao_usuario: ConfiguracaoUsuario


class UsuarioSaidaDB(UsuarioEntradaDB):
    id: PydanticObjectId = Field(..., alias="_id")


inserir_usuario_banco = {
    "_id": BsonObjectId("123456781234567812345678"),
    "nome": "Pedro Cantidio",
    "email": "ppcantidio@gmail.com",
    "senha_criptografada": "#uMaSeNhaqualquer55678",
    "configuracao_usuario": {"dt_fechamento": datetime.date.today()},
}

m = UsuarioSaidaDB(**inserir_usuario_banco)
m = m.dict()
print(type(m.get("id")))
