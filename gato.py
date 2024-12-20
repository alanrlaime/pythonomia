def suma(a,b):
  return a+b

a = int(input("n1: "))
b = int(input("n2: "))
print("La suma de",a,b,"es",suma(a,b))

def raiz(a):
  return a**(1/2)

print("operacion de radical")

def ultimo-digito(a):
  return a%10

#Recursividad

def factoria(n):
  if n == 1:
    return 1
  else:
    return n*factorial(n-1)

def multiplicacion(a,b):
  return a*b
print("con los gatos")
print(suma(2,5))


def gatos(n):
  print("tengo frio")

def sumarDigitosPares(n,c,s):
  if(c != 0):
    h = n%10
    n = n/10
    c = c-1
    if( h/2 == 0):
      s = s+h
    return sumarDigitosPares(n,c,s)
  return s
  
