from fastapi import FastAPI
from . import cpf
import re

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
	
@app.get("/validaCPF/{cpf_value}")
async def read_item(cpf_value: str):
    """
    Considerar a mascara de cpf sem pontuação.
    validação https://www.macoratti.net/alg_cpf.htm
    """
    
    if len(cpf_value) == 11:
        cpf_value_normalized = re.sub('[^0-9]', '', cpf_value)
        
        if len(cpf_value_normalized[:11])==11:
            return {"cpf_value":cpf.valida_cpf(cpf_value)}

    return {"cpf_value": "cpf inválido"}