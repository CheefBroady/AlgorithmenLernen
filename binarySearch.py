import time


def binarySearch(list, item):
    low = 0 # Indexposition der Liste (Anfang)
    high = len(list)-1 # Indexposition am Ende der Liste
    counter = 0

    while low <= high:
        mid = (low + high) // 2  # die Liste wird halbiert, der Index in der Mitte wird gesucht
        # mid = int(mid)
        guess = list[mid] # Wert aus gesuchtem Index wird ausglesen
        counter += 1    # zählt Durchläufe (Test)
        schleifenInfo = str(counter) + ". Durchlauf: Auf Index: " + str(mid) + " befindet sich der Wert: " + str(list[mid])
        if guess == item:
            print(schleifenInfo)
            print("Benötigte Durchläufe:", counter) # gibt Anzahl Durchläufe aus (Test)
            return mid
        if guess > item:
            print(schleifenInfo)
            high = mid - 1
        else:
            print(schleifenInfo)
            low = mid + 1 
    return None



myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

while True:
    inputItem = int(input("Bitte geben Sie ein Zahl zwischen 1 und 13 an!\n"))
    if inputItem < 1 or inputItem > 13:
        print("Gesuchter Wert:", inputItem ,"befindet sich außerhalb des möglichen Wertearrays!")
    else:
        print("\n***** Gesuchter Wert:", inputItem, "*****\n")
        searchIdx = binarySearch(myList, inputItem)
        print("Gesuchter Wert:", inputItem, "wurde auf dem Listenindex:", searchIdx, "(" + str(myList[searchIdx]) + ") aufgefunden!\n\n" )
        break


time.sleep(1.5)