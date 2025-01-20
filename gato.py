import numpy as np

def suma(a,b):
  return a+b
#Recursividad

def factoria(n):
  if n == 1:
    return 1
  else:
    return n*factorial(n-1)

def sumarDigitosPares(n,c,s):
  if(c != 0):
    h = n%10
    n = n/10
    c = c-1
    if( h/2 == 0):
      s = s+h
    return sumarDigitosPares(n,c,s)
  return s

def menu__dias(a):
  dias = {
    0 : "lunes",
    1 : "martes",
    2 : "miercoles
  }
  entr = int(input("opciones: "))
