import json
import requests
data = {"t":66, "u":72, "d":90, "r":84, "j":36, "g":50, "s":94, "q":62, "f":35}
with open("reto/dic_reto.json", "w") as write_file:
  json.dump(data, write_file)

with open("reto/dic_reto.json", "r") as read_file:
  laminas = json.load(read_file)
# print(laminas)

datoRecibido =()
datoRecibido = (input(datoRecibido))
datosRecibido=list(datoRecibido)
# print(datoRecibido)

contador = 0
for key in laminas:
  if key in datoRecibido:
    contador = contador + laminas[key]
print(contador,"")

for x in datoRecibido:
  if x in laminas:
    print(x, end=" ")
