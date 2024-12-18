
def calcula_digito_verificador(numero, ordem_digito_verificador):
    
    soma = 0
    numero = numero[::-1]#inverte para somar os valores corretamente
    for x in range(2,ordem_digito_verificador+10):
        soma += int(numero[x-2]) * x
    return soma
	
def verifica_digito_validador(digito):
    if (digito % 11) >= 2:
        digito = 11 - (digito % 11)
    else:
        digito = 0
    return digito
	
def valida_cpf(cpf_value):
    digito_um = calcula_digito_verificador(cpf_value[:-2], 1)
    digito_um_verificado = verifica_digito_validador(digito_um)
	
    digito_dois = calcula_digito_verificador(cpf_value[:-2]+str(digito_um_verificado), 2)
    digito_dois_verificado = verifica_digito_validador(digito_dois)
    
    cpf_validado = str(cpf_value[:-2])+str(digito_um_verificado)+str(digito_dois_verificado)
    
    if cpf_value == cpf_validado:
        return {"cpf_value":"cpf válido"}
    return {"cpf_value":"cpf inválido"}
	
