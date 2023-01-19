from fastapi import APIRouter


router = APIRouter(prefix="/despesarecorrente", tags=["despesa_recorrente"])


@router.get("/{identificador}")
async def resgata_despesa_recorrente(identificador: str):
    pass


@router.get("/")
async def resgata_despesas_recorrentes():
    pass


@router.put("/{identificador}")
async def atualiza_despesa_recorrente(identificador: str):
    pass


@router.delete("/{identificador}")
async def deleta_despesa_recorrente(identificador: str):
    pass


@router.post("/")
async def cria_despesa_recorrente(despesa_recorrente):
    pass
