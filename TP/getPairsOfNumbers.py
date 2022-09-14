def getPairsOfNumbers():
   tribonacci = [3, 5, 9]
   pairOfNumbers = {}
   oddNumber =3
   while len(pairOfNumbers) < 100:
       flag = False
       for numb in tribonacci:
           if oddNumber%numb == 0:
               if tribonacci[-1] <= oddNumber:
                   tribonacci.append(tribonacci[-1] + tribonacci[-2] + tribonacci[-3])
               break
           if numb == tribonacci[-1] or oddNumber < tribonacci[-1]:
               flag = True
               break

       if flag:
           if tribonacci[-1]<= oddNumber:
               tribonacci.append(tribonacci[-1] + tribonacci[-2] + tribonacci[-3])
           for i in range(len(tribonacci)-1, 0, -1):
               if tribonacci[i] < oddNumber:
                   pairOfNumbers[oddNumber] = tribonacci[i]
                   break
       oddNumber += 2

   return pairOfNumbers

if __name__ == '__main__':
   dicc = getPairsOfNumbers()
   print(dicc)