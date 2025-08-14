import re

#isso é opcional para enviar somente para numeros brasileiros

def format_phone(number: str):
    if not number:
        return ""
    clean_number = re.sub(r"\D", "", number)

    if clean_number.startswith("55"):
        return clean_number
    
    if clean_number.startswith("0"):
        return clean_number
    
    return f"55{clean_number}"
