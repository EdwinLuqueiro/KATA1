"""Primer if """

contraseña = "contraseña"

Contraseña_in = input("Introdusca la contraseña ")
Contraseña_in = Contraseña_in.lower()

if contraseña == Contraseña_in:
    print("Felicitaciones la contraseña es correcta")
else:
    print(":( la contraseña no coincide")
