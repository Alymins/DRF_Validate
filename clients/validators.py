import re
from validate_docbr import CPF

def valid_name(name: str) -> bool:
    return name.isalpha()
        
def valid_cpf(cpf_number: str) -> bool:
    cpf = CPF()
    return cpf.validate(cpf_number)
    
def valid_rg(rg: str) -> bool:
    return len(rg) == 9
    
def valid_phone(phone: str) -> bool:
    """Validate phone number format (99 99999-9999)"""
    regex = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    return re.findall(regex, phone)

    