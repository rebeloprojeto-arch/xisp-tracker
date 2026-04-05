import json
from datetime import datetime

with open("data/xp.json", "r") as f:
    data = json.load(f)

xp_atual = data["xp_atual"]
meta = data["meta"]
xp_diario = data["xp_diario"]
cartao = data["cartao"]

if cartao == "100":
    xp_real = xp_diario * 2
elif cartao == "50":
    xp_real = xp_diario * 1.5
else:
    xp_real = xp_diario

xp_atual += xp_real

media_diaria = xp_real
restante = meta - xp_atual
dias_restantes = restante / media_diaria if media_diaria > 0 else 0

data["xp_atual"] = xp_atual
data["ultimo_update"] = str(datetime.now())

with open("data/xp.json", "w") as f:
    json.dump(data, f, indent=4)

print("XP Atual:", xp_atual)
print("Dias restantes:", dias_restantes)
