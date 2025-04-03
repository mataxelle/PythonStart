import calculator.operators

addition_input_1 = float(input("Add: "))
addition_input_2 = float(input("and: "))

addition_resultat = calculator.operators.addition(addition_input_1, addition_input_2)
print('The result of the addition is = ', addition_resultat)

multiplication_input_1 = float(input("Multiply: "))
multiplication_input_2 = float(input("and: "))

multiplication_resultat = calculator.operators.multiplication(multiplication_input_1, multiplication_input_2)
print('The result of the multiplication is = ', multiplication_resultat)