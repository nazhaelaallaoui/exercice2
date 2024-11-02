
U1 = []
L = []
U2 = [0] * 10  
print("Entrez les valeurs pour le tableau U1 :")
for i in range(10):
    valeur = int(input(f"U1[{i}]: "))
    U1.append(valeur)

print("Entrez les valeurs pour le tableau L (0 ou 1 uniquement) :")
for i in range(10):
    while True:
        valeur = int(input(f"L[{i}]: "))
        if valeur in [0, 1]:
            L.append(valeur)
            break
        else:
            print("Veuillez entrer 0 ou 1 seulement.")
for i in range(10):
    if L[i] == 1:
        U2[i] = U1[i]


print("Tableau U2:", U2)