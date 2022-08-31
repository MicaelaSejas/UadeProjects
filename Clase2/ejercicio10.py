def main():
    removingList = ["Hola", "chau", "Aaaa"]
    newDictionary = {"Hola": 1, "Jejeje": 2, "chau": 3,"Aaaa": 4}
    returnedDictionary = deleteKeys(removingList, newDictionary)
    for data in returnedDictionary.items():
        print(data)

def deleteKeys(removingList, newDictionary):
    for i in removingList:
        newDictionary.pop(i)
    return newDictionary