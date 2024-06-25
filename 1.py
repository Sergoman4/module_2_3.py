my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print(my_list)
while True:
  number = int(input('ведите число: '))
  if number <= 0:
    break
  elif number > 0:
    print(number)
