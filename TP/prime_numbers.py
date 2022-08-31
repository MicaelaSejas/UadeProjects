from math import trunc

def getPrimeNumbers():
   primerNumber = []
   for i in range(11, 100, 2):
       isPrimer = True

       for j in range(2, trunc(i / 2), 1):
           if i % j == 0:
               isPrimer = False

       if isPrimer:
           primerNumber.append(i)
   return primerNumber


def getCircularPrimeNumbers(numberList):
   circularPrimerNumbers = []
   for number in numberList:
       reversedNumber = int(str(number)[::-1])
       if reversedNumber in numberList:
           circularPrimerNumbers.append(number)
   return circularPrimerNumbers


if __name__ == '__main__':
   primeNumbers = getPrimeNumbers()
   print(primeNumbers)
   print(getCircularPrimeNumbers(getPrimeNumbers()))
