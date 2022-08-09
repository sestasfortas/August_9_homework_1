first_number = float(input("input first number: "))
second_number = float(input("input second number: "))
what_to_do = (input("'*','/'"))
if what_to_do == '*':
    print(f"{first_number} * {second_number} =", first_number * second_number)
elif what_to_do == '/':
    print(f'{first_number} / {second_number} =', first_number / second_number)
else:
    print("Whatafak you want from me")