"""
conversão de alfanumericos e inteiros    
"""

# elabore um programa que receba um numero inteiro como alfanumerico ;
# após isso deverá ser multiplicado por 12 ;
# no final, print o numero de digitos do resultado


i = "1510"
m = int(i)
m*= 12
f = str(i)

#   The strip() method returns a copy of the string by removing both the leading and the trailing characters 
#   (based on the string argument passed).
print(f"Numero de digitos de {f.strip()}= {len(f)}")


