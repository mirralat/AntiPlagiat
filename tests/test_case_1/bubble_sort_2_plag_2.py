import random

def sartirovka(sartirovka_target):
  for i in range(len(sartirovka_target)):
    im_gay = False
    for j in range(0, len(sartirovka_target) - i - 1):
      if sartirovka_target[j] > sartirovka_target[j + 1]:
        temp = sartirovka_target[j]
        sartirovka_target[j] = sartirovka_target[j+1]
        sartirovka_target[j+1] = temp

        im_gay = True

    if not im_gay:
      break

data = []
for i in range(4):
    data.append(random.randint(3,9))

sartirovka(data)

print('Братишка я тебе подарочек насортировал:')
print(data)
