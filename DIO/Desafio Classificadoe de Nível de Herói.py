# Definindo a função para classificar o herói
def classificar_heroi(nome, xp):
# Estruturas de decisão para determinar o nível do herói
  if xp < 1000:
      nivel = "Ferro"
  elif xp <= 2000:
      nivel = "Bronze"
  elif xp <= 5000: 
      nivel = "Prata"
  elif xp <= 7000:
      nivel = "Ouro"
  elif xp <= 8000:
      nivel = "Platina"
  elif xp <= 9000:
      nivel = "Ascendente"
  elif xp <= 10000:
      nivel = "Imortal"
  else:
      nivel = "Radiante"
    
print(f"O Herói de nome {nome} está no nível de {nivel}")

nome_heroi = input("Digite o nome do herói: ")
xp_heroi = int(input("Digite a quantidade de XP do herói: "))
classificar_heroi(nome_heroi, xp_heroi)