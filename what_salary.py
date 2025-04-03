import calculator.operators as operators

salaire = 0
hebdomadaire = 0
horaire = 0

salaire_annuel = float(input("Entrez votre salaire annuel : "))
heures_travaillees = float(input("Entrez le nombre d'heures travaillées par semaine : "))

salaire = operators.salaire_mensuel(salaire_annuel)
hebdomadaire = operators.salaire_hebdomadaire(salaire)
horaire = operators.salaire_horaire(hebdomadaire, heures_travaillees)

print("Votre salaire annuel est de", salaire_annuel, "euros.")
print("Votre salaire mensuel est de", salaire, "euros.")
print("Votre salaire hebdo est de", hebdomadaire, "euros.")
print("Votre salaire horaire est de", horaire, "euros.")