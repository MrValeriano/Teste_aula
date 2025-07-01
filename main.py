print("Olá turma do Python!")
print("Tudo bem?")
nome: str = input("Qual é o seu nome?\n> ")
try:
    idade = int(input("Qual é a sua idade?\n> "))
    print(f"Olá, {nome}! Você é {"maior" if idade >= 18 else "menor"} de idade!")
    if not 0 < idade <= 100: raise Exception
except ValueError:
    print("\nErro! A idade deve ser um número")
except Exception:
    print("\nErro! Número inválido!")