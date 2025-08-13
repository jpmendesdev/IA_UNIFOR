import numpy as np
# <<DOCUMENTAÇÃO DO NUMPY JP>>

#1) MANIPULAÇÃO DE ARRAYS
# 1 dimensão array
# 2 dimensões matriz
# 3 ou mais dimensões tensor

a = np.array([[1,2,3,4,5,6], [7,8,9,10,11,12]])
#print(a)

#Criação n arrayas bidimensionais com valores zero com dimensões escolhidas

zero = np.zeros(shape = (5,3,6))
# print(zero)

#Criação de um array bidimensional com valores 1 

um_array = np.ones((2,3))
# print(um_array)


#Cria um array bidimensional com valores randômicos
vazio = np.empty((3,4))
# print(vazio)

#Cria um array passando um range, não precisa digitar de 1 a 5 por ex
#consegue pular o range de tanto em tanto
arr = np.arange(50,200,30)
# print(arr)

array_linear = np.linspace(0,100,20,endpoint=False)
print(array_linear)