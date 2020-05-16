precio= 3.49
descuento = 0.4
precio_con_descuento = precio * descuento

numero_barras = input("Ingrese número de barras vendidas")
numero_barras = int(numero_barras)

print("Precio habitual: " + str(precio))
print("Descuento por no ser fresca: " + str(precio_con_descuento))
print("Valor total: " + str(numero_barras * precio_con_descuento))