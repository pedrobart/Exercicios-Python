"""
conversões de inteiros, reais, alfanumericos e datas

"""
#____Elabore um programa que converta: 
# Um numero real num inteiro;
# Um numero inteiro num real;
# Um numero numa cadeia de carateres;
# Uma cadeia de carateres num numero;
# Uma cadeia de carateres numa data;

from datetime import datetime

     

if __name__ == "__main__":

    a = float("235.6")
    i = int(5.75)
    r = float(7)
    s = str(4.568)
    d = datetime.strptime("12/01/2022", "%d/%m/%Y").date()

    print(f"{i}\n{r}\n{s}\n{a}\n{d:%d/%m/%y}")
    
    """
5
7.0
4.568
235.6 
12/01/22
    """
