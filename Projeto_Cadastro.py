import random
import datetime

# Obtenção do nome do usuário
nome = input("Digite o seu nome: ")

# Obtenção da idade do usuário
idade = input("Digite a sua idade: ")

# Registro automático da data de cadastro
data_registro = datetime.date.today()

# Seleção aleatória do cartão a ser recebido pelo usuário
cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
cartao_sorteado = random.choice(cartoes)

# Impressão das informações do usuário e do cartão sorteado
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Data de registro: {data_registro}")
print(f"Cartão sorteado: {cartao_sorteado}")

# Geração da mensagem de boas-vindas personalizada
mensagem = f"Olá {nome}, seu registro foi concluído com sucesso no dia {data_registro.strftime('%d/%m/%Y')}. Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao_sorteado}!"

# Impressão da mensagem de boas-vindas e das informações do usuário
print(mensagem)
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Data de registro: {data_registro}")
print(f"Cartão sorteado: {cartao_sorteado}")