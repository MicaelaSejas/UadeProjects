from math import trunc


"""getPrimeNumbers recorre un intervalo de numeros y guarda en una lista aquellos que sean primos.
Guardando el 1 y el 2, nos permite obtener esos dos numeros primos y poder saltear los pares, que nunca son primos.
En este Tp se consideran los números de un solo dígito como numeros circulares por si mismos, sin embargo, de considerarse 
como 05 -> 50, se podría empezar desde el 11 ya que estos quedarian excluidos desde el comienzo.
"""
def getPrimeNumbers():
   primerNumber = [1, 2]
   for i in range(3, 100, 2):
       isPrimer = True

       for j in range(2, trunc(i / 2), 1):
           if i % j == 0:
               isPrimer = False
               break

       if isPrimer:
           primerNumber.append(i)
   return primerNumber


"""getCircularPrimeNumbers convierte cada numero de la lista en un string al cual invierte y vuelve a 
pasar a numero. Luego se fija si está dentro del string y en caso de estarlo, lo agrega en la lista a retornar.
Podría invertirse el número haciendo operaciones mátemáticas sin embargo, el uso de strings
permite enviar en la lista numeros mas grandes de dos caracteres (en caso de ser necesario).
"""
def getCircularPrimeNumbers(numberList):
   circularPrimeNumbers = []
   for number in numberList:
       reversedNumber = int(str(number)[::-1])
       if reversedNumber in numberList:
           circularPrimeNumbers.append(number)
   return circularPrimeNumbers


if __name__ == '__main__':
   primeNumbers = getPrimeNumbers()
   print(f"The prime numbers are: {primeNumbers}\n")
   circularPrimeNumbers = getCircularPrimeNumbers(getPrimeNumbers())
   print(f"The circular prime numbers are: {circularPrimeNumbers}\n")
