from fastapi import APIRouter, Request, Depends
from pydantic import create_model
from src.services.extrato_service import ExtratoService
from src.utils.responses import response_error


router = APIRouter(prefix="/extrato", tags=["extrato"])


@router.get("/{codigo_extrato}")
async def retorna_extrato(codigo_extrato: str):
    if codigo_extrato is None:
        return response_error("O codigo do extrato não pode ser nulo")

    retorno = ExtratoService().retorna_extrato(codigo_extrato)
    return retorno


@router.post("/{codigo_extrato}/despesa")
async def adiciona_despesa(codigo_extrato: str):
    pass


@router.put("/{codigo_extrato}/despesa/{identificador}")
async def atualiza_despesa(codigo_extrato: str, identificador: str):
    pass


@router.delete("/{codigo_extrato}/despesa/{identificador}")
async def deleta_despesa(codigo_extrato: str, identificador: str):
    pass


@router.post("/{codigo_extrato}/receita")
async def adiciona_receita(codigo_extrato: str):
    pass


@router.put("/{codigo_extrato}/receita/{identificador}")
async def atualiza_receita(codigo_extrato: str, identificador: str):
    pass


@router.delete("/{codigo_extrato}/receita/{identificador}")
async def deleta_receita(codigo_extrato: str, identificador: str):
    pass
