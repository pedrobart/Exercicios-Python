'''
enumerações 
'''
'''
Uma enumeração é um conjunto de nomes simbólicos (membros) vinculados a valores únicos e constantes.
Dentro de uma enumeração, os membros podem ser comparados por identidade, e a enumeração em si pode ser iterada.
'''
'''

Enumerations are created using the class syntax, 
which makes them easy to read and write.

To define an enumeration, subclass Enum as follows:

from enum import Enum
>>> class Color(Enum):
...     RED = 1
...     GREEN = 2
...     BLUE = 3

'''

from enum import Enum

nivel = "1,2,3,4,5"
situacao = "prova oral,Aprovado,Distinção"
notas = Enum("Notas", "E,D,C,B,A")

print(notas.A.value,"-distinção: ",notas.A.name)
    

    