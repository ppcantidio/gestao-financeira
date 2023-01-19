from fastapi import APIRouter


router = APIRouter(prefix="/receitarecorrente", tags=["receita_recorrente"])


@router.get("/{identificador}")
async def resgata_receita_recorrente(identificador: str):
    pass


@router.get("/")
async def resgata_receitas_recorrentes():
    pass


@router.put("/{identificador}")
async def atualiza_receita_recorrente(identificador: str):
    pass


@router.delete("/{identificador}")
async def deleta_receita_recorrente(identificador: str):
    pass


@router.post("/")
async def cria_receita_recorrente(receita_recorrente):
    pass
