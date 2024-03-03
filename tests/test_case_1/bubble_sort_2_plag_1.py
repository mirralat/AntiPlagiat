def bubbleSort(massiv):
  for i in range(len(massiv)):
    swapped = False
    for j in range(0, len(massiv) - i - 1):
      if massiv[j] > massiv[j + 1]:
        temp = massiv[j]
        massiv[j] = massiv[j+1]
        massiv[j+1] = temp

        swapped = True

    if not swapped:
      break

data = [-3, 47, 0, 12, -8]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)
