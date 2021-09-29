#Estrutura de Tupla: coordenadas = (-23.691067557530193, -46.6574982153427)
#Estrutura de Lista (array): cars = ["Ford", "Volvo", "BMW"]
dict = {"brand": "Ford", "model": "Mustang", "year": 1964}

for x in range(1, 6):
    print("Aluno {}: ".format(x))
    nome = str(input("Nome: ")).strip()
    endereço = str(input("Endereço: "))
    coordenadasX = float(input("Coordenada X: "))
    coordenadasY = float(input("Coordenada Y: "))
    nomePai = str(input("Nome do pai: "))
    nomeMãe = str(input("Nome da mãe: "))
    temIrmãos = str(input("Você tem irmãos? [S/N]"))
    if temIrmãos == "S":
        quantIrmãos = int(input("Quantos? "))
        for y in range(1, quantIrmãos+1):
            irmãos = str(input("Qual é o nome do {}° irmão? ".format(y)))
            nomesIrmãos = []
            nomesIrmãos.append(irmãos)
    elif temIrmãos == "N":
        continue
    else:
        print("Resposta inválida.")
    temAnimais = str(input("Você tem animais de estimação? [S/N]"))
    if temAnimais == "S":
        quantAnimais = int(input("Quantos? "))
        for z in range(1, quantAnimais+1):
            animais = str(input("Qual é o nome do {}° animal? ".format(z)))
            nomesAnimais = []
            nomesAnimais.append(animais)
    elif temAnimais == "N":
        continue
    else:
        print("Resposta inválida.")

coordenadas = (coordenadasX, coordenadasY)

Y = "aluno"
Z = Y + x
Z = {
    "Nome: ": nome(x),
    "Endereço: ": endereço(x),
    "Nome do pai: ": nomePai(x),
    "Nome da mãe: ": nomeMãe(x),
    "Tem irmãos: ": temIrmãos(x),
    "Número de irmãos: ": quantIrmãos(x),
    "Nome dos irmãos: ": nomesIrmãos(x),
    "Tem animais: ": temAnimais(x),
    "Número de animais: ": quantAnimais(x),
    "Nome dos animais: ": nomesAnimais(x)
}

print(Z)