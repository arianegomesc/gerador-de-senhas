import random
import string

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_digitos=True, usar_simbolos=True):
    """
    Gera uma senha aleatória baseada nas opções fornecidas.
    """
    caracteres = ""

    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_digitos:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Selecione pelo menos um tipo de caractere.")

    return ''.join(random.choice(caracteres) for _ in range(tamanho))
