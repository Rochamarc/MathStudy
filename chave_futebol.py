from random import choice

# fases = oitavas, quartas, semi e final.
# 16 clubes => 8 clubes => 4 clubes e 2 clubes
# 15 confrontos

clubes = [ f"Clube {i+1}" for i in range(16) ]

clubes.sort()

oitavas = []
for i in range(len(clubes)//2):
    confronto = []
    for y in range(2):
        print(clubes)
        confronto.append(clubes.pop())
    oitavas.append(confronto)
    print(oitavas)
def mostrar_chave(clubes) -> list:
    """"""
    return None


