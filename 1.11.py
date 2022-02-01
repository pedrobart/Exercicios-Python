"""
-> Determine o comprimento de uma cadeia de carateres;
    
-> Concatene duas cadeias de carateres;

-> Converta uma cadeia de carateres em letras MAISCULAS; 

-> Extraia uma subcadeia de carateres;

-> Determine a posição de INICIO de uma subcadeia de carateres;

-> Verifique se duas cadeias de carateres são iguais;

-> Compare em termo Alfabeticos, duas cadeias de carateres;

-> Elimine os espaços á Esquerda e á Direita de uma cadeia de carateres;
    
"""

if __name__ == '__main__':
    
#Determine o comprimento de uma cadeia de carateres;
    E1, E2=len("Porto"), "Lisboa,\n"
    
#Concatene duas cadeias de carateres; + Converta uma cadeia de carateres em letras MAISCULAS;
    E3, E4 = "Fica no sul", "coimbra".upper()
    
#Extraia uma subcadeia de carateres;
    E5 = "Pedro Bart"[0:15]
    
#Determine a posição de INICIO de uma subcadeia de carateres;
    E6, E7, E8 = "ABCD","ABBCD","ABCCD"
# 
    E9, E10 = "Pedro Bart", "   finish   ".strip(" ")
    
    print(E1)
    print(E2+E3)
    print(E4)
    print(E5)
    print(E6==E7)
    print(E7<E8)
    print(E9.find("Porto", 1, len(E9)))
    print(E10)
    
"""
5
Lisboa,
Fica no sul
COIMBRA
Pedro Bart
False
True
-1
finish
"""

#CONCATENAR. Concatenar é a junção de 2 cadeias de caracteres 
# e que dá origem a uma nova string que é formada pela junça das 2 partes. 
# A concatenação, pode ser a direita ou então a esquerda de outra string.
concatenação = "123" + "456"
print(concatenação)

