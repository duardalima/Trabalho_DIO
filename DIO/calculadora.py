# Determina o nível do jogador baseado no número de vitórias

if vitorias < 10:
    nivel = "Ferro"
elif 10 <= vitorias <= 20:
    nivel = "Bronze"
elif 21 <= vitorias <= 50:
    nivel = "Prata"
elif 51 <= vitorias <= 80:
    nivel = "Ouro"
elif 81 <= vitorias <= 90:
    nivel = "Diamante"
elif 91 <= vitorias <= 100:
    nivel = "Lendário"
else:
    nivel = "Imortal"

#Mensagem final com o saldo e o nível do jogador
print(f"O Herói tem um saldo de {saldo_vitorias} está no nível de {nivel}")