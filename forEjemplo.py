#creamos lista de referencia

lista = ["Alvin", 19, 'Masculino']

# operador "in" hace referencia a que pertenece
#haremos que imprima todos los datos de la lista con for y while
# ACLAREMOS QUE DATO YA SE CONVERTIRA EN EL VALOR DE LA LISTA NO 
#ES UN INDICE DE RECORRIDO
for dato in lista:
    print(dato)

print("\nMetodo con while\n")
c=0
while c < len(lista):
    print(lista[c]); c+=1


print("imprimiendo números de 0 a 9 xd")
for i in range(0, 10):
    print(i)

#tamaño de la lista
print(f"La lista es \n{len(lista)}")

#imprimiendo toda la lista haciendo uso de range y el for
#en el range sobreentiende que iniciará desde 0, por eso 
#solo se le da el parámetro tope
# for j in range(len(lista)):
#     print(lista[j])