
"""Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
"""
#list
compra_semanal = ['leche', 'fruta', 'verduras', 'aguacates']

#tuple
alim_sana = ('legumbre', 'verdura', 'fruta', ('grasas saludables', 'snacks de fibra', 'especias'))

#float 
a = 4.51

#integer
a = 10

#decimal
from decimal import Decimal
coste_placabase = Decimal(15.45) * Decimal(0.02)

#diccionary
clientes_vip = {
  "persona_1": {
    "nombre": "David", 
    "ciudad": "Valencia"
  },
  "persona_2": {
    "nombre": "Chris",
    "ciudad": "Madrid"
  },
  
  "persona_3": {
    "nombre": "Sam",
    "ciudad": "Sevilla"
  }
}



"""Exercise 2: Round your float up.
"""
import math
print(math.ceil(4.51))




"""Exercise 3: Get the square root of your float.
"""
import math
a = 4.51
sqrt_a = math.sqrt(a)




"""Exercise 4: Select the first element from your dictionary.
"""
clientes_vip = {
  "persona_1": {
    "nombre": "David", 
    "ciudad": "Valencia"
  },
  "persona_2": {
    "nombre": "Chris",
    "ciudad": "Madrid"
  },
  
  "persona_3": {
    "nombre": "Sam",
    "ciudad": "Sevilla"
  }
}

#a) para obtener el primer elemento completo
lista_vip = list(clientes_vip.items())  #convertido a lista conteniendo claves y valores 
print(lista_vip[0]) # devuelve ('persona_1', {'nombre': 'David', 'ciudad': 'Valencia'})

#b) para obtener el valor de la primera clave "persona_1"
first_value = clientes_vip["persona_1"]  
print(first_value)  # devuelve  {'nombre': 'David', 'ciudad': 'Valencia'}




"""Exercise 5: Select the second element from your tuple.
"""
alim_sana = ('legumbre', 'verdura', 'fruta', ('grasas saludables', 'snacks de fibra', 'especias'))
print(alim_sana[1])




"""
Exercise 6: Add an element to the end of your list.
"""
compra_semanal = ['leche', 'fruta', 'verduras', 'aguacates']

compra_semanal.extend(["tofu"])             #sin conservar la lista inicial

compra_definit = compra_semanal + ["tofu"]   #en nueva lista
print (compra_definit)  




"""
Exercise 7: Replace the first element in your list.
"""
compra_semanal[0] = "leche de soja"
print (compra_semanal)




"""
Exercise 8: Sort your list alphabetically.
"""

compra_semanal.sort()



"""
Exercise 9: Use reassignment to add an element to your tuple.
"""
alim_sana = ('legumbre', 'verdura', 'fruta', ('grasas saludables', 'snacks de fibra', 'especias'))

alim_sana += ('0conserv-0azucar',)



