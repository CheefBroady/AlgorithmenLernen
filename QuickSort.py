
import random
import time

# def quickSort(arr):
#     if len(arr) < 2:
#         return arr
#     elif len(arr) == 2:
#         if arr[0] > arr[1]:
#             moveItem = arr[0]
#             arr[0] = arr[1]
#             arr[1] = moveItem
#         return arr
#     elif len(arr) > 2:
#         lowerArray = []
#         upperArray = []
#         pivotElement = arr[0]
#         for i in range(len(arr)):
#             if arr[i+1] < pivotElement:
#                 lowerArray.append(arr[i+1])
#             else:
#                 upperArray.append(arr[i+1])
#             return(quickSort(lowerArray), quickSort(upperArray))

def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivotItem = arr[random.randrange(0,len(arr)-1)]
        lowerArray = [i for i in arr[1:] if i <= pivotItem]
        upperArray = [i for i in arr[1:] if i > pivotItem]
        return quickSort(lowerArray) + [pivotItem] + quickSort(upperArray)

myArray = []
# print("Länge des Arrays vor initialisierung:", len(myArray))

arraySize = int(input("Wieviele Element soll das Array enthalten?\n"))
if arraySize == 0:
    print("Es wird kein Array angefordert")
    exit
else:
    print("Bitte geben Sie die", arraySize, "Werte für Ihr Array ein!")
    for i in range(arraySize):
        myArray.append(int(input(str(i+1)+". Wert: ")))
    print("Array vor dem Sortieren:", myArray)
    print("Array nach dem Sortieren:", quickSort(myArray))










