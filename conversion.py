nombres = "1,2,3,4"
my_list = nombres.split(',')
print(my_list)
liste_entiers = []
total = 0
moyenne = 0
for i in my_list:
 liste_entiers.append(int(i))
 print(type(int(i)))
 print(liste_entiers)

print('Fin de la conversion de la chaîne en entier')

for nb in liste_entiers:
 total += nb

moyenne = total / len(liste_entiers)
print(f'Le total est : {total}')
print(f'La moyenne est : {moyenne}')

for nbr in liste_entiers:
 if nbr > moyenne:
  print(f'{nbr} est supérieur à la moyenne qui est de {moyenne}')