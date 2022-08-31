from tkinter import N


def main():
    number = input("Ingrese número del 1 al 12")
    multiplicationTable = getMultiplicationTable(number)
    testMultiplicationTableFunction()

def getMultiplicationTable(number):
    multiplicationTable = {}
    for i in range(11):
        multiplicationTable[str(number +" x "+ i)] = {number*i}
    return multiplicationTable

def testMultiplicationTableFunction():
    number= 5
    multiplicationTableTest = getMultiplicationTable(number)
    
    if multiplicationTableTest.get("5 X 8") != "" and   multiplicationTableTest.get("5 X 8") != 40:
        print("Success!")