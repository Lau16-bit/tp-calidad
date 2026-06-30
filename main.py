import requests
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def obtener_usuario(id_usuario):
    url = f"https://jsonplaceholder.typicode.com/users/{id_usuario}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# TP7 - Gestión de Calidad - 2026
