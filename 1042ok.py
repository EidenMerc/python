#Pegando as informações do teclado

entrada = input().split("")

#transformando os numeros em inteiros
# uso de vetores, colocando cada numero dentro de uma posição

a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

# colocando em uma lista

lista = [a,b,c]

#Odenando a lista usando o metodo  .sort

lista.sort()

#Mostrando os numeros ordenados

print (lista[0])
print (lista[1])
print (lista[2])
print ("")

# mostrando as informaçoes na mesma ordem que foi inserida conforme foi pedido pelo enunciado

print(a)
print(b)
print(c)
